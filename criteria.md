# Acceptance Criteria

## 1. False positives — at most 1 in 10 human submissions is labeled high-confidence AI

Of 10 pieces I wrote myself, at most 1 is labeled `high-confidence AI`. The other 9 must receive either `high-confidence human` or `unsure`.

**Why this target:** A wrong accusation on a writing platform is not a minor inconvenience — it calls someone's integrity into question. Missing an AI submission costs less socially than falsely convicting a real writer. 1 in 10 is already generous; it leaves room for edge cases like very plain writing while still holding the system accountable. Anything looser than that is not a real constraint.

---

## 2. Score spread — clearly-AI and clearly-human text differ by at least 0.4

A passage I generate with an LLM and a passage I write myself must produce combined scores at least 0.40 apart (e.g., AI ≥ 0.65, human ≤ 0.25). If the two signals agree on nothing across the full range, there is no detection system — just a random number.

**Why this target:** If clearly-different inputs score within 0.2 of each other, the thresholds I set in Milestone 4 are meaningless: any threshold that catches the AI text will also catch the human text. A 0.40 gap gives the combining rule enough room to place a label. Without this, the rest of the criteria can't be met honestly.

---

## 3. Label coverage — all three labels are reachable with real inputs

Given at least 10 test submissions, each of the three labels (`high-confidence human`, `unsure`, `high-confidence AI`) appears at least once. No label is stuck unreachable because of how thresholds are set.

**Why this target:** A system that never returns `unsure` has removed the one honest label — the one that admits the detection problem is hard. If I can't produce all three labels with real inputs, my thresholds are either too aggressive (everything is AI) or too permissive (everything is human), and the design is broken regardless of the accuracy numbers.

---

## 4. The appeal path — every appeal changes status and is recorded

Given a `content_id` from a prior `/submit` response, a POST to `/appeal` must: (a) return HTTP 200 with `"status": "under_review"`, and (b) produce a new log entry visible at `/log`. Both must hold on every valid appeal, not most.

**Why this target:** The appeal endpoint is the only recourse a falsely-accused writer has. If it silently fails, swallows the request, or logs nothing, the person has nowhere to go. "Usually works" is not a standard for the endpoint that matters most to a real human. This criterion has no tolerance because neither does the writer on the other end.

---

## 5. Bad input — missing or empty text returns 400, not a crash

A POST to `/submit` with no `text` field, with `text` set to an empty string `""`, or with `text` set to a single word returns HTTP 400 with an error message. It must not return 500, hang, or raise an unhandled exception.

**Why this target:** The attack set in Unit 8 will send malformed inputs on purpose. A crash on bad input is a worse outcome than a rejected submission — it hands an attacker a way to take the service down and produces a 500 that looks like the handler failed when it never ran. The route must validate at its boundary before touching any signal.
