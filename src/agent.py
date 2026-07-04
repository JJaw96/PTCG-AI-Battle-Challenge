import random
from pathlib import Path

# Get the correct path to the deck file
deck_path = Path(__file__).parent / "decks" / "deck.csv"

with open(deck_path) as f:
    deck = [int(line.strip()) for line in f if line.strip()]


def agent(obs_dict):
    print("Agent obs keys:", list(obs_dict.keys()))

    if "select" not in obs_dict or obs_dict.get("select") is None:
        print("Deck submission phase - returning deck")
        return deck

    # Game loop
    select = obs_dict["select"]
    options = select.get("option", [])
    max_count = select.get("maxCount", 1)

    if not options:
        print("No options - returning empty")
        return []

    # Random action select
    chosen = random.sample(range(len(options)), min(max_count, len(options)))
    print(f"Randomly chose actions: {chosen}")

    return chosen
