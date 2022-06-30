from flask import Flask
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:John1412%@localhost:5432/petfax'
    app.config['SQLALCEMY_TRACK_MODIFICATIONS'] = False

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello():
        return 'Hello, Petfax!'
    
    from . import pet
    app.register_blueprint(pet.bp)

    from . import show
    app.register_blueprint(show.bp2)

    from . import create
    app.register_blueprint(create.bp3)

    from . import fact
    app.register_blueprint(fact.bp4)
    
    return app