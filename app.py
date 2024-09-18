from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import User,Recipe
from config import app






if __name__ == '__main__':
    app.run(debug=True)
