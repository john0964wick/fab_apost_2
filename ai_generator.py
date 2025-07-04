def generate_clickbait(original_post):
    title = f"Jangan Lewatkan! {original_post[:25]}..."
    body = f"{original_post}\n\n👉 Klik untuk tahu lebih 👉 [ADLINK]"
    return f"{title}\n\n{body}"
