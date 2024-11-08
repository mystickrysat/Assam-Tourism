from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/towns-and-cities')
def towns_and_cities():

    locations_file = 'locations-list.csv'
    with open(locations_file, 'r') as places:
        places = csv.reader(places)
        locations = [place[0] for place in places]

    return render_template('towns-and-cities.html', locations=locations)


if __name__ == '__main__':
    app.run(debug=True)
