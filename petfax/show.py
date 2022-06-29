from flask import (Blueprint, render_template)
import json

bp2 = Blueprint('show', __name__, url_prefix='/pets/<int:id>')
pets = json.load(open('pets.json'))
print(pets)

@bp2.route('/')
def index(id):
    return render_template('pets/show.html', pet=pets[id -1])
