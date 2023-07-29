import json
import random
from flask import Flask, jsonify

app = Flask(__name__)

# Load compliments from JSON file
with open('index.json') as file:
    compliments = json.load(file)

@app.route('/')
@app.route('/all')
def get_all_compliments():
    return jsonify(compliments)

@app.route('/random')
def get_random_compliment():
    random_compliment = random.choice(compliments)
    return jsonify(random_compliment)

@app.route('/id/<int:id>')
def get_compliment_by_id(id):
    if id < 1 or id > len(compliments):
        return jsonify({"error": "Invalid ID"})
    
    compliment = compliments[id - 1]
    return jsonify(compliment)

if __name__ == '__main__':
    app.run()
