from flask import (Blueprint, redirect, render_template, request, redirect)

bp4  = Blueprint('fact', __name__, url_prefix="/facts" )

@bp4.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
         print(request.form)
         return redirect('/facts')    
    return render_template('facts/index.html')