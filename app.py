from flask import Flask, request, send_file
import os
from io import BytesIO

import convert

def create_app():
    app = Flask(__name__)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/propaganda')
    def propaganda():
        if request.args.get("phrase") is None:
            return "missing phrase param", 400

        bio = BytesIO()
        img = convert.save_meme(request.args.get("phrase"), bio)
        return send_file(img, mimetype='image/jpeg')

    return app
