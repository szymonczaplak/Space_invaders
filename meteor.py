class Meteors:
    def __init__(self, pygame):
        self.x = []
        self.y = []
        self.size = []
        self.METEORYT1 = pygame.image.load('meteoryt1.png')
        self.METEORYT2 = pygame.image.load('big_met.png')

    def get_meteors_update(self, client, port):
        request = "POST /update_meteors=? HTTP/1.1\r\nHost:%s\r\n\r\n" % port
        client.send(request.encode())
        response = client.recv(port)
        http_response = response.decode("utf-8").replace("\r", "")
        listed_response = http_response.split("\n")
        self.x = list(map(int, listed_response[5].split()))
        self.y = list(map(int, listed_response[6].split()))
        self.size = list(map(int, listed_response[7].split()))

    def draw(self, screen):
        for i in range(len(self.x)):
            if self.size[i] == "snall":
                screen.blit(self.METEORYT1, (self.x[i], self.y[i]))
            else:
                screen.blit(self.METEORYT2, (self.x[i], self.y[i]))