import requests
import random
import socket

def is_proxy_working(proxy, timeout=3):
    try:
        proxies = {"http": proxy, "https": proxy}
        r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=timeout)
        return r.status_code == 200
    except:
        return False

def get_random_proxy():
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    r = requests.get(url)
    proxy_list = r.text.strip().split('\n')
    random.shuffle(proxy_list)
    for p in proxy_list:
        proxy = f"http://{p.strip()}"
        if is_proxy_working(proxy):
            return proxy
    raise Exception("No valid proxies found.")
