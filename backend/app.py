#!/usr/bin/env python3
import os, pathlib, logging
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
# from backend.utils.logger import setup_logging
# from backend.blueprints import register_blueprints

ROOT = pathlib.Path(__file__).parent.parent
app = Flask(__name__, template_folder=str(ROOT/"templates"), static_folder=str(ROOT/"static"))

app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "changeme")
CORS(app)
socketio = SocketIO(app, async_mode="eventlet", message_queue=os.environ.get("REDIS_URL"))

# setup_logging()
# register_blueprints(app)

@app.route("/")
def index():
    return "<h1>OpenXPlan v12.3 Backend is Running!</h1>"

if __name__ == "__main__":
    logging.info("Starting OpenXPlan v12.3 Secure Version...")
    socketio.run(app, host="0.0.0.0", port=5000, debug=False)
