import os
from dotenv import load_dotenv


load_dotenv(os.path.join('.env'))

MONGO_URI = os.getenv('MONGO_URI')
DEBUG = True
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['mp3', 'wav', 'ogg', 'mp4', 'aac', 'wma', 'flac'])
server = f'http://{HOST}:{PORT}/'
