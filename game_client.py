import socket
import pygame
import time
import random
from player import Players
from bullet import Bullets
from meteor import Meteors
from enemy import Enemies
from game import Game
from bonus import Bonus


# Szymon Czaplak


def update(client, port, p, e):
    request = "POST /update_status=? HTTP/1.1\r\nHost:%s\r\n\r\n" % port
    client.send(request.encode())
    response = client.recv(1212)
    http_response = response.decode("utf-8").replace("\r", "")
    listed_response = http_response.split("\n")
    try:
        if listed_response[5] != "OK":
            print(listed_response)
            update(client, port, p, e)
            return
    except:
        update(client, port, p, e)
        return
    p.get_players_update(listed_response[6:11])
    e.get_enemies_update(listed_response[11:15])
    b.get_bullet_update(listed_response[15:18])
    print(listed_response)


def instrukcja():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    screen.fill((0, 0, 0))
    screen.blit(INSTRUKCJA, (0, 0))
    pygame.display.flip()
    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if (pressed[pygame.K_SPACE]):
                return


def Menu():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    menu_position = 1
    screen.fill((0, 0, 0))
    instructions = small_font.render("Sterowanie po menu strzalkami, a wybor spacja", 1, (14, 24, 51))
    txt = myfont.render("Space Invanders", 1, (0, 225, 225))
    play = myfont.render("Play", 1, (0, 225, 225))
    instr = myfont.render("Instrukcja", 1, (0, 225, 225))
    ext = myfont.render("Exit", 1, (0, 225, 225))
    screen.blit(txt, (50, 50))
    pygame.display.flip()
    while True:
        screen.fill((0, 0, 0))
        screen.blit(txt, (50, 50))
        screen.blit(instructions, (10, 270))

        nacisk = pygame.key.get_pressed()

        if (menu_position == 1):
            play2 = myfont.render("Play", 1, (178, 34, 34))
            screen.blit(play2, (50, 100))
            screen.blit(ext, (50, 200))
            screen.blit(instr, (50, 150))
        if (menu_position == 2):
            instr2 = myfont.render("Instrukcja", 1, (178, 34, 34))
            screen.blit(instr2, (50, 150))
            screen.blit(ext, (50, 200))
            screen.blit(play, (50, 100))
        if (menu_position == 3):
            ext2 = myfont.render("Exit", 1, (178, 34, 34))
            screen.blit(ext2, (50, 200))
            screen.blit(play, (50, 100))
            screen.blit(instr, (50, 150))
        for event in pygame.event.get():
            if nacisk[pygame.K_UP]:
                if (menu_position != 1):
                    menu_position -= 1

            if (nacisk[pygame.K_DOWN]):
                if (menu_position != 3):
                    menu_position += 1
            if nacisk[pygame.K_SPACE]:
                return menu_position
        pygame.display.flip()
        clock.tick(60)


pygame.init()
random.seed()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 300))

target_host = "localhost"

target_port = 1212  # create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

INSTRUKCJA = pygame.image.load('Instrukcje.png')
TEXT = pygame.image.load('txt.png')

pygame.font.init()
myfont = pygame.font.SysFont('monospace', 25)
small_font = pygame.font.SysFont('monospace', 15)

while (1):
    done = False
    p = Players(pygame)
    b = Bullets()
    m = Meteors(pygame)
    e = Enemies(pygame)
    bo = Bonus(pygame)
    g = Game()

    while (1):
        menu_ret = Menu()
        if menu_ret == 1:
            break
        elif menu_ret == 2:
            instrukcja()
        elif menu_ret == 3:
            exit()

    screen.fill((0, 0, 0))

    game_start_time = time.time()

    time_txt = None
    score_txt = None
    p.register_player(client, target_port)
    screen.fill((0, 0, 0))

    #g.play(client, target_port)
    while not done:
        screen.fill((0, 0, 0))
        print("imhere")
        #p.get_players_update(client, target_port)
        update(client, target_port, p, e)
       # m.get_meteors_update(client, target_port)
       # bo.get_bonuses_update(client, target_port)
        #e.get_enemies_update(client, target_port)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            p.bullet_create(client, target_port)

        b.draw(pygame, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        #done = g.check_if_done(client, target_port)


        if pressed[pygame.K_UP]:
            p.move("up", client, target_port)
        if pressed[pygame.K_DOWN]:
            p.move("down", client, target_port)
        if pressed[pygame.K_LEFT]:
            p.move("left", client, target_port)
        if pressed[pygame.K_RIGHT]:
            p.move("right", client, target_port)

        p.draw(screen)
        e.draw(screen)
        pygame.display.update()

        #m.draw(screen)
        #bo.draw(screen)

        #score_txt = small_font.render("Score: " + g.get_score(client, target_port))
        #screen.blit(score_txt, (0, 0))
        #
        #screen.blit(time_txt, (198, 0))

        pygame.display.flip()
        clock.tick(120)

    time_txt = small_font.render("time: " + str(time.time() - game_start_time), 20, (12, 225, 225))
    g.stop(client, target_port)
    screen.fill((0, 0, 0))
    pygame.font.init()
    myfont = pygame.font.SysFont('monospace', 30)
    textsurface = myfont.render('GAME OVER' + g.get_score(client, target_port), 1, (12, 0, 225))
    screen.blit(textsurface, (90, 125))
    screen.blit(time_txt, (198, 0))
    screen.blit(score_txt, (0, 0))
    pygame.display.flip()
    time.sleep(4)
