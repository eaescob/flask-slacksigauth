import json
import hashlib
import hmac
import pytest

from flask import Flask, make_response
from flask_slacksigauth import slack_sig_auth


def create_signature(secret, timestamp, data):
    req = str.encode('v0:' + str(timestamp) + ':') + str.encode(data)
    request_signature = 'v0='+hmac.new(
        str.encode(secret),
        req, hashlib.sha256
    ).hexdigest()
    return request_signature


def load_challenge_fixture(event, as_string=True):
    filename = "tests/data/{}.json".format(event)

    with open(filename) as json_data:
        event_data = json.load(json_data)
        if not as_string:
            return event_data
        else:
            return json.dumps(event_data)


def sig_challenge_fixture_plugin():
    return load_challenge_fixture('signature_challenge')

def create_signature_plugin():
    return create_signature

def pytest_configure():
    pytest.create_signature = create_signature_plugin()
    pytest.sig_challenge_fixture = sig_challenge_fixture_plugin()


@pytest.fixture
def app():
    flask_app = Flask(__name__)
    flask_app.testing = True
    flask_app.config['SLACK_SIGNING_SECRET'] = 'SIGNING_SECRET'
    @flask_app.route('/', methods=['POST', 'GET'])
    @slack_sig_auth
    def index():
        return make_response("OK", 200)

    app = flask_app
    return app
