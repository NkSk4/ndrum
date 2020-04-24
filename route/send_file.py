from flask import Blueprint
from server import mongo
from flask_cors import cross_origin
send = Blueprint('send', __name__)


@send.route('/<filename>', methods=['GET'])
@cross_origin()
def download_file(filename):
    return mongo.send_file(filename)



