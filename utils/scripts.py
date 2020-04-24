import os
from pydub import AudioSegment, exceptions
from werkzeug.datastructures import FileStorage
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import magic
import mimetypes
import audiofile
from pathlib import Path


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_local_file(file, filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    return file_path


def get_fmt(file_path):
    file_type = magic.from_file(file_path, mime=True)
    fmt = mimetypes.guess_extension(file_type)
    print(fmt)
    return fmt


def local_file_name(file_path):
    return Path(file_path).name


def get_converted_file(file_path, fmt):
    print(file_path)
    if fmt == '.mp3' or '.mp2':
        print('is mp')
        mp_file = change_type(file_path)
        return mp_file
    else:
        try:

            converted_file_name = local_file_name(file_path).split('.')[0]+'.mp3'
            new_file_path = os.path.join(UPLOAD_FOLDER, converted_file_name)
            mp3_audio = AudioSegment.from_file(file_path, fmt)
            mp3_audio.export(new_file_path, format="mp3")
            mp_file = change_type(new_file_path)

            return mp_file
        except exceptions.CouldntDecodeError:
            return False


def get_duration(file_path):
    time = audiofile.duration(file_path)
    return time


def change_type(file):
    local = open(file, 'rb')
    storage = FileStorage(local)
    return storage


def garbage_collection(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)
