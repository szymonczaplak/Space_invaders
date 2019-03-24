class Bonus:
    def __init__(self, pygame):
        self.x = []
        self.y = []
        self.BONUS = pygame.image.load('bonus.png')

    def get_bonuses_update(self, client, port):
        request = "POST /bonus_update=? HTTP/1.1\r\nHost:%s\r\n\r\n" % port
        client.send(request.encode())
        response = client.recv(1212)
        http_response = response.decode("utf-8").replace("\r", "")
        listed_response = http_response.split("\n")
        self.x = list(map(int, listed_response[5].split()))
        self.y = list(map(int, listed_response[6].split()))

    def draw(self, screen):
        for i in range(self.x):
            screen.blit(self.BONUS, (self.x[0], self.y[0]))
