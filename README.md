# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

A piece of text travels through seven things on its way from arriving to the
label a reader sees. Each one adds something the next depends on.

1. **The route — `app.py::submit`.** A `POST /submit` request arrives carrying
   `{"text": "...", "creator_id": "..."}`. Flask parses the JSON body and the
   handler pulls out `text` and `creator_id`. *What it adds:* the entry point
   and input validation — it decides what happens when `text` is missing,
   empty, or enormous before anything downstream runs. It also mints a
   `content_id` (a UUID) that ties this submission to every later log entry and
   to any appeal.

2. **Signal one — `detector.py::model_signal`.** The text goes to the local
   gpt2 model, which measures **perplexity** (how predictable the text is) and
   squashes it onto a 0–1 score where higher means more AI-like. *What it
   adds:* the first piece of evidence — a reading of the text *for meaning*.

3. **Signal two — `stylometry.py::style_signal`.** The same text is measured
   *as text* (sentence-length spread, type-token ratio, punctuation density),
   combined into a second 0–1 score pointing the same way (higher means more
   AI-like). *What it adds:* an independent second opinion that doesn't depend
   on understanding the words.

4. **The combining rule — `scoring.py::combine_signals`.** The two 0–1 scores
   become one 0–1 `combined_score`. *What it adds:* the single number the whole
   decision rests on — and the place where "which way do I want to be wrong?"
   actually gets decided.

5. **The label mapping — `scoring.py::score_to_label`.** The combined score is
   compared against `HUMAN_THRESHOLD` and `AI_THRESHOLD` to produce a `guess`
   (`human` / `unsure` / `ai`) and the full `label` sentence a person reads.
   *What it adds:* translation from a machine number into something a human can
   act on.

6. **The audit log — `audit.py::log_decision`.** The decision is written as one
   JSON line with all nine fields (timestamp, content_id, creator_id, guess,
   model_score, style_score, combined_score, label, status=`decided`). *What it
   adds:* a permanent, readable trace — the evidence the next unit grades, and
   the record `/appeal` reads back.

7. **The response.** The handler returns `content_id`, `guess`, `confidence`,
   `label`, `model_score`, and `style_score` to the caller. *What it adds:* the
   answer the reader sees, and the two signal scores the next unit's tools read
   straight off the wire.

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** *Predictability.* It runs gpt2 locally, computes the
**perplexity** of the text (mean negative log-likelihood per token,
exponentiated), and maps it through a logistic curve onto 0–1. Low perplexity —
text the model "could have guessed" — scores high (AI-like); high perplexity
scores low (human-like).

**Why that might differ between human and AI writing:** A language model
generates by repeatedly choosing a *likely* next word, so AI text tends to be
text a model finds easy to predict. Human writing wanders more — odd word
choices, abrupt turns, the specific instead of the typical — which reads as
higher perplexity.

**What it can't see:** **Predictability is not authorship.** What this signal
actually rewards is *common words in short, ordinary sentences* — so a real
person writing plainly (someone writing in a second language and sticking to
vocabulary they're sure of, a younger writer, anyone writing simply on purpose)
scores about as machine-like as a machine does. The reverse trips it too: dense,
ornate prose full of rare words reads as *human*, because rare words are exactly
what the model fails to predict. So the writers it most readily accuses are the
ones with the least room to argue back. This is structural, not a bug — and it
is the false positive this whole project is about.

### Signal two — the style signal

**What it measures:** The *shape* of the text, with no understanding of its
meaning — three measures combined: **sentence-length spread** (do sentences vary
in length or march in step?), **type-token ratio** (how much of the vocabulary
repeats), and **punctuation density** (how much punctuation, and how varied).

**Why that might differ between human and AI writing:** "Most likely next word,"
averaged across a whole passage, produces regularity — even, mid-length
sentences and a narrower band of vocabulary. Human writing is lumpier: a
three-word sentence next to a forty-word one, with more idiosyncratic
punctuation.

**What it can't see:** **It cannot read.** It has no idea what the text *says*,
so anything that changes the shape without changing the substance moves it —
adding typos, breaking long sentences into short ones, pasting in a quotation.
That is very cheap to do on purpose, and the next unit's attack set is built to
do exactly this.

### Tracing the false positive

<!-- Milestone 1: follow a real writer whose genuine work gets called AI. -->

**The person:** A real writer — say someone writing in their second language,
in clear, plain, short sentences — submits their own genuine work.

**The score they get, step by step:**

- **Signal one (model signal)** reads their plain, common-word, short-sentence
  prose as *highly predictable*. Low perplexity → **high** `model_score`
  (machine-like). This is the structural blind spot firing on exactly the
  person least able to argue back.
- **Signal two (style signal)** sees low sentence-length spread and a narrow
  vocabulary — the marks it associates with AI — so it *also* leans **high**.
- **The combining rule** takes two high numbers and produces a **high**
  `combined_score`. Both signals agree, and both are wrong for the same reason.
- **The label mapping** compares that score to `AI_THRESHOLD`. It clears it, so
  the guess is **`ai`**.

**What the label says to them:** the high-confidence-AI sentence. To a person
who wrote every word themselves, that reads as an accusation — and it landed
because their writing is *plain*, not because it's fake.

**What they can do about it — `POST /appeal`:** They send
`{"content_id": "...", "reasoning": "..."}`. The service confirms the
`content_id` exists, calls `audit.log_appeal(...)` — which moves the item's
status to **`under_review`** and writes the appeal beside the original decision
in the append-only log — and confirms back to the writer. No automatic
re-check: a human now has to look. The appeal endpoint is the only thing
standing between a wrong accusation and nothing at all.

**Why this decides the thresholds:** Because both signals fail *the same way* on
this writer, no weighting in `combine_signals` saves them — the only lever that
protects them is how wide the **unsure band** is (the gap between
`HUMAN_THRESHOLD` and `AI_THRESHOLD`). Widening it means fewer plain-writing
humans accused, at the cost of more AI text slipping through as "unsure." There
is no setting that avoids the trade — only settings that decide who pays for it.

### The endpoint contract

<!-- Milestone 1: the shape of the two endpoints — what goes in, what comes
     out, field by field. The contract everything else has to keep. -->

**`POST /submit`**

*In* (JSON body):

| Field | Type | Required | Meaning |
|---|---|---|---|
| `text` | string | yes | The writing to judge. A few sentences minimum — the model raises on fewer than 3 tokens. |
| `creator_id` | string | yes | Who submitted it. Ties the decision to a submitter; becomes the rate-limit key later. |

*Out* (JSON body, HTTP 200):

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string (UUID) | Unique id for this submission. The handle for `/appeal` and every log entry. |
| `guess` | string | Machine-readable: `human` / `unsure` / `ai`. |
| `confidence` | float 0–1 | How strongly the score sits toward its end of the scale. |
| `label` | string | The full human-readable sentence a reader sees. |
| `model_score` | float 0–1 | Signal one's score (higher = more AI). |
| `style_score` | float 0–1 | Signal two's score (higher = more AI). |

*Error outcomes:* `400` for missing/empty/too-short `text`; `501
not_implemented` until the route is built.

**`POST /appeal`**

*In* (JSON body):

| Field | Type | Required | Meaning |
|---|---|---|---|
| `content_id` | string | yes | The id from the `/submit` response being challenged. |
| `reasoning` | string | yes | The writer's explanation of why the call was wrong. |

*Out* (JSON body, HTTP 200):

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | Echoes the item now under review. |
| `status` | string | `under_review` — confirms the status moved. |
| `message` | string | Human confirmation the appeal was recorded. |

*Error outcomes:* `404` if the `content_id` doesn't exist in the log (don't fail
silently — a typo here is the most common hour-eater in this milestone); `400`
for missing fields.

**Reading it back — could someone else build against this without asking me a
question?** Almost. Two things to pin down so nobody has to guess:

- **`confidence` needs a formula.** "How strongly the score sits toward its
  end" is ambiguous until defined — e.g. the distance of `combined_score` from
  0.5, scaled to 0–1 — otherwise two implementers compute it differently.
- **Branch on `guess`, never on `label`.** `guess` is the stable machine enum
  (`human` / `unsure` / `ai`); `label` is prose that can be reworded freely. A
  consumer parsing the sentence would break the moment the wording changes.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
