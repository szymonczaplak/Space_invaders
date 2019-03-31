class Game:
    def __init__(self):
        self.state = None
        self.score = None

    def play(self, client, port):
        self.state = "play"
        request = "game=play\n" % port
        client.send(request.encode())

    def stop(self, client, port):
        self.state = "stop"
        request = "STOP=?\n"
        client.send(request.encode())

    def check_if_done(self, client, port):
        request = "POST /game_check_if_done=? HTTP/1.1\r\nHost:%s\r\n\r\n" % port
        client.send(request.encode())
        response = client.recv(port)
        http_response = response.decode("utf-8").replace("\r", "")
        listed_response = http_response.split("\n")
        if listed_response[5] == "yes":
            return True
        return False

    def get_score(self, client, port):
        request = "POST /get_score=? HTTP/1.1\r\nHost:%s\r\n\r\n" % port
        client.send(request.encode())
        response = client.recv(port)
        http_response = response.decode("utf-8").replace("\r", "")
        listed_response = http_response.split("\n")
        return listed_response[5]
