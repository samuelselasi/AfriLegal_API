#!/usr/bin/python3
""" Starts a Flask Web Application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/afrilegal-api/', strict_slashes=False)
def afrilegal():
    """ Render AfriLegal API Landing page """

    return render_template('index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5003)
