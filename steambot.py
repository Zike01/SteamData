import requests


class SteamBot:
    def __init__(self, key):
        self.params = {
            "key": key
        }

        self.url = None

    def get_most_played(self):
        self.url = "https://api.steampowered.com/ISteamChartsService/GetMostPlayedGames/v1/"
        return self.get_data()

    def get_trending(self):
        pass

    def get_popular(self):
        pass

    def get_hot_releases(self):
        pass

    def get_data(self):
        games = requests.get(self.url, params=self.params).json()["response"]["ranks"]
        # Obtain (rank, game_name, peak) from games data
        games_list = []
        for game in games:
            rank = game["rank"]
            
            # get game name from appid
            try:
                appid = game["appid"]
                url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
                game_data = requests.get(url, params=self.params).json()
                game_name = game_data[f"{appid}"]["data"]["name"]
            except KeyError:
                continue

            peak = game["peak_in_game"]

            games_list.append((rank, game_name, peak))

        return games_list
