from flask import Flask, request
import json
import time
from utils import *

app = Flask(__name__)

version = "v1"


@app.route('/', methods=['GET'])
def default():
    return returner(200, 'ok', 'Written by Xu Xiao')

@app.route('/health', methods=['GET'])
def health():
    return returner(200, 'ok', 'good')


@app.route('/version', methods=['GET'])
def versions():
    return returner(200, 'ok', version)


if __name__ == '__main__':
    # docker build -f ./Dockerfile -t nsf-flask-trade .
    # docker run -itd -p 8000:8000 --name nsf-flask-trade nsf-flask-trade
    app.run(host="0.0.0.0", port=8000)

