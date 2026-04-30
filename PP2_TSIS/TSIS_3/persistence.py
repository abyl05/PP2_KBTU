import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LEADERBOARD_FILE = os.path.join(BASE_DIR, "leaderboard.json")
SETTINGS_FILE = os.path.join(BASE_DIR, "settings.json")


# ===================== LEADERBOARD =====================
def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []

    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_score(name, score, distance):
    data = load_leaderboard()

    data.append({
        "name": name,
        "score": score,
        "distance": distance
    })

    # сортировка по дистанции (по убыванию)
    data = sorted(data, key=lambda x: x["distance"], reverse=True)

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ===================== SETTINGS =====================
def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {
            "sound": True,
            "difficulty": "normal",
            "car_color": "blue"
        }

    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)