import requests
import json
import os

from kl_assets.api.espn import get_endpoint
from kl_assets.utils import sanitize_name
from kl_assets.config import SAVE_FACES


leagues = {
    "nba": "basketball/nba",
    "nfl": "football/nfl",
    "mlb": "baseball/mlb",
    "nhl": "hockey/nhl",
}

for i, (league, api_path) in enumerate(leagues.items()):

    print(f"\n[{i+1}/{len(leagues)}] Processing {league.upper()}...")

    response = get_endpoint(f"sports/{api_path}/teams")
    data = response.json()

    if not os.path.exists(f"graphics/logos/{league}"):
        os.makedirs(f"graphics/logos/{league}")

    with open(f"utils/abbr_{league}.json", "r") as f:
        abbr_dict = json.load(f)

    for j, team in enumerate(data["sports"][0]["leagues"][0]["teams"]):
        
        tm_data = team["team"]
        logo_url = tm_data["logos"][0]["href"]
        team_name = tm_data["displayName"]
        print(f"\n    {team_name}...")
        tm = abbr_dict[team_name]
        tm_id = tm_data["id"]

        with open(f"graphics/logos/{league}/{tm.upper()}.png", "wb") as f:
            img_resp = requests.get(logo_url)
            f.write(img_resp.content)

        if not SAVE_FACES.get(league, False):
            continue

        roster_response = get_endpoint(f"sports/{api_path}/teams/{tm_id}/roster")

        if not os.path.exists(f"graphics/faces/{league}/{tm.upper()}"):
            os.makedirs(f"graphics/faces/{league}/{tm.upper()}")

        for athlete in roster_response.json()["athletes"]:

            if "headshot" not in athlete:
                continue
            
            player_id = athlete["id"]
            player_name = athlete["headshot"]["alt"]
            print(f"        {player_name}...")
            headshot_url = athlete["headshot"]["href"]
            sanitized_name = sanitize_name(player_name)
            with open(f"graphics/faces/{league}/{tm.upper()}/{player_id}_{sanitized_name}.png", "wb") as f:
                hs_response = requests.get(headshot_url)
                f.write(hs_response.content)