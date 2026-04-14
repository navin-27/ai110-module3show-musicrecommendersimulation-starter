# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  
VibeFinder 1.0  

---

## 2. Intended Use  

This recommender system suggests songs based on user preferences such as genre, mood, and energy level. It is designed for educational purposes to simulate how recommendation systems work.

The system assumes that users have clear preferences for genre, mood, and energy. It is intended for classroom exploration rather than real-world deployment.

---

## 3. How the Model Works  

The model compares user preferences with song features like genre, mood, and energy.

Each song is given a score:
- +2 if genre matches
- +1 if mood matches
- Energy score based on how close the song's energy is to the user's preference

Songs with higher scores are ranked higher and recommended to the user.

---

## 4. Data  

The dataset contains around 10 songs with different genres, moods, and energy levels.

Genres include pop, rock, lofi, jazz, and others. Moods include happy, chill, intense, and relaxed.

The dataset is small and does not represent all music tastes.

---

## 5. Strengths  

The system works well for users with clear preferences.

It correctly prioritizes songs that match both genre and mood. The scoring system is simple and easy to understand.

---

## 6. Limitations and Bias  

The system only considers a few features (genre, mood, energy).

It does not consider artist preference, popularity, or user history.

The dataset is small, so recommendations are limited and may not be diverse.

---

## 7. Evaluation  

I tested the system using different user profiles.

For example, when the user prefers "pop" and "happy", the system correctly ranks matching songs higher.

The results matched expectations in most cases.

---

## 8. Future Work  

- Add more features like tempo and danceability  
- Improve explanation quality  
- Increase dataset size  
- Add user history-based recommendations  

---

## 9. Personal Reflection  

I learned how recommendation systems use simple scoring to suggest items.

I also learned how small changes in logic can affect results.

This project helped me understand how apps like Spotify recommend music.