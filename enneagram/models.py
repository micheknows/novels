from flask import Flask, jsonify

class Enneagram:

    def __init__(self):
        self.types = {
            "Type 1": {
                "Name": "The Reformer",
                "Traits": ["Principled", "Purposeful", "Self-Controlled", "Perfectionistic"],
                "Fear": "Of being corrupt/evil, defective",
                "Desire": "To be good, to have integrity, to be balanced",
                "Motivations": ["Want to be right", "to strive higher and improve everything", "to be consistent with their ideals", "to justify themselves", "to be beyond criticism so as not to be condemned by anyone"]
            },
            "Type 2": {
                "Name": "The Helper",
                "Traits": ["Generous", "Demonstrative", "People-Pleasing", "Possessive"],
                "Fear": "Of being unwanted, unworthy of being loved",
                "Desire": "To feel loved",
                "Motivations": ["Want to be loved", "to express their feelings for others", "to be needed and appreciated", "to get others to respond to them", "to vindicate their claims about themselves"]
            },
            # Rest of types
        }

app = Flask(__name__)

enneagram = Enneagram()

@app.route("/api/enneagram")
def get_enneagram():
    return jsonify(enneagram.types)

if __name__ == "__main__":
    app.run(debug=True)