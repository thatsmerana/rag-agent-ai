from flask import Flask
from config import Config
from src.auth.auth import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        init_db(app)
        print("Database initialized successfully!") 