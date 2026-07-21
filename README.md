# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.
The recommender works by comparing each songs features with what the user preferences are, It accounts for variables like Genre,mood, energy, acoustics. Every feature builds the score for each song, once every song is scored they are all sorted: highest to lowest, with highest being recommended first. 

Algorithm Recipe:
final_score = (0.40 × genre_score) + (0.30 × mood_score) + (0.15 × energy_score) + (0.15 × acoustic_score)

Some prompts to answer:

- What features does each `Song` use in your system
  - For example:
   - Genre
   - Mood 
   - Energy
   - Acousticness

- What information does your `UserProfile` store
- favorite_genre
- favorite_mood
- target_energy
- likes_acoustic

- How does your `Recommender` compute a score for each song
The recommender compares every song with the users profile and gives it a score between 0 -1 

- How do you choose which songs to recommend
The recommender calculates a score for each song, It then sorts the songs from highest score to lowest score and recommends the higher scoring songs first

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Loaded songs: 10

Top recommendations:

1. Sunrise City - Score: 0.97
Because: Genre matches (pop): +0.40; Mood matches (happy): +0.30; Energy similarity (0.82 vs 0.80): +0.15; Acoustic similarity (0.18 vs target 0.0): +0.12

2. Gym Hero - Score: 0.67
Because: Genre matches (pop): +0.40; Mood differs (intense): +0.00; Energy similarity (0.93 vs 0.80): +0.13; Acoustic similarity (0.05 vs target 0.0): +0.14

3. Rooftop Lights - Score: 0.54
Because: Genre differs (indie pop): +0.00; Mood matches (happy): +0.30; Energy similarity (0.76 vs 0.80): +0.14; Acoustic similarity (0.35 vs target 0.0): +0.10

4. Storm Runner - Score: 0.27
Because: Genre differs (rock): +0.00; Mood differs (intense): +0.00; Energy similarity (0.91 vs 0.80): +0.13; Acoustic similarity (0.10 vs target 0.0): +0.14

5. Night Drive Loop - Score: 0.26
Because: Genre differs (synthwave): +0.00; Mood differs (moody): +0.00; Energy similarity (0.75 vs 0.80): +0.14; Acoustic similarity (0.22 vs target 0.0): +0.12

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



