#!/usr/bin/python3
""" Starts a Flask Web Application """

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/afrilegal-api-documentation/', strict_slashes=False)
def documentation():
    """Render technical documentation page"""

    return render_template('doc.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5005)
