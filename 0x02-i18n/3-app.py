#!/usr/bin/env python3
"""
Flask app with Babel for internationalization support.
Includes locale selection and template parametrization for translations.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


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


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages
    based on the request's Accept-Language headers.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the index page.
    Renders a simple HTML template with localized messages.
    """
    return render_template('3-index.html',
                           home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == "__main__":
    app.run()
