from flask import Flask, render_template, jsonify
from enneagram.models import Enneagram
import json

app = Flask(__name__)

enneagram = Enneagram()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/enneagram")
def get_enneagram():
    data = {
        "types": enneagram.types
    }
    return json.dumps(data, indent=4)

if __name__ == "__main__":
    app.run(debug=True)