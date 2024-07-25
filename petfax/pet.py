from flask import Blueprint, render_template, abort
import json

pets = json.load(open('pets.json'))

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:index>')
def show(index):
    pet = next((p for p in pets if p['pet_id'] == index), None)
    if pet is None:
        abort(404)
    return render_template('show.html', pet=pet)
