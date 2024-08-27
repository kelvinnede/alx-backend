#!/usr/bin/env python3
"""
Flask app with Babel for internationalization support.
Includes a mock user login system using URL parameters.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """
    Retrieve a user by ID from the URL parameter 'login_as'.
    Returns None if the user ID is not found.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """
    Function that runs before each request.
    Sets the global user variable if a user is logged in.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages.
    If 'locale' is in the request arguments
    and is a supported locale, use it.
    Otherwise, use the request's Accept-Language headers.
    """
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the index page.
    Renders a simple HTML template with localized messages.
    """
    if g.user:
        welcome_msg = _("logged_in_as", username=g.user["name"])
    else:
        welcome_msg = _("not_logged_in")
    return render_template('5-index.html', welcome_msg=welcome_msg)


if __name__ == "__main__":
    app.run()
