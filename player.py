import pygame
import time

class Players:
    def __init__(self, pygame):
        self.x = []
        self.y = []
        self.life = []
        self.weapon = []
        self.index = []
        self.client_index = None
        self.SHIP = pygame.image.load('ship.png')
        self.SHIP2 = pygame.image.load('ship_2.png')
        self.last_bullet_time = 0

    def register_player(self, client, port):
        request = "POST /register_player= HTTP/1.1\r\nHost:%s\r\n\r\n" % port
        client.send(request.encode())
        response = client.recv(1212)
        http_response = response.decode("utf-8").replace("\r", "")
        listed_response = http_response.split("\n")
        try:
            self.client_index = int(listed_response[5])
        except:
            print(listed_response)
            exit(-1)



    def get_players_update(self, list_):
        self.x = list(map(int, list_[0].split()))
        self.y = list(map(int, list_[1].split()))
        self.life = list(map(int, list_[2].split()))
        self.weapon = list(map(int, list_[3].split()))
        self.index = list(map(int, list_[4].split()))

    def bullet_create(self, client, port):
        if int(round(time.time() * 1000)) - self.last_bullet_time > 120:
            request = "POST /player_bullet_create={} HTTP/1.1\r\nHost:%s\r\n\r\n".format(self.client_index) % port
            client.send(request.encode())
            self.last_bullet_time = int(round(time.time() * 1000))

    def move(self, dir, client, port):
        request = "POST /player_move={}{} HTTP/1.1\r\nHost:%s\r\n\r\n".format(self.client_index, dir) % port
        client.send(request.encode())

    def draw(self, screen):
        for i in self.index:
            if self.life[i] == 2:
                screen.blit(self.SHIP, (self.x[i], self.y[i]))
                pygame.display.flip()
            if self.life[i] == 1:
                screen.blit(self.SHIP2, (self.x[i], self.y[i]))
