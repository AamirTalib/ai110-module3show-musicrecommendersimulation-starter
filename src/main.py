"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print("Loaded songs:", len(songs))

    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.90,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.30,
            "likes_acoustic": True,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.90,
            "likes_acoustic": False,
        },
        "Conflicting Edge Case": {
            "favorite_genre": "lofi",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "likes_acoustic": True,
        },
    }

    for name, prefs in profiles.items():
        print("\n" + "=" * 60)
        print(f"Profile: {name}")
        print("=" * 60)

        recommendations = recommend_songs(prefs, songs, k=5)

        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            match_pct = score * 100
            print(f"\n{rank}. {song['title']} - {song['artist']}")
            print(f"   Final score: {score:.3f}  ({match_pct:.1f}% match)")
            print("   Reasons:")
            for reason in explanation.split("; "):
                print(f"     - {reason}")


if __name__ == "__main__":
    main()
