#!/usr/bin/env python

import os
import json
import logging
import datetime
from logging.handlers import RotatingFileHandler
from flask import Flask, jsonify, request, send_file

application = Flask(__name__, static_folder='./', static_url_path='')

if not os.path.isdir('./log'):
    os.mkdir('./log')

logger = logging.getLogger(__name__)
consoleHandler = logging.StreamHandler()
fileHandler = RotatingFileHandler(os.path.join('./log', "my-application-{}.log".format(datetime.datetime.today().isoformat())), maxBytes=10*1024*1024)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
consoleHandler.setFormatter(formatter)
consoleHandler.setLevel(logging.WARNING)
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)


"""
@application.route("/api/data", methods=["POST"])
def method():
    try:
        if true:
            return jsonify({"result": "yes"})
        else:
            raise ValueError("no")
    except Exception as err:
        logger.error(err)
        return jsonify({"error": err}), 400
"""

@application.route("/", methods=["GET"])
def root():
    return application.send_static_file('index.html')

# Run application
if __name__ == "__main__":
	application.run()
