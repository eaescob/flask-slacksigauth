import pytest
import time

from flask import Flask


def test_slack_sigauth(client):
    data = pytest.sig_challenge_fixture
    timestamp = int(time.time())
    signature = pytest.create_signature('SIGNING_SECRET', timestamp, data)

    res = client.post(
        '/',
        data=data,
        content_type='application/json',
        headers={
            'X-Slack-Request-Timestamp': timestamp,
            'X-Slack-Signature': signature
        }
    )

    assert res.status_code == 200

def test_bad_sigauth(client):
    data = pytest.sig_challenge_fixture
    timestamp = int(time.time())
    signature = pytest.create_signature('BAD_SECRET', timestamp, data)

    res = client.post(
        '/',
        data=data,
        content_type='application/json',
        headers={
            'X-Slack-Request-Timestamp': timestamp,
            'X-Slack-Signature': signature
        }
    )

    assert res.status_code == 403
