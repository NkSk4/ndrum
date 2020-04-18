from flask import Blueprint
from server import mongo
send = Blueprint('send', __name__)


@send.route('/<filename>', methods=['GET'])
def download_file(filename):
    return mongo.send_file(filename)
