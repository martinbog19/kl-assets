import requests
import json
import os

from kl_assets.api.espn import get_endpoint



leagues = {
    "nba": "basketball/nba",
    "nfl": "football/nfl",
    "mlb": "baseball/mlb",
    "nhl": "hockey/nhl",
}

for league, api_path in leagues.items():

    print(f"Processing {league.upper()}...")

    response = get_endpoint(f"sports/{api_path}/teams")
    data = response.json()

    if not os.path.exists(f"graphics/logos/{league}"):
        os.makedirs(f"graphics/logos/{league}")

    with open(f"utils/abbr_{league}.json", "r") as f:
        abbr_dict = json.load(f)

    for tm_data in data["sports"][0]["leagues"][0]["teams"]:
        
        logo_url = tm_data["team"]["logos"][0]["href"]
        team = tm_data["team"]["displayName"]
        tm = abbr_dict[team]

        with open(f"graphics/logos/{league}/{tm.upper()}.png", "wb") as f:
            img_resp = requests.get(logo_url)
            f.write(img_resp.content)