import requests

def shorten_url(long_url, token):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.post("https://api-ssl.bitly.com/v4/shorten",
                      json={"long_url": long_url}, headers=headers)
    return r.json().get("link", long_url)
