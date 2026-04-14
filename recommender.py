from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        return "Explanation placeholder"
import csv

def load_songs(csv_path: str):
    songs = []

    print(f"Loading songs from {csv_path}...")

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            # convert numbers properly
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])

            songs.append(row)

    print(f"Loaded {len(songs)} songs")  # DEBUG LINE

    return songs
def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0
    reasons = []

    # Genre match
    if song["genre"] == user_prefs["genre"]:
        score += 2
        reasons.append("genre match")

    # Mood match
    if song["mood"] == user_prefs["mood"]:
        score += 1
        reasons.append("mood match")

    # Energy similarity
    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = 1 - energy_diff
    score += energy_score
    reasons.append("similar energy")

    return score, reasons
def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    # sort by score (highest first)
    scored_songs.sort(key=lambda x: x[1], reverse=True)

    return scored_songs[:k]
