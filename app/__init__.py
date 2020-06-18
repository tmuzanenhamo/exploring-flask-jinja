# Create a package
from flask import Flask

app = Flask(__name__)

# create different views
from app import views
from app import adminviews