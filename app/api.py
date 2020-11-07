from flask import Flask
from flask import jsonify
from .config import STAR_WARS_ROOT_URL, STAR_SHIPS_PATH
from .filters import sort_by_hyperdrive_rating

import requests

START_SHIPS_URL = f'{STAR_WARS_ROOT_URL}/{STAR_SHIPS_PATH}'
app = Flask(__name__)


def get_starships():
    data = requests.get(START_SHIPS_URL)
    response = data.json()
    status = data.status_code
    if status == 200:
        starships = response['results']
        return starships
    return []


@app.route('/', methods=['GET'])
def root():
    return "Starship sorting API"


@app.route('/starships', methods=['GET'])
def starships():
    response = get_starships()
    sorted_starships = sort_by_hyperdrive_rating(starships=response)
    return jsonify({'data': sorted_starships})

