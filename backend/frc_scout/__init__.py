import os
from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from .datastore import Team
from .datastore import HomeTeam
from .datastore import Events
from .datastore import CurrentEvent
from .datastore import FutureEvents
from .datastore import EventMatches
from .datastore import TeamMatchReport
from .datastore import ReportConfiguration
from .datastore import Match
from .datastore import Event
from .datastore import EventMatch


from flask import request
from flask_restful import Resource


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # TODO: Review this temporary solution to get local Angular App to work
    CORS(app, origin="localhost")

    api = Api(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('application.cfg', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    if "MOCK_BLUE_ALLIANCE_API" in app.config and app.config["MOCK_BLUE_ALLIANCE_API"]:
        print("Creating mock alliance")
        from mock_blue_alliance import MockBlueAlliance
        app.config["BLUE_ALLIANCE_API"] = MockBlueAlliance()
    else:
        from real_blue_alliance import RealBlueAlliance
        app.config["BLUE_ALLIANCE_API"] = RealBlueAlliance(app.config["AUTH_KEY"])

    if "MOCK_CLOCK" in app.config:
        print("Creating mock clock")
        from clock import MockClock
        app.config["CLOCK"] = MockClock(app.config["MOCK_CLOCK"])
    else:
        print("Real Clock")
        from clock import RealClock
        app.config["CLOCK"] = RealClock()

    # Add resources
    api.add_resource(HomeTeam, '/home')
    api.add_resource(Team, '/team/<key>')
    api.add_resource(Events, '/events')
    api.add_resource(Event, '/event/<key>')
    api.add_resource(CurrentEvent, '/events/current')
    api.add_resource(FutureEvents, '/events/future')

    api.add_resource(EventMatches, '/event/<key>/matches')
    api.add_resource(EventMatch, '/event/<string:event>/match/<int:match>')
    api.add_resource(Match, '/match/<key>')
    api.add_resource(TeamMatchReport, '/match/<string:match>/team/<string:team>')
    api.add_resource(ReportConfiguration, '/event/<event>/config')
    return app
