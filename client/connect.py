from server import server

class ConnectView:
    def __init__(self, view):

        server.register_blueprint(view)

