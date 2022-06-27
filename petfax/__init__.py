from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, Petfax!'
    
    from . import pet
    app.register_blueprint(pet.bp)

    from . import show
    app.register_blueprint(show.display)

    from . import create
    app.register_blueprint(create.form)
    
    return app