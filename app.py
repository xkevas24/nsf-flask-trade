from flask import Flask, request
import json
import time
import socket
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


@app.route('/serviceIp', methods=['GET'])
def serviceIp():
    cookies = request.cookies.get('nsfLB')
    header = request.headers.get('nsfLB')
    return returner(200, 'ok', {
        'a-response-url': socket.gethostbyname(socket.getfqdn(socket.gethostname())),
        'nsfLB-Cookie': cookies,
        'nsfLB-Header': header,
        'z-all': {
            'headers': str(request.headers),
            'cookies': str(request.cookies)
        }

    })


if __name__ == '__main__':
    # docker build -f ./Dockerfile -t nsf-flask-trade .
    # docker run -itd -p 8000:8000 --name nsf-flask-trade nsf-flask-trade
    # docker tag nsf-flask-trade:latest harbor.cloud.netease.com/qztest/nsf-flask-trade:latest
    # docker push harbor.cloud.netease.com/qztest/nsf-flask-trade:latest
    # docker save -o nsf-flask-trade.tar nsf-flask-trade
    app.run(host="0.0.0.0", port=8000)
    # local
    # docker login -u AlanHsu24 -p xxhandsome24
    # docker tag nsf-flask-trade:latest alanhsu24/nsf-flask-trade:latest
    # docker load --input /root/nsf-flask-trade.tar
    # kubectl create deployment nsf-flask-trade --image=alanhsu24/nsf-flask-trade:latest
    # kubectl scale --replicas=4 deploy nsf-flask-trade
    # kubectl get deployments -o wide // kubectl get deployment   -A
    # kubectl get pod --show-labels  -A
    # kubectl expose deployment nsf-flask-trade --port=8000 --target-port=8000 --type=NodePort
    # kubectl expose deployment nsf-flask-trade --port=8000 --target-port=8000 --external-ip="172.30.87.65" --type=NodePort
    # kubectl describe pod
    # 滚动更新
    # kubectl set image deployment/nsf-flask-trade nsf-flask-trade=alanhsu24/nsf-flask-trade:latest
    # kubectl set image deployment/nsf-flask-trade nsf-flask-trade=nsf-flask-trade

