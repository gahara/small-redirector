import os
import requests
from flask import request, Response
from dotenv import load_dotenv
from app import app

load_dotenv()
HOST = os.environ.get('HOST')

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']

@app.route('/', defaults={'path': ''}, methods=HTTP_METHODS)
@app.route('/<path:path>', methods=HTTP_METHODS)
def catch_all(path):
    resp = requests.request(
        method=request.method,
        url=request.url.replace(request.host_url, HOST),
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    headers = [(name, value) for (name, value) in resp.raw.headers.items()]

    response = _corsify_actual_response(Response(resp.content, resp.status_code, headers=headers))

    return response

def _build_cors_prelight_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response