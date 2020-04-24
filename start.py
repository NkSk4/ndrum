from client.connect import ConnectView, server
from route.upload_file import upload
from route.send_file import send
import config

up = ConnectView(upload)
sn = ConnectView(send)


if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT)
