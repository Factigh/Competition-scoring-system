# Competition Scoring System

A console-based Python program that scores a multi-week contest. In every week each contestant also acts as a coach and gives points to three other contestants, and the audience votes as well. The program calculates weekly and overall rankings, week championships, and a coach-by-contestant score table.

> **Note:** This is my second project in the Algorithms and Programming course. This time the focus was on **methods (functions)**: the program is split into small functions with parameters and return values, instead of one long script. The scenario and rules come from the course assignment.

## How the scoring works

- The user enters the **number of contestants** (at least 5) and the **number of weeks** (at least 3).
- Every week:
  - Each contestant, acting as a **coach**, gives **1, 2 and 3 points** to three different contestants. A coach cannot score themselves or give two scores to the same contestant.
  - The **audience** gives 1, 2 and 3 points to three different contestants. These points are multiplied by `(number of contestants - 1)`, so the audience's influence grows with the size of the contest.
  - **Total score = coach score + audience score.**
- Contestants are ranked by total score. If totals are tied, the contestant with the higher coach score ranks first.
- Scores add up from week to week, so the program prints the **overall standings** after each week.

Example with 5 contestants: if the audience gives its 3-point vote to contestant 2, the audience score is `3 × (5 - 1) = 12`. If the coaches gave the same contestant 3 + 2 + 3 points, the coach score is 8 and the weekly total is 20.

## Output

After each week:
- Scoring results for the week (rank, contestant no, coach score, audience score, total score)
- Overall standings so far

At the end of the competition:
- Overall standings based on coach scores only
- Overall standings based on audience scores only
- Total score of every contestant for each week, and the number of **week championships** (the contestant(s) with the highest total in a week; ties count for everyone)
- A **coach table** showing how many points each contestant received from each coach in total (a contestant's own column shows `-`)

Afterwards the program asks whether to organize a new competition.

## Input validation

- Non-numeric input prints `Invalid entry.` and asks again (handled with `try/except`)
- Contestant and week counts below the minimum are rejected
- Coach votes: a number from 1 to the contestant count, not the coach themselves, and not a contestant that coach has already scored this week
- Audience votes: a number from 1 to the contestant count, no repeats within the week

## How to run

Requires Python 3.6 or newer (uses f-strings). No external libraries.

```bash
python competition_scoring.py
```

Example start of a run:

```
Enter contestant number 5
Enter number of weeks 3
Which number of contestant 1.coach give the score 1? 2
Which number of contestant 1.coach give the score 2? 4
Which number of contestant 1.coach give the score 3? 3
...
```

## Program structure

| Function | What it does |
| --- | --- |
| `control_input` | Reads an integer with a minimum value and handles invalid input |
| `createlist` | Creates a 2D list filled with zeros |
| `controlcoach` / `controlaudience` | Read and validate coach and audience votes |
| `week_score` | Collects all votes of one week and builds the weekly score list |
| `weeksorted` / `sortlist` | Ranking by total score, ties broken by coach score |
| `overall` | Adds the weekly scores to the running totals and ranks them |
| `trioscore` | Builds the coach-only and audience-only standings |
| `champs` / `maximum` | Store weekly totals and count week championships |
| `table`, `mini_table`, `table_champ`, `table_coach` | Print the formatted tables |
| `main` | Runs the whole competition and the "new competition?" loop |

## Known limitations

- Everything is entered by hand. Even the smallest contest (5 contestants, 3 weeks) needs 54 vote entries. Random or file-based votes would make testing much easier.
- Results are only printed, nothing is saved to a file.

## Concepts practiced

Functions with parameters and return values, 2D lists, `try/except` input handling, sorting with `key=lambda` (and stable sorting for tie-breaks), nested loops, formatted table output.
