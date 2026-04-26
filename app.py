from flask import Flask
from ProductionCode.command_line import *
import csv

app = Flask(__name__)
PORT = 5100

data = []

@app.route('/')
def homepage():
    return "Welcome to the homepage of water statistics!"

@app.route('/<string:location>/<string:year>/')
def getCell(location: str, year: int) -> str:
    return str(getData(location, year))

@app.route('/search/loc/<string:location>/')
def getColHeader(location: str) -> str:
    return str(getData(location, None))

@app.route('/search/year/<string:year>/')
def getCol(year: str) -> str:
    return str(getData(None, year))

@app.errorhandler(404)
def page_not_found(e):
    return "ERROR 404: Page not found. Please try again. See README.md for details on syntax."

@app.errorhandler(500)
def python_bug(e):
    return "ERROR 500: Something went wrong in our Python code."

if __name__ == '__main__':
    loadData()
    app.run(port=PORT)
