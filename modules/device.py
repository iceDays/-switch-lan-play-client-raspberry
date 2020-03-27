from flask import Blueprint
from utils import make_success


device = Blueprint('BlueprintDevice', __name__)


@device.route('/device/hello')
def hello_world():
    return make_success()
