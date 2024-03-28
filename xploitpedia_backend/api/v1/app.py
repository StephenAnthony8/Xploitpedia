#!/usr/bin/python3
""" Flask Xiopedia api setup """
from api.v1.views import xiopedia_views
from flask import Flask, jsonify,\
    make_response, render_template
from flask_cors import CORS
from os import getenv

app = Flask(__name__)
app.register_blueprint(xiopedia_views) # to be configured
cors = CORS(app, resources={r"/api/v1/*": {'origins': '*'}})

# error_handling
@app.errorhandler(404)
def err_404(error):
    """ Raises an error 404 """
    error_response = make_response(
        jsonify(
            {'error': 'Requested resource not found'},
            404)
    )
    return (error_response)

# db_closing(to allow for new entries)
# @app.teardown_appcontext

if __name__ == '__main__':
    host = getenv('XIOPEDIA_API_HOST', '0.0.0.0')
    port = getenv('XIOPEDIA_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)