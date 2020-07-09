# application/frontend/__init__.py
from flask import Blueprint

frontend_blueprint = Blueprint('frontend', __name__)

from . import views
