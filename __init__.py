from flask import Flask
from flask_talisman import Talisman

def create_app():
    app = Flask(__name__)

    csp = {
        'default-src': [
            '\'self\''
        ]
    }

    Talisman(
        app,
        content_security_policy=csp
    )

    return app
