# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-06 13:28
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `eda6cd7b-eb42-4603-8f0f-28e980366f03` | human | 0.308 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `e6303ba0-09ce-4bbb-be17-b6cc49c86601` | human | 0.327 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `8b559920-6ce5-467c-a664-ea44486a6778` | unsure | 0.578 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `806d0f56-9220-4fc1-a47d-39b439e82462` | unsure | 0.628 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `003ea0e7-0c63-4c09-bcdb-61978445059e` | human | 0.328 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `331f3eba-26a5-4133-b921-fab546507c95` | human | 0.418 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `97214cb0-6f62-4afc-9030-2e5f91d34ddc` | unsure | 0.573 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `807d316e-7d99-4821-9fd0-20799ff022f1` | human | 0.402 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `da30f93f-fcfa-4d0e-b372-6f683595f0be` | unsure | 0.585 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a0f9c8a4-74c5-44bf-b676-057a1ef38ed9` | ai | 0.863 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `48ec8704-1e4c-4112-8177-c278d642fb6a` | unsure | 0.574 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `49903f40-39ea-46d6-aa1b-de667e306b31` | unsure | 0.716 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `5af6d72d-19d4-45ef-a337-3053018d9a9d` | unsure | 0.723 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `78ede516-dec6-4063-8499-141a64bf428e` | unsure | 0.704 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ce202cda-456c-4bb7-a9c2-65bbddb89371` | ai | 0.764 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `8dd9dd21-61ed-4784-8661-0c35532a62af` | unsure | 0.590 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `1e192085-8800-4bf0-84b3-ec525acec377` | unsure | 0.578 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `ac81a082-4063-4bad-96ce-08b4e40e25cc` | human | 0.380 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `63851068-7340-4515-b002-92765e512f41` | human | 0.375 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `a384936f-75e0-4756-9a3c-b83a32a68691` | human | 0.229 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `8368eea3-99a4-41c9-b8a6-8400d7353c44` | unsure | 0.565 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `17f097ef-7179-416b-b376-0d8f7612d0d8` | unsure | 0.513 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `65db4db6-510b-48f0-b428-d7cfd42a20da` | human | 0.382 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `28fd1f02-e80c-4636-8b25-22f5044e8b38` | unsure | 0.551 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `bfb756d0-e876-4949-b32a-21b1aa687e82` | human | 0.180 |  |
| MF04 | malformed | text is only punctuation | 200 | `b447a1e1-3bfe-45ba-8cc0-a8e1c2cd8bcc` | human | 0.263 |  |
| MF05 | malformed | text is a very long single word | 200 | `1fc1f6cc-a04b-4102-9fd0-2a23a596bf8c` | unsure | 0.719 |  |
| MF06 | malformed | text is emoji only | 200 | `c3dfeb30-9f6e-4f24-b67e-9fac87999170` | ai | 0.999 |  |
| MF07 | malformed | text is right-to-left script | 200 | `63f78a2e-a754-4c7e-8ae3-8c95e3e04ee9` | ai | 0.953 |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1633be9b-12fc-4ff6-881b-4910fa1d4f9e` | human | 0.200 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `43f41883-44bc-460a-94ab-49c76c6b3ed1` | human | 0.200 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `096320e1-ee03-4841-964a-504c635cea4c` | human | 0.200 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `797c6e18-6733-46f9-af69-6eee7c2d0feb` | human | 0.200 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a0a2a0c6-dbe0-43bd-a0c7-b43017c2bedd` | human | 0.200 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "eda6cd7b-eb42-4603-8f0f-28e980366f03",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3085,
  "model_score": 0.1635,
  "style_score": 0.647,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "e6303ba0-09ce-4bbb-be17-b6cc49c86601",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3266,
  "model_score": 0.5943,
  "style_score": 0.2119,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "8b559920-6ce5-467c-a664-ea44486a6778",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5779,
  "model_score": 0.6662,
  "style_score": 0.4897,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "806d0f56-9220-4fc1-a47d-39b439e82462",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.628,
  "model_score": 0.6114,
  "style_score": 0.6447,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "003ea0e7-0c63-4c09-bcdb-61978445059e",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3282,
  "model_score": 0.3212,
  "style_score": 0.3353,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "331f3eba-26a5-4133-b921-fab546507c95",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.4183,
  "model_score": 0.5727,
  "style_score": 0.2638,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "97214cb0-6f62-4afc-9030-2e5f91d34ddc",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5734,
  "model_score": 0.5862,
  "style_score": 0.5606,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "807d316e-7d99-4821-9fd0-20799ff022f1",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.4017,
  "model_score": 0.2452,
  "style_score": 0.5582,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "da30f93f-fcfa-4d0e-b372-6f683595f0be",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5853,
  "model_score": 0.7042,
  "style_score": 0.4663,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "a0f9c8a4-74c5-44bf-b676-057a1ef38ed9",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8629,
  "model_score": 0.9792,
  "style_score": 0.7467,
  "label": "This submission closely matches the patterns we see in AI-generated text \u2014 predictable word choices and an even, regular style. We think it was written by an AI. If you wrote this yourself, you can appeal using the content ID in this response.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "48ec8704-1e4c-4112-8177-c278d642fb6a",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5743,
  "model_score": 0.6175,
  "style_score": 0.5311,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "49903f40-39ea-46d6-aa1b-de667e306b31",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7158,
  "model_score": 0.7387,
  "style_score": 0.693,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "5af6d72d-19d4-45ef-a337-3053018d9a9d",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7228,
  "model_score": 0.8051,
  "style_score": 0.6404,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "78ede516-dec6-4063-8499-141a64bf428e",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7042,
  "model_score": 0.8329,
  "style_score": 0.5755,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "ce202cda-456c-4bb7-a9c2-65bbddb89371",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7637,
  "model_score": 0.8005,
  "style_score": 0.727,
  "label": "This submission closely matches the patterns we see in AI-generated text \u2014 predictable word choices and an even, regular style. We think it was written by an AI. If you wrote this yourself, you can appeal using the content ID in this response.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "8dd9dd21-61ed-4784-8661-0c35532a62af",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5895,
  "model_score": 0.8814,
  "style_score": 0.4644,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "1e192085-8800-4bf0-84b3-ec525acec377",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5779,
  "model_score": 0.8816,
  "style_score": 0.4478,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "ac81a082-4063-4bad-96ce-08b4e40e25cc",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3801,
  "model_score": 0.3223,
  "style_score": 0.438,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "63851068-7340-4515-b002-92765e512f41",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3747,
  "model_score": 0.4625,
  "style_score": 0.2868,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "a384936f-75e0-4756-9a3c-b83a32a68691",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2294,
  "model_score": 0.2044,
  "style_score": 0.2545,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "8368eea3-99a4-41c9-b8a6-8400d7353c44",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5648,
  "model_score": 0.5943,
  "style_score": 0.5352,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "17f097ef-7179-416b-b376-0d8f7612d0d8",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5135,
  "model_score": 0.4998,
  "style_score": 0.5272,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "65db4db6-510b-48f0-b428-d7cfd42a20da",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3818,
  "model_score": 0.6401,
  "style_score": 0.2711,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "28fd1f02-e80c-4636-8b25-22f5044e8b38",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5506,
  "model_score": 0.5583,
  "style_score": 0.5429,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "bfb756d0-e876-4949-b32a-21b1aa687e82",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.18,
  "model_score": 0.0,
  "style_score": 0.6,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "b447a1e1-3bfe-45ba-8cc0-a8e1c2cd8bcc",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.2628,
  "model_score": 0.0112,
  "style_score": 0.85,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "1fc1f6cc-a04b-4102-9fd0-2a23a596bf8c",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.7193,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "Our signals don't agree on this one. It has features we associate with human writing and features we associate with AI-generated text. We're not confident either way. If you wrote this yourself, no action is needed \u2014 but you can appeal if this result affects you.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "c3dfeb30-9f6e-4f24-b67e-9fac87999170",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "This submission closely matches the patterns we see in AI-generated text \u2014 predictable word choices and an even, regular style. We think it was written by an AI. If you wrote this yourself, you can appeal using the content ID in this response.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "63f78a2e-a754-4c7e-8ae3-8c95e3e04ee9",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "This submission closely matches the patterns we see in AI-generated text \u2014 predictable word choices and an even, regular style. We think it was written by an AI. If you wrote this yourself, you can appeal using the content ID in this response.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "1633be9b-12fc-4ff6-881b-4910fa1d4f9e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2001,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "43f41883-44bc-460a-94ab-49c76c6b3ed1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2001,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "096320e1-ee03-4841-964a-504c635cea4c",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2001,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "797c6e18-6733-46f9-af69-6eee7c2d0feb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2001,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "a0a2a0c6-dbe0-43bd-a0c7-b43017c2bedd",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.2001,
  "model_score": 0.0287,
  "style_score": 0.6,
  "label": "This submission shows the patterns we'd expect from a person \u2014 varied style, unexpected word choices, and the kind of irregularity that tends to be human. We think a person wrote this.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
