import pygame
import time
import random

#Szymon Czaplak

def bullet_create(n,x,y):
    if n == 1:
        bullet_position_y.append(y)
        bullet_position_x.append(x)
    if n >= 2:
        bullet_position_y.append(y)
        bullet_position_x.append(x)
        bullet_position_y.append(y)
        bullet_position_x.append(x+9)
    if n >= 3:
        for i in range(0,10, 3):
            bullet_position_y.append(y)
            bullet_position_x.append(x+i)

def bullet_update():
    for i in range(1,len(bullet_position_y)):
        bullet_position_y[i]-=5
    for i in range(len(bullet_position_y)):
        if(bullet_position_y[i]<0):
            bullet_position_y[i]=-12
            bullet_position_x[i]=-12
    for k in range(bullet_position_x.count(-12)):
        if(len(bullet_position_y)>1):
            bullet_position_y.remove(-12)
            bullet_position_x.remove(-12)


def bullet_print():
    for i in range(len(bullet_position_y)):
        pygame.draw.lines(screen,(0,128,125), True,[ (bullet_position_x[i],bullet_position_y[i]), (bullet_position_x[i],bullet_position_y[i]-5) ], 2)




def enemy_show_up(life,lines, hight):
    for i in range(50,250,30):
        #pygame.draw.rect(screen, (85,23,51) , pygame.Rect(i,50 , 10, 10))
        screen.blit(ENEMY,(i,hight))
        enemy_x.append(i)
        enemy_y.append(hight)
        enemy_position.append(hight)
        pygame.display.flip()
        enemy_life.append(life)
    if(lines == 2):
        for i in range(50,250,30):
            screen.blit(ENEMY,(i,hight+50))
            enemy_x.append(i)
            enemy_y.append(hight+50)
            enemy_position.append(hight+50)
            pygame.display.flip()
            enemy_life.append(life)

def enemy_draw():
    for i in range(len(enemy_y)):
        if(enemy_life[i] > 1):
            screen.blit(ENEMY,(enemy_x[i],enemy_y[i]))
        if(enemy_life[i] == 1):
            screen.blit(ENEMY_LOW,(enemy_x[i],enemy_y[i]))



def enemy_move(counter, hight, if_down):
    movement=0.7
    if(counter<20):
        movement
        for i in range(len(enemy_x)):

            if(enemy_position[i]==hight):
                enemy_x[i]+=0.7
            else:
                enemy_x[i]-=0.7
    else:
        for i in range(len(enemy_x)):
            if(enemy_position[i] == hight):
                enemy_x[i]-=0.7
            else:
                enemy_x[i]+=0.7

    if(if_down != 0):
        for i in range(len(enemy_y)):
            enemy_y[i]+=0.1




def enemy_bullet_create(hight):

    chosen_one=random.randrange(len(enemy_y))
    if(enemy_bullet_position_y[-1]>enemy_y[chosen_one]+bullet_intensity):
        if(len(enemy_y)<3):
            enemy_bullet_position_y.append(enemy_y[chosen_one]+10)
            enemy_bullet_position_x.append(enemy_x[chosen_one])
            #enemy_bullet_owner.append(enemy_y[random.randrange(len(enemy_y))])
            if(random.randint(1,100)<70):
                enemy_bullet_life.append(1)
            else:
                enemy_bullet_life.append(0)

        else:
            enemy_bullet_position_y.append(enemy_y[chosen_one]+10)
            enemy_bullet_position_x.append(enemy_x[chosen_one])
            enemy_bullet_life.append(1)

def enemy_bullet_print():
        for i in range(len(enemy_bullet_position_y)):
            if(enemy_bullet_life[i] >0):
                pygame.draw.lines(screen,(125,0,100), True,[ (enemy_bullet_position_x[i],enemy_bullet_position_y[i]), (enemy_bullet_position_x[i],enemy_bullet_position_y[i]+5) ], 2)


def enemy_bullet_update():
    for i in range(1,len(enemy_bullet_position_y)):
        enemy_bullet_position_y[i]+=2
    licznik=0
    for i in range(len(enemy_bullet_position_y)):
        if(enemy_bullet_position_y[i]>304):
            enemy_bullet_position_y[i]=308
            enemy_bullet_position_x[i]=308
            enemy_bullet_life[i]=-500
            licznik+=1
    for k in range(licznik):
        if(len(enemy_bullet_position_y)>1):
            enemy_bullet_position_y.remove(308)
            enemy_bullet_position_x.remove(308)
            enemy_bullet_life.remove(-500)



def detect_collision():
    for i in range(len(bullet_position_y)):
        for k in range(len(enemy_y)):
            if(bullet_position_y[i]>=enemy_y[k] and  bullet_position_x[i]<=enemy_x[k]+10 and bullet_position_y[i]<=enemy_y[k]+10and bullet_position_x[i] >= enemy_x[k]):
                enemy_life[k]-=1
                if(enemy_life[k]==0):
                    enemy_y[k]=-500
                    enemy_x[k]=-500
                    enemy_life[k]=-500
                    enemy_position[k]=-500
                    SCORE[0]+=1
                bullet_position_y[i]=-500
                bullet_position_x[i]=-500


    for i in range(len(enemy_y)):
        if(enemy_y[i]>300):
            return 1


    if(len(boss_life)>0):
        if(x<=enemy_x[0]+145 and x+10>= enemy_x[0] and y<=enemy_y[0] + 49 and y+10>= enemy_y[0]):
                return 1
    else:
        for i in range(len(enemy_x)):
            if(x<=enemy_x[i]+10 and x+10>= enemy_x[i] and y<=enemy_y[i] + 10 and y+10>= enemy_y[i]):
                return 1

    if(len(boss_life) != 0):
        for i in range(len(bullet_position_y)):
            if(bullet_position_y[i]>=enemy_y[0] and  bullet_position_x[i]<=enemy_x[0]+145 and bullet_position_y[i]<=enemy_y[0]+49and bullet_position_x[i] >= enemy_x[0]):
                boss_life[k]-=1
                if(boss_life[k]==0):
                    enemy_y[k]=-500
                    enemy_x[k]=-500
                    boss_life[k]=-500
                    SCORE[0]+=1
                bullet_position_y[i]=-500
                bullet_position_x[i]=-500
    if(len(meteoryt_x)>0):
        for i in range(len(meteoryt_x)):
            for k in range(len(bullet_position_y)):
                if(meteoryt_type[i] == 1):
                    if bullet_position_y[k]>=meteoryt_y[i] and  bullet_position_x[k]<=meteoryt_x[i]+10 and bullet_position_y[k]<=meteoryt_y[i]+10 and bullet_position_x[k] >= meteoryt_x[i] :
                        bullet_position_y[k] = -500
                        bullet_position_x[k] = -500
                elif(meteoryt_type[i] == 2):
                    if bullet_position_y[k]>=meteoryt_y[i] and  bullet_position_x[k]<=meteoryt_x[i]+20 and bullet_position_y[k]<=meteoryt_y[i]+20 and bullet_position_x[k] >= meteoryt_x[i] :
                        bullet_position_y[k] = -500
                        bullet_position_x[k] = -500


        for i in range(len(meteoryt_x)):
            for k in range(1, len(enemy_bullet_position_y)):
                if(meteoryt_type[i] == 1):
                    if enemy_bullet_position_y[k]>=meteoryt_y[i] and  enemy_bullet_position_x[k]<=meteoryt_x[i]+10 and enemy_bullet_position_y[k]<=meteoryt_y[i]+10 and enemy_bullet_position_x[k] >= meteoryt_x[i] :
                        enemy_bullet_position_y[k] = -500
                        enemy_bullet_position_x[k] = -500
                        enemy_bullet_life[k] = -500
                elif(meteoryt_type[i] == 2):
                    if enemy_bullet_position_y[k]>=meteoryt_y[i] and  enemy_bullet_position_x[k]<=meteoryt_x[i]+20 and enemy_bullet_position_y[k]<=meteoryt_y[i]+20 and enemy_bullet_position_x[k] >= meteoryt_x[i] :
                        enemy_bullet_position_y[k] = -500
                        enemy_bullet_position_x[k] = -500
                        enemy_bullet_life[k] = -500
        for i in range(enemy_bullet_position_x.count(-500)) :
            enemy_bullet_position_x.remove(-500)
            enemy_bullet_position_y.remove(-500)
            enemy_bullet_life.remove(-500)





    if(len(bonus_x)>0):
        for i in range(len(bullet_position_x)):
            for k in range(len(bonus_x)):
                if(bullet_position_x[i] >= bonus_x[k] and bullet_position_x[i] <= bonus_x[k] + 10 and bullet_position_y[i] <= bonus_y[k]+10 and bullet_position_y[i] >= bonus_y[k]):
                    bonus_x[k] = 500
                    bullet_type[0] += 1
                    SCORE[0]+=100


    if(len(boss_life) ==0):
        if(enemy_y.count(-500)>0):
            enemy_y.remove(-500)
            enemy_x.remove(-500)
            enemy_position.remove(-500)
            enemy_life.remove(-500)
    else:
        if(enemy_y.count(-500)>0):
            enemy_y.remove(-500)
            enemy_x.remove(-500)
            boss_life.remove(-500)
            return 1


    for i in range(1, len(enemy_bullet_position_y)):
        for k in range(len(enemy_y)):
            if(enemy_bullet_position_y[i]>=y and  enemy_bullet_position_x[i]<=x+10 and enemy_bullet_position_y[i]<=y+10 and enemy_bullet_position_x[i] >= x):
                if(enemy_bullet_life[i]>0):
                    bullet_type[0]=1
                    player_life[0]-=1
                    enemy_bullet_position_x[i]=-500
                    enemy_bullet_position_y[i]=-500
                    enemy_bullet_life[i]=-500
                    if(player_life[0] == 0):
                        return 1

    for i in range(enemy_bullet_position_x.count(-500)):
        enemy_bullet_position_x.remove(-500)
        enemy_bullet_position_y.remove(-500)
        enemy_bullet_life.remove(-500)


    if(len(meteoryt_x) !=0):
        for i in range(len(meteoryt_x)):
            if(meteoryt_type[i] ==1):
                if(x<=meteoryt_x[i]+10 and x+10>= meteoryt_x[i] and y<=meteoryt_y[i] + 10 and y+10>= meteoryt_y[i]):
                    return 1
            elif(meteoryt_type[i]==2):
                if(x<=meteoryt_x[i] + 20 and x+10>= meteoryt_x[i] and y<=meteoryt_y[i] + 20 and y+10>= meteoryt_y[i]):
                    return 1

def meteoryt_make(x):
    k=random.randrange(150, 300)
    meteoryt_x.append(x)
    meteoryt_y.append(k)
    meteoryt_type.append(random.randrange(1,3))


def meteoryt_create(intensity):
    for i in range(350,10000, intensity):
        meteoryt_make(i)


def meteoryt_draw():
    for i in range(len(meteoryt_y)):
        if(meteoryt_type[i]==1):
            screen.blit(METEORYT1,(meteoryt_x[i],meteoryt_y[i]))
        else:
            screen.blit(METEORYT2,(meteoryt_x[i],meteoryt_y[i]))
        meteoryt_x[i]-=0.9


def boss_show_up():
        screen.blit(BOSS,(50,50))
        boss_life.append(180)
        enemy_x.append(50)
        enemy_y.append(50)
        enemy_position.append(50)
        pygame.display.flip()
        enemy_life.append(4)

def boss_draw():
    if(len(enemy_x) > 0):
        screen.blit(BOSS,(enemy_x[0],enemy_y[0]))

def boss_bullet_create(zmienna):
    if(enemy_bullet_position_y[-1]>140):
        for i in range(zmienna, 159, 26):
            enemy_bullet_position_y.append(50+49)
            enemy_bullet_position_x.append(50+i)
            enemy_bullet_life.append(1)

def bonus_create(high, timex):
    l=time.time() - timex
    if(l > random.randrange(2,11)):
        if(len(bonus_y)==0):
                bonus_y.append(high)
                bonus_x.append(-10)


def bonus_print():
    if(len(bonus_y)>0):
        screen.blit(BONUS, (bonus_x[0],bonus_y[0]))

def bonus_move():
    if(len(bonus_x) > 0):
        bonus_x[0]+=1.5

def instrukcja():
    pygame.init()
    screen=pygame.display.set_mode((300, 300))
    screen.fill((0,0,0))
    screen.blit(INSTRUKCJA, (0 , 0))
    pygame.display.flip()
    while True:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if(pressed[pygame.K_SPACE]):

                return


def Menu():
    pygame.init()
    screen=pygame.display.set_mode((300, 300))
    menu_position=1
    screen.fill((0,0,0))
    instructions=small_font.render("Sterowanie po menu strzalkami, a wybor spacja", 1, (14,24,51))
    txt=myfont.render("Space Invanders", 1, (0,225,225))
    play=myfont.render("Play", 1, (0,225,225))
    instr=myfont.render("Instrukcja", 1, (0,225,225))
    ext=myfont.render("Exit", 1, (0,225,225))
    screen.blit(txt, (50,50))
    pygame.display.flip()
    while True:
        screen.fill((0,0,0))
        screen.blit(txt, (50,50))
        screen.blit(instructions,(10,270))

        nacisk=pygame.key.get_pressed()



        if(menu_position == 1):
                play2=myfont.render("Play", 1, (178,34,34))
                screen.blit(play2, (50,100))
                screen.blit(ext, (50,200))
                screen.blit(instr, (50,150))
        if(menu_position == 2):
            instr2=myfont.render("Instrukcja", 1, (178,34,34))
            screen.blit(instr2, (50,150))
            screen.blit(ext, (50,200))
            screen.blit(play, (50,100))
        if(menu_position == 3):
            ext2=myfont.render("Exit", 1, (178,34,34))
            screen.blit(ext2, (50,200))
            screen.blit(play, (50,100))
            screen.blit(instr, (50,150))
        for event in pygame.event.get():
                if nacisk[pygame.K_UP]:
                    if( menu_position != 1):
                        menu_position-=1

                if(nacisk[pygame.K_DOWN]):
                    if( menu_position != 3):
                        menu_position+=1
                if nacisk[pygame.K_SPACE]:
                    return menu_position
        pygame.display.flip()
        clock.tick(60)



pygame.init()
random.seed()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((300, 300))



INSTRUKCJA=pygame.image.load('Instrukcje.png')
ENEMY=pygame.image.load('enemy1.png')
ENEMY_LOW=pygame.image.load('enemy_low.png')
BOSS=pygame.image.load('boss.png')
SHIP=pygame.image.load('ship.png')
SHIP2=pygame.image.load('ship_2.png')
TEXT=pygame.image.load('txt.png')
METEORYT1=pygame.image.load('meteoryt1.png')
METEORYT2=pygame.image.load('big_met.png')
BONUS = pygame.image.load('bonus.png')


pygame.font.init()
myfont=pygame.font.SysFont('monospace', 25)
small_font=pygame.font.SysFont('monospace', 15)

while(1):
    player_life=[2]

    done = False
    x=150
    y=200
    bullet_position_y=[0]
    bullet_position_x=[-5]

    enemy_bullet_position_y=[302]
    enemy_bullet_position_x=[-5]
    enemy_bullet_life=[0]

    bullet_intensity=120
    counter=[0]
    counter2=[0]

    enemy_y=[]
    enemy_x=[]
    enemy_life=[]
    enemy_position=[]
    enemy_down_move=1

    level=0

    bullet_speed=30

    hight=50

    SCORE=[0]

    boss_life=[]

    meteoryt_x=[]
    meteoryt_y=[]
    meteoryt_type=[]

    bullet_type = [1]

    bonus_y=[]
    bonus_x=[]


    while(1):
        menu_ret = Menu()
        if(menu_ret == 1):
            break
        elif(menu_ret == 2):
            instrukcja()
        elif(menu_ret == 3):
            exit()

    screen.fill((0,0,0))

    game_start_time=time.time()

    while not done:

            if(len(enemy_x) == 0):
                enemy_down_move=1
                lines=2
                hight= 50
                bonus_x=[]
                bonus_y=[]
                start_time=time.time()
                meteoryt_x=[]
                meteoryt_y=[]
                meteoryt_type=[]
                font1=pygame.font.SysFont('monospace',1)
                level+=1
                display=myfont.render("level"+str(level), 1, (12,225,225))
                screen.blit(display, (125,125))
                pygame.display.flip()
                time.sleep(1)
                if(level<=3):
                    enemy_show_up(1,1, hight)
                    lines=1
                    pygame.display.flip()
                elif(level>3 and level<5):
                    bullet_intensity=100
                    enemy_show_up(level-2,2,hight)
                    pygame.display.flip()
                elif(level>=5 and level<7):
                    screen.fill((0,0,0))
                    txt=myfont.render("Survive!", 1, (12,225,225))
                    enemy_down_move=0
                    screen.blit(txt, (110, 125))
                    pygame.display.flip()
                    time.sleep(1)
                    bullet_intensity=70
                    meteoryt_create(80)
                    enemy_show_up(level-2,2,hight)

                elif(level>=7 and level<9):
                    bullet_intensity=100
                    enemy_show_up(level-2,2,hight)
                    pygame.display.flip()
                elif(level>=9 and level<11):
                    screen.fill((0,0,0))
                    txt=myfont.render("Survive !", 1, (12,225,225))
                    enemy_down_move=0
                    screen.blit(display, (110,125))
                    pygame.display.flip()
                    time.sleep(1)
                    bullet_intensity=70
                    meteoryt_create(80)
                    enemy_show_up(level-2,2,hight)
                elif(level>=11 and level <13):
                    enemy_down_move=0
                    bullet_intensity=67
                    meteoryt_create(65)
                    enemy_show_up(level-2,2,hight)
                    pygame.display.flip()
                elif(level >=13):
                    enemy_down_move=0
                    meteoryt_create(80)
                    boss_show_up()



            pressed=pygame.key.get_pressed()
            if (pressed[pygame.K_SPACE]):
                if(bullet_position_y[-1]<y-bullet_speed):
                    bullet_create(bullet_type[0], x, y)

            bullet_update()
            bullet_print()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True

            if(level!=13):
                enemy_bullet_create(hight)
            else:
                if(counter2[0] == 0):
                    boss_bullet_create(15)
                    counter2[0]=1
                elif(counter2[0] == 1):
                    boss_bullet_create(0)
                    counter2[0]=0

            enemy_bullet_update()


            enemy_move(counter[0], hight, enemy_down_move)

            counter[0]+=1
            if(counter[0]==40):
                counter[0]=0

            done=detect_collision()


            screen.fill((0, 0, 0))



            if pressed[pygame.K_UP]:
                if not (y<0):
                    y-=3
            if pressed[pygame.K_DOWN]:
                if not (y>290):
                    y+=3
            if pressed[pygame.K_LEFT]:
                if not (x==0):
                    x-=3
            if pressed[pygame.K_RIGHT]:
                if not (x>290):
                    x+=3





            color = (255, 100, 0)

            if(player_life[0] == 2):
                screen.blit(SHIP,(x,y))
            elif(player_life[0] == 1):
                screen.blit(SHIP2,(x,y))


            meteoryt_draw()
            bonus_move()
            bonus_print()

            score_txt=small_font.render("Score: "+str(SCORE[0]), 20, (12,225,225))
            screen.blit(score_txt, (0,0))
            time_txt=small_font.render("time: "+str(time.time() - game_start_time), 20, (12,225,225))
            screen.blit(time_txt, (198,0))

            if(level>=7):

                bonus_create(random.randrange(1,40),start_time)

            if(level != 13):
                enemy_draw()
                pygame.display.flip()
                enemy_bullet_print()
                bullet_print()
                pygame.display.flip()
            else:
                boss_draw()
                bullet_print()
                enemy_bullet_print()
                pygame.display.flip()
            clock.tick(60)


    if(level != 13 or ( level == 13 and len(boss_life) >0)):
        screen.fill((0,0,0))
        pygame.font.init()
        myfont=pygame.font.SysFont('monospace', 30)
        textsurface = myfont.render('GAME OVER', 1, (12,0,225))
        screen.blit(textsurface, (90,125))
        screen.blit(time_txt, (198,0))
        screen.blit(score_txt, (0,0))
        pygame.display.flip()
        time.sleep(4)
    elif(level == 13 and len(boss_life) == 0):
        screen.fill((0,0,0))
        pygame.font.init()
        myfont=pygame.font.SysFont('monospace', 30)
        textsurface = myfont.render('Congratulations!', 1, (12,0,225))
        screen.blit(textsurface, (70,125))
        screen.blit(score_txt, (0,0))
        screen.blit(time_txt, (198,0))
        pygame.display.flip()
        time.sleep(4)