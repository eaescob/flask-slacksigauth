import hashlib
import hmac
import os


from functools import wraps
from flask import request, make_response
from flask import current_app
from time import time


def verify_signature(request, timestamp, signature, signing_secret):
    # Verify the request signature of the request sent from Slack
    # Generate a new hash using the app's signing secret and request data

    # Compare the generated hash and incoming request signature
    # Python 2.7.6 doesn't support compare_digest
    # It's recommended to use Python 2.7.7+
    # noqa See https://docs.python.org/2/whatsnew/2.7.html#pep-466-network-security-enhancements-for-python-2-7

    if timestamp is None or signature is None:
        return False

    if abs(time() - int(timestamp)) > 60 * 5:
        return False

    req = str.encode('v0:' + str(timestamp) + ':') + request.get_data()
    request_hash = 'v0=' + hmac.new(
        str.encode(signing_secret),
        req, hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(request_hash, signature)


def slack_sig_auth(f):
    @wraps(f)
    def validate_slack_signature(*args, **kwargs):
        slack_signing_secret = current_app.config['SLACK_SIGNING_SECRET']

        if slack_signing_secret is None:
            slack_signing_secret = os.environ['SLACK_SIGNING_SECRET']

        if slack_signing_secret is None:
            raise AttributeError('No slack signing secret configured, please see README.')

        req_timestamp = request.headers.get('X-Slack-Request-Timestamp')
        req_signature = request.headers.get('X-Slack-Signature')

        if not verify_signature(request, req_timestamp, req_signature, slack_signing_secret):
            return make_response("Unauthorized", 403)
        return f(*args, **kwargs)
    return validate_slack_signature
