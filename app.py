from flask import Flask
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

VERSION = "1.0"

@app.route("/")
def index():
    count = r.incr("hits")
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitOps Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: #0f172a;
                color: white;
                text-align: center;
            }}
            .card {{
                background: #1e293b;
                padding: 60px 80px;
                border-radius: 16px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.5);
            }}
            h1 {{ font-size: 3em; margin: 0 0 10px 0; color: #38bdf8; }}
            .version {{ font-size: 1.2em; color: #94a3b8; margin-bottom: 30px; }}
            .count {{ font-size: 5em; font-weight: bold; color: #f0f9ff; }}
            .label {{ color: #64748b; margin-top: 10px; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 GitOps Demo</h1>
            <div class="version">Version {VERSION}</div>
            <div class="count">{count}</div>
            <div class="label">visites enregistrées</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)