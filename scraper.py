from playwright.sync_api import sync_playwright
import random
from proxy_fetcher import get_random_proxy

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Linux; Android 10)..."
]

def scrape_fb_keywords():
    with sync_playwright() as p:
        proxy = get_random_proxy()
        browser = p.chromium.launch(proxy={"server": proxy})
        ctx = browser.new_context(user_agent=random.choice(user_agents))
        page = ctx.new_page()
        page.goto("https://www.facebook.com/search/pages?q=viral")
        page.wait_for_timeout(5000)
        items = page.query_selector_all('div[role="article"]')
        kws = [item.inner_text().split('\n')[0] for item in items[:5]]
        browser.close()
        return kws

def scrape_posts_from_page(page_name):
    with sync_playwright() as p:
        proxy = get_random_proxy()
        browser = p.chromium.launch(proxy={"server": proxy})
        ctx = browser.new_context(user_agent=random.choice(user_agents))
        page = ctx.new_page()
        page.goto(f"https://www.facebook.com/{page_name}")
        page.wait_for_timeout(5000)
        items = page.query_selector_all('div[role="article"]')
        texts = [item.inner_text() for item in items[:3]]
        browser.close()
        return texts
