from flask import  redirect

from app import app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return redirect(f'http://google.com/{path}', code=302)
