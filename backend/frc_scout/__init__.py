import os
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from .datastore import Team
from .datastore import HomeTeam
from .datastore import Events
from .datastore import CurrentEvent
from .datastore import FutureEvents


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    api = Api(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        HOME_TEAM='frc5829'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from mock_blue_alliance import MockBlueAlliance
    app.config["BLUE_ALLIANCE_API"] = MockBlueAlliance()

    # Add resources
    api.add_resource(HomeTeam, '/home')
    api.add_resource(Team, '/team/<key>')
    api.add_resource(Events, '/events')
    api.add_resource(CurrentEvent, '/events/current')
    api.add_resource(FutureEvents, '/events/future')

    return app
