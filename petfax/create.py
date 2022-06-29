from flask import (Blueprint, render_template)

bp3  = Blueprint('create', __name__, url_prefix="/form" )

@bp3.route('/')
def index():
    return render_template('facts/form.html')

