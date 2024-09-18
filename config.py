from dotenv import load_dotenv
load_dotenv()

import os
import random

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import MetaData
from flask_restful import Api,Resource



app = Flask(__name__)

# Configure your SQLAlchemy database URI here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipe_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)