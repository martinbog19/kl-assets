import requests
import os



BASE_URL = "http://site.api.espn.com/apis/site/v2/"


def get_endpoint(api_endpoint: str, params: dict = None) -> requests.Response:
    query_url = os.path.join(BASE_URL, api_endpoint)
    response = requests.get(query_url, params=params)
    response.raise_for_status()
    return response



    # url = f"http://site.api.espn.com/apis/site/v2/sports/{api_path}/teams"
    # response = requests.get(url)
    # response.raise_for_status()
    # data = response.json()

    # if not os.path.exists(f"graphics/logos/{league}"):
    #     os.makedirs(f"graphics/logos/{league}")

    # with open(f"utils/abbr_{league}.json", "r") as f:
    #     abbr_dict = json.load(f)

    # for tm_data in data["sports"][0]["leagues"][0]["teams"]:
        
    #     logo_url = tm_data["team"]["logos"][0]["href"]
    #     team = tm_data["team"]["displayName"]
    #     tm = abbr_dict[team]

    #     with open(f"graphics/logos/{league}/{tm.upper()}.png", "wb") as f:
    #         img_resp = requests.get(logo_url)
    #         f.write(img_resp.content)