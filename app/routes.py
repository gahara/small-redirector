from flask import  redirect, request
from flask_cors import CORS
from app import app

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
cors = CORS(app)

@app.route('/', defaults={'path': ''}, methods=HTTP_METHODS)
@app.route('/<path:path>', methods=HTTP_METHODS)
def catch_all(path):
    return redirect(f'http://google.com{request.full_path}', code=302)
