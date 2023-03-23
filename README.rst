Slack Signature Authentication for Flask
========================================
.. image:: https://github.com/eaescob/flask-slacksigauth/actions/workflows/build.yml/badge.svg
    :target: https://github.com/eaescob/flask-slacksigauth/actions/workflows/build.yml
.. image:: https://codecov.io/gh/eaescob/flask-slacksigauth/branch/master/graph/badge.svg?token=WPOI4PT5ZU 
    :target: https://codecov.io/gh/eaescob/flask-slacksigauth
.. image:: https://badge.fury.io/py/flask-slacksigauth.png
    :target: https://badge.fury.io/py/flask-slacksigauth

The Slack Signature Authentication module is a Python-based solution for Flask applications
to be able to authenticate POST requests coming in from Slack. The module returns HTTP code
403 for those requests that fail Slack's signature validation. The module adds a decorator
that can be used for Flask routes.

Integrity
---------
Added `SLSA`_ provenance checks to every release starting with v1.0.9

.. _SLSA: https://slsa.dev

You will need to install `slsa-verifier`_ first

.. _slsa-verifier: https://github.com/slsa-framework/slsa-verifier

Provenance verification
^^^^^^^^^^^^^^^^^^^^^^^
.. code:: shell

 python -m pip download --only-binary=:all: flask-slacksigauth #Downloads flask_slacksigauth-1.0.9-py3-none-any.whl
 curl --location -O https://github.com/eaescob/flask-slacksigauth/releases/download/v1.0.9/multiple.intoto.jsonl
 slsa-verifier verify-artifact                             \
   --provenance-path multiple.intoto.jsonl                 \
   --source-uri github.com/eaescob/flask-slacksigauth      \
   flask_slacksigauth-1.0.9-py3-none-any.whl

Check for - PASSED: Verified SLSA Provenance

After successful verification, package is safe to be installed.
   
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
