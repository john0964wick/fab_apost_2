from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT keyword, COUNT(*), MAX(timestamp) FROM logs GROUP BY keyword")
    data = cur.fetchall()
    conn.close()
    return render_template("dashboard.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
