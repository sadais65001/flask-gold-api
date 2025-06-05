from flask import Flask, jsonify
import time

app = Flask(__name__)
cache = {
    "last_updated": time.strftime("%Y-%m-%d %H:%M:%S"),
    "gold_rate": "N/A"
}

@app.route("/")
def get_data():
    return jsonify(cache)

if __name__ == "__main__":
    app.run()
