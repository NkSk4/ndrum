import os
from pydub import AudioSegment
from werkzeug.datastructures import FileStorage
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS

import audiofile

time = ''
def converter(file, filename):
    fmt = filename.rsplit('.', 1)[1].lower()
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    global time
    time = audiofile.duration(file_path)
    if fmt == 'mp3':
        return file
    else:
        converted = filename.split('.')[0]+'.mp3'
        new_file = os.path.join(UPLOAD_FOLDER, converted)
        audio = AudioSegment.from_file(file_path, fmt)
        audio.export(new_file, format="mp3")

        file = open(new_file, 'rb')
        file = FileStorage(file)
        os.remove(file_path), os.remove(new_file)

        return file


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
