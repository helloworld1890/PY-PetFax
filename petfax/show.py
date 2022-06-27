from flask import (Blueprint, render_template)
import json

display = Blueprint('show', __name__, url_prefix='/pets/<int:id>')
pets = json.load(open('pets.json'))
print(pets)

@display.route('/')
def index(id):
    return render_template('show.html', pet=pets[id -1])
