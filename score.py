import os

HS_FILE = "highscore.txt"

def load_high_score():
    if not os.path.exists(HS_FILE):
        return 0
    with open(HS_FILE, "r") as f:
        try:
            return int(f.read())
        except ValueError:
            return 0

def save_high_score(score):
    with open(HS_FILE, "w") as f:
        f.write(str(score))