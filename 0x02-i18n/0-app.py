#!/usr/bin/env python3
"""
Basic Flask app for displaying a welcome message.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route for the index page.
    Renders a simple HTML template with a welcome message.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
