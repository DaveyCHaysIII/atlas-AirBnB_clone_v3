#!/usr/bin/python3
"""This is our flask instance"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    """teardown function"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
