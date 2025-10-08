import os
from flask import Flask

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 8080))

@app.route("/")
def home():
    return "Hello, Render!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
