from flask import current_app
from . import index_blu


@index_blu.route('/')
def index():
    return 'index'


@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('../../../favicon.ico')