from flask import Flask
from flask_cors import CORS
import os
from .routes.person_routes import person_bp
from .db import db, migrate
from .models.person import Person
# Import models, blueprints, and anything else needed to set up the app or database


def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    if config:
        app.config.update(config)
    # Initialize app with SQLAlchemy db and Migrate
    db.init_app(app)
    migrate.init_app(app, db)
    # Register Blueprints 
    app.register_blueprint(person_bp)

    CORS(app)
    return app
