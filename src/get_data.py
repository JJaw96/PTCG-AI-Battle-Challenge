import kagglehub

kagglehub.login()
path = kagglehub.competition_download("pokemon-tcg-ai-battle-challenge-strategy")
print("Path to competition files:", path)
