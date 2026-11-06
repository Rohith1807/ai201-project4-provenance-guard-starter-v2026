# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-06 12:59
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `d264b666-363a-4e0f-a6da-44ca8be66c6d` | human | 0.236 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `d10dbcad-37c6-4d2d-9aff-9b70eff994b9` | human | 0.384 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `f643b177-cdfa-41fa-b210-45b1959ef241` | unsure | 0.604 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `8f6c8481-5e90-4693-b54d-230420b94dae` | unsure | 0.623 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9fbd1807-287b-4482-8214-fdc2cb1d937d` | human | 0.326 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `be8928fc-9652-4cb9-976c-5e51a5ef92ba` | human | 0.465 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `aa5858ed-8b8f-470f-9e13-1560aa739a95` | unsure | 0.577 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `748df7bc-20b7-4b28-ba83-3cfde07b7820` | human | 0.355 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `eaff4f3f-92b4-4d74-babd-e58962870e4d` | unsure | 0.621 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d9422928-5447-47f2-be10-2a0e87cc2613` | ai | 0.898 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `b8011202-e409-41f4-99ae-e84955fb9a56` | unsure | 0.587 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `1c5de6fe-bdfe-4e9a-b14f-48b09cbb4df8` | unsure | 0.723 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `05b5d012-3871-418d-b466-a678760233d3` | unsure | 0.748 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d6b9061e-abf0-4230-b02e-cc06954b3adb` | unsure | 0.743 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `564480c9-358f-4201-9b13-6ba00ecf8bd6` | ai | 0.775 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `52af0411-5cc1-40cd-8007-4573e7625706` | unsure | 0.652 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `454a831e-1e1a-40b0-90a0-07a778d708b8` | unsure | 0.643 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `913b71e0-17b3-436b-930e-445f05dc90da` | human | 0.363 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `59d2824e-c9f9-4510-ac7b-59e6715ede1e` | human | 0.401 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `373fcb5a-f55d-4009-a73f-8965a3a04757` | human | 0.222 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `dbb24bbc-2bc5-4ca3-8431-11bc3b4020ee` | unsure | 0.574 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `ec1f6095-1665-4b29-b3b0-d3afc55cba58` | unsure | 0.509 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a8cd63da-d7c3-4e3b-9c4d-7e99a4dd1608` | human | 0.437 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `c5bf2f4d-ee7f-4721-9593-e67f48c5f271` | unsure | 0.553 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `00475896-76db-4a4f-a753-709b06f64d27` | human | 0.090 |  |
| MF04 | malformed | text is only punctuation | 200 | `f62c38c5-dcbe-4bd9-8699-37c8d9680547` | human | 0.137 |  |
| MF05 | malformed | text is a very long single word | 200 | `7c00d645-dfbb-4105-a1f8-57d7cdd54399` | ai | 0.779 |  |
| MF06 | malformed | text is emoji only | 200 | `06d34009-98d0-4a78-bd22-79bd94660316` | ai | 0.998 |  |
| MF07 | malformed | text is right-to-left script | 200 | `899f062f-1e87-419a-be67-80d0dcb825c8` | ai | 0.939 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8be7a179-2df9-4919-bc62-40dd00cf200e` | human | 0.114 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e78c780f-cfa4-458e-9af6-2ceb7e5adf79` | human | 0.114 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `4da9faa1-c099-4a6e-8d30-01a151be4598` | human | 0.114 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7d067529-8d42-447c-b146-f6c869a50f62` | human | 0.114 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `66df13d4-0b11-4a6e-a21e-6519459f59b1` | human | 0.114 |  |
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
  "content_id": "d264b666-363a-4e0f-a6da-44ca8be66c6d",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.236,
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
  "content_id": "d10dbcad-37c6-4d2d-9aff-9b70eff994b9",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.384,
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
  "content_id": "f643b177-cdfa-41fa-b210-45b1959ef241",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6044,
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
  "content_id": "8f6c8481-5e90-4693-b54d-230420b94dae",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.6231,
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
  "content_id": "9fbd1807-287b-4482-8214-fdc2cb1d937d",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3261,
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
  "content_id": "be8928fc-9652-4cb9-976c-5e51a5ef92ba",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.4646,
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
  "content_id": "aa5858ed-8b8f-470f-9e13-1560aa739a95",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5772,
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
  "content_id": "748df7bc-20b7-4b28-ba83-3cfde07b7820",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3548,
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
  "content_id": "eaff4f3f-92b4-4d74-babd-e58962870e4d",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.6209,
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
  "content_id": "d9422928-5447-47f2-be10-2a0e87cc2613",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8978,
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
  "content_id": "b8011202-e409-41f4-99ae-e84955fb9a56",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5873,
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
  "content_id": "1c5de6fe-bdfe-4e9a-b14f-48b09cbb4df8",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.7227,
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
  "content_id": "05b5d012-3871-418d-b466-a678760233d3",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.7475,
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
  "content_id": "d6b9061e-abf0-4230-b02e-cc06954b3adb",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7428,
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
  "content_id": "564480c9-358f-4201-9b13-6ba00ecf8bd6",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7748,
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
  "content_id": "52af0411-5cc1-40cd-8007-4573e7625706",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6521,
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
  "content_id": "454a831e-1e1a-40b0-90a0-07a778d708b8",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.643,
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
  "content_id": "913b71e0-17b3-436b-930e-445f05dc90da",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3628,
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
  "content_id": "59d2824e-c9f9-4510-ac7b-59e6715ede1e",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.401,
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
  "content_id": "373fcb5a-f55d-4009-a73f-8965a3a04757",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2219,
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
  "content_id": "dbb24bbc-2bc5-4ca3-8431-11bc3b4020ee",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5736,
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
  "content_id": "ec1f6095-1665-4b29-b3b0-d3afc55cba58",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5094,
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
  "content_id": "a8cd63da-d7c3-4e3b-9c4d-7e99a4dd1608",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.4372,
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
  "content_id": "c5bf2f4d-ee7f-4721-9593-e67f48c5f271",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5529,
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
  "content_id": "00475896-76db-4a4f-a753-709b06f64d27",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.09,
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
  "content_id": "f62c38c5-dcbe-4bd9-8699-37c8d9680547",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.137,
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
  "content_id": "7c00d645-dfbb-4105-a1f8-57d7cdd54399",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7789,
  "model_score": 0.9976,
  "style_score": 0.6,
  "label": "This submission closely matches the patterns we see in AI-generated text \u2014 predictable word choices and an even, regular style. We think it was written by an AI. If you wrote this yourself, you can appeal using the content ID in this response.",
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
  "content_id": "06d34009-98d0-4a78-bd22-79bd94660316",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.998,
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
  "content_id": "899f062f-1e87-419a-be67-80d0dcb825c8",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9392,
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
  "content_id": "8be7a179-2df9-4919-bc62-40dd00cf200e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1144,
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
  "content_id": "e78c780f-cfa4-458e-9af6-2ceb7e5adf79",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1144,
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
  "content_id": "4da9faa1-c099-4a6e-8d30-01a151be4598",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1144,
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
  "content_id": "7d067529-8d42-447c-b146-f6c869a50f62",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1144,
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
  "content_id": "66df13d4-0b11-4a6e-a21e-6519459f59b1",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.1144,
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
