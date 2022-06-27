from flask import Blueprint

form  = Blueprint('create', __name__, )

@form.route('/pets/create')
def index():
    return 'form page'