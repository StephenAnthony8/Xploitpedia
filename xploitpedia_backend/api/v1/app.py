#!/usr/bin/python3
""" Flask xiopedia api setup """
from api.v1.views import app_views
from flask import Flask, jsonify,\
    make_response  #, render_template
from flask_cors import CORS
from os import getenv
from models import storage

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.url_map.strict_slashes = False
app.register_blueprint(app_views) # to be configured
cors = CORS(app, resources={r"/api/v1/*": {'origins': '*'}})

# error_handling
@app.errorhandler(404)
def err_404(error):
    """ Raises an error 404 """
    error_response = make_response(
        jsonify(
            {'error': 'Requested resource not found'}),
            404
    )
    return (error_response)

# db_closing(to allow for new entries)
@app.teardown_appcontext
def close_db(error):
    """ closes the database instance """
    storage.close()


if __name__ == '__main__':
    host = getenv('XIOPEDIA_API_HOST', '0.0.0.0')
    port = getenv('XIOPEDIA_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True, debug=True)