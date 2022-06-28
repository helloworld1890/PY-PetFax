from flask import (Blueprint, render_template)

form  = Blueprint('create', __name__, url_prefix="/pets/form" )

@form.route('/')
def index():
    return render_template('form.html')