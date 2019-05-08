import flask
from flask import Flask

app: Flask = flask.Flask(__name__)
print(__name__)

countries_population = {"India" : "1.3", "China" : "1.4", "USA" : "0.32", "Indonesia" : "0.26"}


@app.route('/population')
def return_population() :
    _country_name = flask.request.args.get('country')
    return countries_population.get(_country_name)


app.run(port=5000)
