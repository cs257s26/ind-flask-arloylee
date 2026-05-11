from flask import Flask
from ProductionCode.command_line import *
import csv

app = Flask(__name__)

data = []

@app.route('/')
def homepage():
    """Display homepage text."""
    return "Welcome to the homepage of water statistics!"

@app.route('/<string:location>/<string:year>/')
def getLocYear(location: str, year: int) -> str:
    """Get and display data from API for a specific location and year."""
    return str(getData(location, year))

@app.route('/search/loc/')
def getLocationHome() -> str:
    """Get and display data from API for a location."""
    return "Use form: /search/loc/YOUR LOCATION/"

@app.route('/search/loc/<string:location>/')
def getLocation(location: str) -> str:
    """Get and display data from API for a location."""
    return str(getData(location, None))

@app.route('/search/year/')
def getYearHome() -> str:
    """Get and display data from API for a year."""
    return "Use form: /search/loc/YOUR YEAR/"

@app.route('/search/year/<string:year>/')
def getYear(year: str) -> str:
    """Get and display data from API for a year."""
    return str(getData(None, year))

@app.errorhandler(404)
def page_not_found(e):
    """If a route is not found, display error."""
    return "ERROR 404: Page not found. Please try again. See README.md for details on syntax."

@app.errorhandler(500)
def python_bug(e):
    """If a python error occours, display error."""
    return "ERROR 500: Something went wrong in our Python code."

if __name__ == '__main__':
    loadData()
    app.run()
