import hashlib
import hmac

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
