"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    Coefficient of variation (stdev / mean) of sentence lengths in words.

    Returns:
        A float >= 0. Higher means MORE varied sentence length, which is more
        human-like. AI text marches in even step, so low CoV = more AI-like.
        This needs to be FLIPPED before contributing to the AI score.

    Edge case: a single sentence has no spread — returns 0.0, which maps to
    "AI-like" after flipping. A one-sentence submission is too short to be
    confident about; callers should treat this as weak evidence only.
    """
    sent_list = sentences(text)
    if len(sent_list) < 2:
        return 0.0
    lengths = [len(words(s)) for s in sent_list]
    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    return statistics.stdev(lengths) / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary, which is
        more human-like. This needs to be FLIPPED before contributing to the
        AI score.

    Falls as text gets longer because common words repeat — two submissions of
    very different lengths aren't directly comparable on this measure alone.
    """
    word_list = words(text)
    if not word_list:
        return 0.0
    return len(set(word_list)) / len(word_list)


def punctuation_density(text: str) -> float:
    """
    Ratio of expressive punctuation characters to total characters.

    Counts semicolons, colons, em-dashes, en-dashes, and exclamation marks —
    the punctuation that varies most between writers. Periods and commas are
    excluded because they're too universal to be informative.

    Returns:
        A float >= 0. Higher means more expressive punctuation, which tends to
        be more human-like. This needs to be FLIPPED before contributing to the
        AI score.
    """
    if not text:
        return 0.0
    expressive = sum(1 for ch in text if ch in ";:—–!")
    return expressive / len(text)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. Higher means more likely AI.

    Each raw measure points toward "human" when high, so each is flipped
    before combining. Scaling:

      - spread_score:  CoV is squashed with a logistic centered at 0.5
        (CoV ≥ 0.5 is varied enough to read as human; CoV near 0 reads as AI)
      - ttr_score:     TTR is naturally 0–1; flip gives the AI direction
      - punct_score:   density is tiny (typically 0–0.03); squashed to 0–1
        with a logistic centered at 0.005

    Weights: spread 0.45, TTR 0.40, punctuation 0.15 — punctuation gets less
    weight because it's the easiest to manipulate.
    """
    cov = sentence_length_spread(text)
    ttr = type_token_ratio(text)
    dens = punctuation_density(text)

    # Flip each so that higher = more AI, then squash to 0–1.
    # Spread: logistic centered at CoV=0.5, steepness 4
    spread_score = 1.0 / (1.0 + (cov / 0.5) ** 4) if cov > 0 else 1.0

    # TTR: high TTR = human = low AI score; already 0–1
    ttr_score = 1.0 - ttr

    # Punctuation: logistic centered at density=0.005, steepness 3
    # Very little expressive punctuation → AI-like → high score
    punct_score = 1.0 / (1.0 + (dens / 0.005) ** 3) if dens > 0 else 1.0

    score = 0.45 * spread_score + 0.40 * ttr_score + 0.15 * punct_score
    return round(min(max(score, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text):.4f}  (higher = more human)")
    print(f"type_token_ratio         {type_token_ratio(text):.4f}  (higher = more human)")
    print(f"punctuation_density      {punctuation_density(text):.4f}  (higher = more human)")
    print(f"style_signal             {style_signal(text):.4f}  (higher = more AI)")
