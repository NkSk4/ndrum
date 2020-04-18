from flask import Flask
import config as cfg
from flask_pymongo import PyMongo

server = Flask(__name__, instance_relative_config=True)
server.debug = cfg.DEBUG
server.config['MAX_CONTENT_LENGTH'] = cfg.MAX_CONTENT_LENGTH
server.config['MONGO_URI'] = cfg.MONGO_URI
server.config['MAX_CONTENT_LENGTH'] = cfg.MAX_CONTENT_LENGTH
mongo = PyMongo(server)




