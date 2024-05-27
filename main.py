from dotenv import load_dotenv
import os
from steambot import SteamBot
import pandas as pd

load_dotenv()

bot = SteamBot(os.getenv("API_KEY"))

def get_most_played():
    most_played_games = bot.get_most_played()
    df = pd.DataFrame(most_played_games, columns=["Rank", "Game Name", "24h Peak"])
    df.to_csv("most_played_games.csv", sep="\t", encoding="utf-8", index=False)

if __name__ == "__main__":
    get_most_played()
