import socket
from player import Players
import time
import pygame

target_host = "localhost"

target_port = 1212  # create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))
# send some data
p = Players(pygame)
p.register_player(client, target_port)


while(1):
    print("a\n")
    p.get_players_update(client, target_port)
    print(p.x[p.client_index], p.y, p.client_index)
    time.sleep(1)
    p.move("up", client, target_port)

print(listed_response[5:])
