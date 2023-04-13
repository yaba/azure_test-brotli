from flask import Flask, jsonify
from flask_compress import Compress

app = Flask(__name__)
# Set the alogirthm to apply gzip - https://github.com/colour-science/flask-compress#options
app.config['COMPRESS_ALGORITHM'] = 'br'
Compress(app)


@app.route("/")
def index():
    msg = 'gzip-stack-examples-python-gzip'
    return jsonify({ 'message': msg * 30 })
