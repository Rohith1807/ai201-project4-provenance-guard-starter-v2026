"""
What your test runs. ← UNIT 8, MILESTONE 3

Five criteria from criteria.md. Criterion 4 (appeal path) requires a real
content_id from a prior submit response and is tested manually — see README.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Ten pieces I actually wrote. Varied in length, register, and subject.
        # Target: at most 1 of 10 labeled high-confidence AI (guess == "ai").
        "texts": [
            # 1 — commute observation
            "The drive in this morning took forever. Someone had stopped in the middle lane near the exit ramp — not broken down, just sitting there with their blinker on like the road would eventually explain itself. I sat behind three cars that were also not moving for about four minutes. By the time I got past it I'd forgotten what I was annoyed about.",

            # 2 — coffee shop note
            "Tried the new place on Snelling. The espresso was fine but the chairs are genuinely uncomfortable in a way that felt intentional, like they don't want you staying. Ended up standing at a shelf by the window for an hour, which was actually kind of nice. Would go back but only if I had nowhere to be.",

            # 3 — class observation
            "We talked about gradient descent again today and something finally clicked that hadn't before. I think the issue was I kept picturing it as a smooth bowl but most loss surfaces aren't — there are ridges and flat stretches and the algorithm just kind of wanders until something pulls it somewhere useful. The analogy that helped was rolling a marble on a crumpled piece of paper.",

            # 4 — weekend
            "Went to the farmer's market on Saturday. Bought two things I didn't plan to buy and nothing I went for. The tomatoes I wanted were sold out by 9:30, which feels like a personal failure even though I know it isn't. Got some honey instead. The guy at the stand was extremely enthusiastic about buckwheat honey specifically and I am still thinking about that.",

            # 5 — running
            "Three miles this morning. The first half mile is always the worst — everything protests and I am very aware of my knees. After that it gets easier and I stop thinking about it. By mile two I'm usually working through something from the week and by the time I'm done I can't always remember what. That part is the point.",

            # 6 — late assignment
            "I turned in the lab report a day late because I kept convincing myself it needed one more pass and it didn't. The problem is I know what good writing looks like and I kept comparing what I had to that instead of to what was actually due. Eventually I just submitted it. Got full credit. I need to do that faster.",

            # 7 — debugging session
            "Spent most of Wednesday evening looking at a bug that turned out to be an off-by-one in a loop I'd written months ago. The error message was not helpful. The thing that finally found it was printing every index in a loop inside the loop, which is embarrassing but worked. I've left the print statement in as a warning to myself.",

            # 8 — reading
            "I'm bad at reading nonfiction slowly enough for it to stick. I read fast and then remember roughly the shape of the argument but not the specifics, which means I can describe the thesis but not defend it. I've started keeping a notepad next to whatever I'm reading and that helps but I forget to look at the notes.",

            # 9 — weather
            "November is different here than I expected it to be. It doesn't get dark early so much as the light just changes — it goes orange and low by 3pm and everything looks like it's being photographed with a filter I didn't choose. It's not unpleasant. I just notice it every day.",

            # 10 — grocery store
            "The self-checkout machine at the grocery store told me to place the item in the bagging area three times in a row for something I'd already bagged. I took it out and put it back in. The machine seemed satisfied. The woman in the lane next to me caught my eye and shook her head slowly, which felt like solidarity.",
        ],
    },

    {
        "name": "score spread",
        "criterion": 2,
        # Clearly AI text and clearly human text must differ by at least 0.40.
        # Target: |ai_score - human_score| >= 0.40.
        "texts": [
            # Clearly AI — standard generated academic paragraph
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables. These factors must be carefully evaluated to ensure optimal outcomes.",

            # Clearly human — personal, specific, irregular
            "Went for a run. Legs hurt. Worth it. I've been trying to get out before seven so I can be back before it gets too warm, which only works about half the time because I'm bad at sleeping. This morning I saw a heron standing in the drainage ditch on Cleveland and it stared at me for a long time before it flew away. I took that personally.",
        ],
    },

    {
        "name": "label coverage",
        "criterion": 3,
        # At least one of each label across the 10 submissions.
        # Sending high-AI, mid-range, and low-AI inputs to exercise all three labels.
        "texts": [
            # Clearly AI — should produce "ai"
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables. These factors must be carefully evaluated to ensure optimal outcomes.",

            # Clearly AI, second example
            "In conclusion, the evidence presented above demonstrates that effective communication is essential for organizational success. The key findings indicate that teams which prioritize information sharing consistently outperform those that do not. It is therefore recommended that organizations implement structured communication protocols to maximize efficiency.",

            # Borderline — formal but short, should land unsure
            "This report sets out the findings of the working group. The group met four times between January and March. Its remit was to review the current arrangements and to recommend changes where these were warranted. The group found that the existing arrangements are broadly sound.",

            # Borderline — human voice but structured
            "Right, so. I've been thinking about this since the meeting on Thursday and I still don't have a neat answer, but here's roughly where I've landed. The importance of effective communication at work cannot be overstated. Teams that actually tell each other things get more done.",

            # Clearly human — should produce "human"
            "Went for a run. Legs hurt. Worth it.",

            # Clearly human — conversational
            "The drive in this morning took forever. Someone had stopped in the middle lane near the exit ramp, just sitting there with their blinker on. I sat behind three cars for about four minutes.",

            # Clearly human — specific personal detail
            "Tried the new coffee place on Snelling. The espresso was fine but the chairs are uncomfortable in a way that felt intentional, like they don't want you staying. Ended up standing at a shelf by the window for an hour.",

            # Short human
            "November is different here than I expected. The light goes orange and low by 3pm and everything looks like it's being photographed with a filter I didn't choose.",

            # AI-leaning
            "There are several key considerations to keep in mind when evaluating this approach. The first consideration relates to scalability, which is a critical factor in determining long-term viability. The second consideration concerns maintainability, which affects the ongoing cost of the solution.",

            # Human-leaning
            "I turned in the lab report a day late because I kept convincing myself it needed one more pass and it didn't. Eventually I just submitted it. Got full credit.",
        ],
    },

    {
        "name": "bad input",
        "criterion": 5,
        # Missing text, empty text, null text, wrong type — all must return 400.
        # Target: 5 of 5 return status 400 (not 500, not 200).
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": 12345, "creator_id": "eval_bad_number"},
            {"text": ["a", "b"], "creator_id": "eval_bad_list"},
        ],
    },
]


# Criterion 4 (appeal path) is tested manually — it requires a real content_id
# from a prior /submit response. See README "Run Log and Verdicts" for the
# manual test output.


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
