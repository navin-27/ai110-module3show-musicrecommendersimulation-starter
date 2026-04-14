# 🎵 Music Recommender Simulation

## Project Summary

This project implements a simple music recommender system that suggests songs based on user preferences such as genre, mood, and energy level.

The system reads a dataset of songs and compares each song with the user’s preferences. It assigns a score to each song and returns the top recommendations along with explanations.

---

## How The System Works

The system uses the following features from each song:

* Genre (e.g., pop, rock, lofi)
* Mood (e.g., happy, chill, intense)
* Energy (a value between 0 and 1)

The `UserProfile` stores:

* Preferred genre
* Preferred mood
* Target energy level

### Scoring Logic

Each song is scored based on how well it matches the user:

* +2 points if the genre matches
* +1 point if the mood matches
* Additional score based on how close the energy value is

Songs are then sorted by score (highest first), and the top results are recommended.

---

## Getting Started

### Setup

1. (Optional) Create a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python -m src.main
```

---

## Running Tests

Run tests using:

```bash
pytest
```

---

## Experiments You Tried

I experimented with adjusting the scoring weights.

* Increasing the genre weight made recommendations more consistent
* Reducing the mood weight made results less accurate
* Energy similarity helped fine-tune ranking between similar songs

These experiments showed how changing weights directly impacts recommendations.

---

## Limitations and Risks

* The dataset is very small (around 10 songs)
* The system only considers a few features (genre, mood, energy)
* It does not consider user listening history
* It may over-prioritize genre compared to other features

---

## Reflection

This project helped me understand how recommender systems convert user preferences into scores.

I learned that even simple scoring systems can produce meaningful recommendations, but they can also introduce bias depending on how features are weighted. It also showed how real-world systems likely use much more complex data and models to improve accuracy.
