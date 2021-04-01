Slack Signature Authentication for Flask
========================================
.. image:: https://travis-ci.org/eaescob/flask-slacksigauth.svg?branch=master
    :target: https://travis-ci.org/eaescob/flask-slacksigauth
.. image:: https://codecov.io/gh/eaescob/flask-slacksigauth/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/eaescob/flask-slacksigauth
.. image:: https://badge.fury.io/py/flask-slacksigauth.svg
    :target: https://badge.fury.io/py/flask-slacksigauth

The Slack Signature Authentication module is a Python-based solution for Flask applications
to be able to authenticate POST requests coming in from Slack. The module returns HTTP code
403 for those requests that fail Slack's signature validation. The module adds a decorator
that can be used for Flask routes.

Installation
------------
.. code:: shell

  pip install flask-slacksigauth

App Setup
------------
After declaring your Flask API endpoints, you can decorate them to for authentication checks:

.. code:: python

  @app.route('/api', methods=['POST', 'GET'])
  @slack_sig_auth
  def api():
    return jsonify(message='OK'), 200

**This will force slack signature authentication for you '/api' endoint.**
