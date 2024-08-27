#!/usr/bin/env python3
"""
Flask app with Babel for internationalization support.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask application.
    Sets up languages, default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

# Instantiate Babel object
babel = Babel(app)


@app.route('/')
def index():
    """
    Route for the index page.
    Renders a simple HTML template with a welcome message.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
