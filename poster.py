from playwright.sync_api import sync_playwright
from time import sleep
from proxy_fetcher import get_random_proxy

def post_to_fb(email, pwd, content):
    with sync_playwright() as p:
        proxy = get_random_proxy()
        browser = p.chromium.launch(headless=False, proxy={"server": proxy})
        ctx = browser.new_context()
        page = ctx.new_page()
        page.goto("https://facebook.com/login")
        sleep(3)
        page.fill("input[name=email]", email)
        page.fill("input[name=pass]", pwd)
        page.click("button[type=submit]")
        sleep(5)
        page.goto("https://facebook.com/me")
        sleep(3)
        page.click("div[aria-label='on your mind']")
        page.fill("div[role=textbox]", content)
        page.click("text=Post")
        sleep(5)
        browser.close()
