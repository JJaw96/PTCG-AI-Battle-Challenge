from kaggle_environments import make
from agent import agent
from pathlib import Path
import json

# deck.csv must contain exactly 60 card IDs (one integer per line)
deck_path = Path(__file__).parent / "decks" / "deck.csv"
deck = [
    int(line.strip()) for line in deck_path.read_text().splitlines() if line.strip()
]

if len(deck) != 60:
    raise ValueError(f"deck.csv contains {len(deck)} cards; expected exactly 60.")

print(f"Loaded deck with {len(deck)} cards. Starting mirror match simulation...")

env = make("cabt", configuration={"decks": [deck, deck]})

env.run([agent, agent])

print("Status:", env.state)
print("Number of steps:", len(env.steps) if hasattr(env, "steps") else "N/A")
print("Final info keys:", list(env.info[-1].keys()) if env.info else "No info")

# Get the base HTML from kaggle
base_html = env.render(mode="html")

# Prepare environment data
environment_data = {
    "steps": env.steps,
    "configuration": env.configuration,
    "name": env.name,
    "id": "local-sim",
    "viewer": None,
}

env_json = json.dumps(environment_data)

# Replace empty environment definition if it exists
output_html = base_html.replace(
    "const environment = {};", f"const environment = {env_json};"
)

output_path = Path(__file__).parent / "sim.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(output_html)

print(f"Simulation finished. Open sim.html to inspect the full game replay.")
print("Final status:", env.state)
