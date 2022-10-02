from flask import Blueprint

stories = Blueprint('stories', __name__, url_prefix='/stories')

from . import views