from flask import request, jsonify, Blueprint
from werkzeug.utils import secure_filename
from bson import json_util
from server import mongo
import json, uuid
import config
import utils.scripts as src
audio_db = mongo.db.Audio
upload = Blueprint('upload', __name__)


@upload.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']

    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and src.allowed_file(file.filename):
        file = src.converter(file, file.filename)
        filename = secure_filename(file.filename)
        filename = filename.split('_')[-1]
        file_id = (hex(uuid.uuid1().time_low))

        data = {'file_name': filename,
                'link': '%s%s' % (config.server, file_id),
                'duration': '%.2f' % src.time

                }
        mongo.save_file(file_id, file, content_type="audio/mpeg")
        resp = jsonify(data)
        json_str = json.loads(json_util.dumps(data))
        audio_db.insert_one(json_str)
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message': 'Allowed file types are mp3, wav', })
        resp.status_code = 400
        return resp

