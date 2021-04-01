import pytest
import time

from flask import Flask


def test_no_timestamp(client):
    data = pytest.sig_challenge_fixture
    timestamp = int(time.time())
    signature = pytest.create_signature('SIGNING_SECRET', timestamp, data)

    res = client.post(
        '/',
        data=data,
        content_type='application/json',
        headers={
            'X-Slack-Signature': signature
        }
    )

    assert res.status_code == 403

def test_no_signature(client):
    data = pytest.sig_challenge_fixture
    timestamp = int(time.time())
    signature = pytest.create_signature('SIGNING_SECRET', timestamp, data)

    res = client.post(
        '/',
        data=data,
        content_type='application/json',
        headers={
            'X-Slack-Request-Timestamp': timestamp
        }
    )

    assert res.status_code == 403

def test_invalid_timestamp(client):
    data = pytest.sig_challenge_fixture
    timestamp = int(time.time())
    timestamp = timestamp - 60 * 5
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

    assert res.status_code == 403


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
