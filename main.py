import os
from scraper import scrape_fb_keywords, scrape_posts_from_page
from ai_generator import generate_clickbait
from bitly import shorten_url
from poster import post_to_fb
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

DB = "database.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            keyword TEXT,
            post_text TEXT,
            timestamp DATETIME
        )
    """)
    conn.commit()
    conn.close()

def log_post(keyword, content):
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO logs (keyword, post_text, timestamp) VALUES (?, ?, ?)",
                 (keyword, content, datetime.utcnow()))
    conn.commit()
    conn.close()

def full_pipeline():
    init_db()
    keywords = scrape_fb_keywords()
    for kw in keywords:
        posts = scrape_posts_from_page(kw)
        for p in posts:
            clicky = generate_clickbait(p)
            short = shorten_url(os.getenv("ADSTER_LINK"), os.getenv("BITLY_TOKEN"))
            content = clicky.replace("[ADLINK]", short)
            post_to_fb(os.getenv("FB_EMAIL"), os.getenv("FB_PASS"), content)
            log_post(kw, content)

if __name__ == "__main__":
    full_pipeline()
