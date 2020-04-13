from functools import wraps
from flask import request, make_response
from flask import current_app

from .utils.sigcheck import verify_signature


def slack_sig_auth(f):
    @wraps(f)
    def validate_slack_signature(*args, **kwargs):
        slack_signing_secret = current_app.config['SLACK_SIGNING_SECRET']
        req_timestamp = request.headers.get('X-Slack-Request-Timestamp')
        req_signature = request.headers.get('X-Slack-Signature')

        if not verify_signature(request, req_timestamp, req_signature, slack_signing_secret):
            return make_response("Unauthorized", 403)
        return f(*args, **kwargs)
    return validate_slack_signature
