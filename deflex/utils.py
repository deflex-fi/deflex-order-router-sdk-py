import requests

def fetch_api_data(api: str, params: dict, use_post: bool = False):
    fullUrl = "https://api.deflex.fi/api/{api}?".format(api=api)
    if use_post:
        response = requests.post(fullUrl, json=params)
    else:
        for key in params:
            fullUrl += key + '=' + str(params[key]) + '&'
        response = requests.get(fullUrl)
    return response.json()