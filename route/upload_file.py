from flask import request, jsonify, Blueprint
from werkzeug.utils import secure_filename
from bson import json_util
from server import mongo
import json, uuid
import config
import utils.scripts as src
from flask_cors import cross_origin

audio_db = mongo.db.Audio
upload = Blueprint('upload', __name__)


@upload.route('/upload', methods=['POST'])
@cross_origin()
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
        filename = secure_filename(file.filename)
        local_file = src.save_local_file(file, filename)
        file_fmt = src.get_fmt(local_file)
        mp_file = src.get_converted_file(local_file, file_fmt)

        if mp_file:

            file_id = hex(uuid.uuid1().time_low)
            duration = src.get_duration(local_file)
            data = {'original_file_name': filename,
                    'link': '%s%s' % (config.server, file_id),
                    'duration': '%.2f' % duration
                    }
            mongo.save_file(file_id, mp_file, content_type="audio/mpeg")
            resp = jsonify(data)
            json_str = json.loads(json_util.dumps(data))
            audio_db.insert_one(json_str)
            resp.status_code = 201
            src.garbage_collection(config.UPLOAD_FOLDER)
            return resp
        else:
            resp = jsonify({'message:': 'File is corrupted or format is not supported'})
            resp.status_code = 400
            return resp
    else:
        resp = jsonify({'message': 'Allowed file types are mp3, wav', })
        resp.status_code = 400
        return resp

