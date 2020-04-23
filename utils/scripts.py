import os
from pydub import AudioSegment, exceptions
from werkzeug.datastructures import FileStorage
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import magic
import mimetypes
import audiofile
time = ''


def converter(file, filename):

    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    file_type = magic.from_file(file_path, mime=True)
    fmt = mimetypes.guess_extension(file_type)
    print(fmt)
    global time
    time = audiofile.duration(file_path)
    print(time)
    if fmt == 'mp3' or 'mp2':

        file = change_type(file_path)
        os.remove(file_path)
        return file
    else:
        try:
            converted = filename.split('.')[0]+'.mp3'
            new_file = os.path.join(UPLOAD_FOLDER, converted)
            audio = AudioSegment.from_file(file_path, fmt)
            audio.export(new_file, format="mp3")
            file = change_type(new_file)
            os.remove(file_path), os.remove(new_file)

            return file
        except exceptions.CouldntDecodeError:
            return False


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def change_type(file):
    local = open(file, 'rb')
    storage = FileStorage(local)
    return storage

