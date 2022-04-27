from flask import Flask
from .config import Devconfig

#initialize application
app = Flask(__name__)

# setting up configuration
app.config.from_object(Devconfig)

from app import views