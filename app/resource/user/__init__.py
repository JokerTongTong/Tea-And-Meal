from flask import Blueprint

index_blu = Blueprint("/", __name__)
# user_blu = Blueprint("user", __name__, url_prefix="/user")

from . import views