import sys

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
GRAY = "\033[90m"
RESET = "\033[0m"

# Evaluation criteria
CRITERIA = {
    "Script and Narrative": 0.0,
    "Direction": 0.0,
    "Acting": 0.0,
    "Technical Aspects": 0.0,
    "Theme and Relevance": 0.0,
    "Entertainment and Engagement": 0.0,
    "Originality and Innovation": 0.0,
    "Genre Consistency": 0.0,
    "Overall Satisfaction": 0.0,
}


def print_header():
    header = f"""
{GRAY}
----------------------
      MOVIESTAR
----------------------

# SCRIPT AND NARRATIVE
- Story coherence and internal consistency.
- Originality and creativity.
- Character development and emotional depth.
- Narrative pace and structure.

# DIRECTION
- Director's ability to guide actors and story.
- Aesthetic and stylistic choices that enhance the narrative.
- Control of pace and dramatic tension.

# ACTING
- Convincing and natural performances.
- Chemistry between characters.
- Acting suited to the film's genre and tone.

# TECHNICAL ASPECTS
- Cinematography: framing, lighting, colors.
- Editing: narrative flow, seamless cuts.
- Sound and score: emotional impact, audio clarity, music suitability.
- Visual effects: narrative integration, quality, and realism.

# THEME AND RELEVANCE
- Depth and relevance of the theme.
- Ability to provoke reflection or empathy.
- Message conveyed and cultural or social impact.

# ENTERTAINMENT AND ENGAGEMENT
- Ability to hold the audience's attention.
- Appropriate pacing and memorable moments.

# ORIGINALITY AND INNOVATION
- Fresh approach to familiar ideas.
- Experimentation with style, narrative, or visuals.

# GENRE CONSISTENCY
- Meets or subverts genre expectations convincingly.

# RATING SCALE
- 5.0: Masterpiece / Essential
- 4.5: Exceptional
- 4.0: Great
- 3.5: Very Good
- 3.0: Good / Decent
- 2.5: Mediocre / Mixed
- 2.0: Weak
- 1.5: Very Bad
- 1.0: Awful
- 0.5: Atrocious
{RESET}
"""
    print(header)


def get_valid_score(criterion):
    while True:
        try:
            score = float(input(f"{GREEN}{criterion}: {RESET}"))
            if 0 <= score <= 10:
                return score
            print(f"{RED}Error: enter values between 0 and 10 only{RESET}")
        except ValueError:
            print(f"{RED}Error: enter a valid number.{RESET}")
        except KeyboardInterrupt:
            print(f"\n{RED}Program terminated.{RESET}")
            sys.exit(1)


def calculate_final_score(scores):
    total = sum(scores.values())
    return total / len(scores) / 2


def format_stars(score):
    full_stars = int(score)
    has_half_star = score % 1 >= 0.5
    return "*" * full_stars + ("½" if has_half_star else "")


def main():
    print_header()
    scores = CRITERIA.copy()

    for criterion in scores:
        scores[criterion] = get_valid_score(criterion)

    final_score = calculate_final_score(scores)
    stars = format_stars(final_score)

    print(
        f"\nFinal Score: {YELLOW}{stars}{RESET} {GRAY}[{final_score:.1f}]{RESET}")


if __name__ == "__main__":
    main()
