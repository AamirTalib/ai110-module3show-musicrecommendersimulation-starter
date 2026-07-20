import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
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
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns them as a list of dictionaries."""
    # Resolve relative paths against the project root so `python -m src.main`
    # works no matter which directory you run it from.
    path = Path(csv_path)
    if not path.is_absolute():
        project_root = Path(__file__).resolve().parent.parent
        path = project_root / path

    songs: List[Dict] = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                songs.append({
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": int(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                })
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find songs file at: {path}")
    except ValueError as e:
        raise ValueError(f"Invalid numeric value in {path}: {e}")

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores one song against user preferences and returns (final_score, reasons)."""
    # Accept both the UserProfile-style keys and main.py's shorter keys.
    fav_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    fav_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))
    target_energy = user_prefs.get("target_energy", user_prefs.get("energy"))
    likes_acoustic = user_prefs.get("likes_acoustic", False)

    # Per-feature scores, each in the range 0.0 - 1.0.
    genre_score = 1.0 if song["genre"] == fav_genre else 0.0
    mood_score = 1.0 if song["mood"] == fav_mood else 0.0
    energy_score = 1 - abs(song["energy"] - target_energy)
    acoustic_target = 1.0 if likes_acoustic is True else 0.0
    acoustic_score = 1 - abs(song["acousticness"] - acoustic_target)

    # Weighted sum (weights total 1.0, so the score stays in 0.0 - 1.0).
    final_score = (
        0.40 * genre_score
        + 0.30 * mood_score
        + 0.15 * energy_score
        + 0.15 * acoustic_score
    )

    reasons = [
        f"Genre {'matches' if genre_score else 'differs'} "
        f"({song['genre']}): +{0.40 * genre_score:.2f}",
        f"Mood {'matches' if mood_score else 'differs'} "
        f"({song['mood']}): +{0.30 * mood_score:.2f}",
        f"Energy similarity ({song['energy']:.2f} vs {target_energy:.2f}): "
        f"+{0.15 * energy_score:.2f}",
        f"Acoustic similarity ({song['acousticness']:.2f} vs target "
        f"{acoustic_target:.1f}): +{0.15 * acoustic_score:.2f}",
    ]
    return final_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores and ranks all songs, returning the top k as (song, score, explanation)."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, reasons))

    # Highest score first; ties broken by title in alphabetical order.
    scored.sort(key=lambda item: (-item[1], item[0]["title"]))

    results = []
    for song, score, reasons in scored[:k]:
        explanation = "; ".join(reasons)
        results.append((song, score, explanation))
    return results
