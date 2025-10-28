import requests
import json



leagues = {
    "nba": "basketball/nba",
    "nfl": "football/nfl",
    "mlb": "baseball/mlb",
}

for league, api_path in leagues.items():

    url = f"http://site.api.espn.com/apis/site/v2/sports/{api_path}/teams"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    with open(f"utils/abbr_{league}.json", "r") as f:
        abbr_dict = json.load(f)

    for tm_data in data["sports"][0]["leagues"][0]["teams"]:
        
        logo_url = tm_data["team"]["logos"][0]["href"]
        team = tm_data["team"]["displayName"]
        tm = abbr_dict.get(team)

        with open(f"graphics/logos/{league}/{tm.upper()}.png", "wb") as f:
            img_resp = requests.get(logo_url)
            f.write(img_resp.content)