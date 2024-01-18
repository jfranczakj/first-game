from ast import Delete
from re import T
import pygame
import sys

#Dodajemy przyciski z pygame#
from pygame.locals import (
        K_UP,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        K_SPACE,
        KEYDOWN,
        KEYUP,
        QUIT, 
        K_d,
        K_a,
        K_w,
        K_z
        ) 

pygame.init()
pygame.mixer.init()

# Pare pomocniczych wartosci
wysokosc = 600
szerokosc = 800
FPS = 30
color = (255,255,255)
color_light = (170,170,170)
color_dark = (100,100,100)

# Wgrywamy potrzebne obrazki

hulk_r=pygame.image.load('hulk right.PNG')
hulk_r=pygame.transform.scale(hulk_r,(60,80))

hulk_l=pygame.image.load('hulk left.PNG')
hulk_l=pygame.transform.scale(hulk_l,(60,80))

captain_r=pygame.image.load('cap_r.PNG')
captain_r=pygame.transform.scale(captain_r,(60,80))

captain_l=pygame.image.load('cap_l.PNG')
captain_l=pygame.transform.scale(captain_l,(60,80))

iron_man_r=pygame.image.load('Maniron.PNG')
iron_man_r=pygame.transform.scale(iron_man_r,(60,80))

iron_man_l=pygame.image.load('Iron.PNG')
iron_man_l=pygame.transform.scale(iron_man_l,(60,80))

spider_r=pygame.image.load('Spider Man right.PNG')
spider_r=pygame.transform.scale(spider_r,(60,80))

spider_l=pygame.image.load('Spider Man left.PNG')
spider_l=pygame.transform.scale(spider_l,(60,80))

fala = pygame.image.load('wiatr.PNG')
fala = pygame.transform.scale(fala, (32,64))

tarcza = pygame.image.load('tarcza.PNG')
tarcza = pygame.transform.scale(tarcza, (32,32))

pajeczyna = pygame.image.load('pajeczyna.PNG')
pajeczyna = pygame.transform.scale(pajeczyna, (16,16))

laser = pygame.image.load('laser.PNG')
laser = pygame.transform.scale(laser, (8,4))

win = pygame.display.set_mode([szerokosc, wysokosc])
pygame.display.set_caption("Pierwsza gierka")

start = pygame.image.load('avengers.jpg')
tlo = pygame.image.load('wakanda.jpg')
win.blit(start, (0,0))
pygame.display.flip()

pygame.mixer.music.load("Marvel Studios.mp3")
pygame.mixer.music.play(loops=-1)

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('AVENGEANCE HEROIC AVENGER.otf', size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img = pygame.transform.scale(img , (15,40))
        img_rect = img.get_rect()
        img_rect.x = x + 30*i
        img_rect.y = y
        surf.blit(img, img_rect)


def menu_koncowe():
    win.fill((0,0,0))
    font = pygame.font.Font('AVENGEANCE HEROIC AVENGER.otf', 30)
    font1 = pygame.font.Font('AVENGEANCE HEROIC AVENGER.otf', 100)
    text = font.render('Quit' , True , color)
    text2 = font1.render('Winner:' , True , color)
    text3 = font.render('Player 1' , True , color)
    text4 = font.render('Player 2' , True , color)
    pygame.display.flip()
    waiting3 = True
    while waiting3:
        win.blit(text2 , (260,100))
        clock.tick(FPS)
        if player_l.lives == 0:
            win.blit(text4, (360,300))
            win.blit(player_r.surf, (360,350))
        elif player_r.lives == 0:
            win.blit(text3, (360,300))
            win.blit(player_l.surf, (360,350))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # Przycisk wyjscia
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= mouse[0] <= 440 and 500 <= mouse[1] <= 540:
                    pygame.quit()
                    

        mouse = pygame.mouse.get_pos()
        # Dalszy przycisk wyjscia
        if 300 <= mouse[0] <= 440 and 500 <= mouse[1] <= 540:
            pygame.draw.rect(win,color_light,[300,500,140,40])
        else:
            pygame.draw.rect(win,color_dark,[300,500,140,40])
        win.blit(text , (345,503))
        pygame.display.update()




def menu_startu():
    win.blit(start,(0,0))
    font = pygame.font.Font('AVENGEANCE HEROIC AVENGER.otf', 30)
    text = font.render('Quit' , True , color)
    text2 = font.render('Start' , True , color)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # Przycisk wyjscia
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 600 <= mouse[0] <= 740 and 500 <= mouse[1] <= 540:
                    pygame.quit()
            # Przycisk Startu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 60 <= mouse[0] <= 200 and 500 <= mouse[1] <= 540:
                    waiting = False

        mouse = pygame.mouse.get_pos()
        # Dalszy przycisk wyjscia
        if 600 <= mouse[0] <= 740 and 500 <= mouse[1] <= 540:
            pygame.draw.rect(win,color_light,[600,500,140,40])
        else:
            pygame.draw.rect(win,color_dark,[600,500,140,40])
        win.blit(text , (645,503))
        # Dalszy przycisk startu
        if 60 <= mouse[0] <= 200 and 500 <= mouse[1] <= 540:
            pygame.draw.rect(win,color_light,[60,500,140,40])
        else:
            pygame.draw.rect(win,color_dark,[60,500,140,40])
        win.blit(text2 , (98,504))
        pygame.display.update()


# Gracz pierwszy


class Player_l(pygame.sprite.Sprite):
    def __init__(self):
        super(Player_l, self).__init__()
        self.surf = iron_man_r
        self.surf_l = iron_man_l
        self.surf_r = iron_man_r
        self.surf = pygame.transform.scale(self.surf,(60,80))
        self.rect = self.surf.get_rect()
        self.lives = 3
        self.xvel = 0
        self.yvel = 600

    def shoot(self):
        bullet_l = Bullet_l(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet_l)
        bullets_l.add(bullet_l)

    def gravity(self):
        self.yvel+=3.2

    
    def update(self):
        toleracja = 50
        self.rect.move_ip((self.xvel,self.yvel))

        hits = pygame.sprite.spritecollide(player_l , belkas, False)
        if hits:
            if abs(hits[0].rect.centerx+80- self.rect.y) < toleracja:
                self.yvel *=-1
            if abs(hits[0].rect.top- self.rect.y-78) < toleracja:
                self.rect.y = hits[0].rect.top -78
                self.yvel = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > szerokosc:
            self.rect.right = szerokosc

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > wysokosc:
            self.rect.bottom = wysokosc

        if abs(belka2.rect.top- self.rect.y) < toleracja and self.rect.x > 140 and self.rect.x < 600:
            self.yvel = 0
        if abs(belka2.rect.top- self.rect.y-78) < toleracja and abs(self.rect.right- belka2.rect.left)< toleracja and abs(self.rect.left- belka2.rect.right)< toleracja:
            self.rect.y = belka2.rect.top -78
            self.yvel = 0


class Bullet_l(pygame.sprite.Sprite):
    def __init__(self, x, y, ):
        super(Bullet_l, self).__init__()
        if player_l.surf == iron_man_r or player_l.surf == iron_man_l:
            self.surf = laser
        elif player_l.surf == captain_r or player_l.surf == captain_l:
            self.surf = tarcza
        elif player_l.surf == hulk_r or player_l.surf == hulk_l:
            self.surf = fala
        else:
            self.surf = pajeczyna
        self.rect = self.surf.get_rect()
        self.rect.centerx = x
        self.rect.top = y+30
        if player_l.surf == player_l.surf_r:
            self.speed = 7
        else:
            self.speed = -7

    def update(self):
        self.rect.x += self.speed

        if self.rect.left > szerokosc:
            self.kill()
        if pygame.sprite.spritecollide(player_r, bullets_l, Delete):
            player_r.lives -= 1
            self.kill()
            print(player_r.lives)





# Gracz drugi

class Player_r(pygame.sprite.Sprite):
    def __init__(self):
        super(Player_r, self).__init__()
        self.surf = iron_man_r
        self.surf_l = iron_man_l
        self.surf_r = iron_man_r
        self.surf = pygame.transform.scale(self.surf,(60,80))
        self.rect = self.surf.get_rect()
        self.lives = 3
        self.xvel = 800
        self.yvel = 600

    def shoot(self):
        bullet_r = Bullet_r(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet_r)
        bullets_r.add(bullet_r)

    def gravity(self):
        self.yvel+=2.9
    
    def update(self):
        toleracja = 50
        self.rect.move_ip((self.xvel,self.yvel))

        hits = pygame.sprite.spritecollide(player_r , belkas, False)
        if hits:
            if abs(hits[0].rect.centerx+80- self.rect.y) < toleracja:
                self.yvel *=-1
            if abs(hits[0].rect.top- self.rect.y-78) < toleracja:
                self.rect.y = hits[0].rect.top -78
                self.yvel = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > szerokosc:
            self.rect.right = szerokosc

        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > wysokosc:
            self.rect.bottom = wysokosc

        if abs(belka2.rect.top- self.rect.y) < toleracja and self.rect.x > 140 and self.rect.x < 600:
            self.yvel = 0 
        if abs(belka2.rect.top- self.rect.y-78) < toleracja and abs(self.rect.right- belka2.rect.left)< toleracja and abs(self.rect.left- belka2.rect.right)< toleracja:
            self.rect.y = belka2.rect.top -78
            self.yvel = 0


        
class Bullet_r(pygame.sprite.Sprite):
    def __init__(self, x, y ):
        super(Bullet_r, self).__init__()
        if player_r.surf == iron_man_r or player_r.surf == iron_man_l:
            self.surf = laser
        elif player_r.surf == captain_r or player_r.surf == captain_l:
            self.surf = tarcza
        elif player_r.surf == hulk_r or player_r.surf == hulk_l:
            self.surf = fala
        else:
            self.surf = pajeczyna
        self.rect = self.surf.get_rect()
        self.rect.centerx = x
        self.rect.top = y+30
        if player_r.surf == player_r.surf_r:
            self.speed = 7
        else:
            self.speed = -7

    def update(self):
        self.rect.x += self.speed

        if self.rect.left < 0:
            self.kill()
        if pygame.sprite.spritecollide(player_l, bullets_r, Delete):
            player_l.lives -= 1
            self.kill()
            print(player_l.lives)

class Belka(pygame.sprite.Sprite):    
    def __init__(self, x, y, dlugosc):
        super(Belka, self).__init__()
        self.surf = pygame.Surface((dlugosc,30))  
        self.surf.fill((150, 75, 0))  
        self.rect = self.surf.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        
    


def menu_wyboru_postaci():
    win.fill((0,0,0))
    draw_text(win, "Choose a hero", 64, szerokosc/2, 30)
    draw_text(win, 'Player  1' , 30 , 100, 100)
    draw_text(win, 'Player  2' , 30 , 700, 100)
    pygame.display.flip()
    waiting2 = True
    while waiting2:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Wybor gracza po lewej stronie

                if 60 <= mouse[0] <= 110 and 150 <= mouse[1] <= 200:
                    player_l.surf = iron_man_r
                    player_l.surf_l = iron_man_l
                    player_l.surf_r = iron_man_r

                if 60 <= mouse[0] <= 110 and 250 <= mouse[1] <= 300:
                    player_l.surf = captain_r
                    player_l.surf_l = captain_l
                    player_l.surf_r = captain_r

                if 60 <= mouse[0] <= 110 and 350 <= mouse[1] <= 400:
                    player_l.surf = hulk_r
                    player_l.surf_l = hulk_l
                    player_l.surf_r = hulk_r
                    
                if 60 <= mouse[0] <= 110 and 450 <= mouse[1] <= 500:
                    player_l.surf = spider_r
                    player_l.surf_l = spider_l
                    player_l.surf_r = spider_r

                # wybor gracza po prawej stronie

                if 690 <= mouse[0] <= 740 and 150 <= mouse[1] <=200:
                    player_r.surf = iron_man_l
                    player_r.surf_l = iron_man_l
                    player_r.surf_r = iron_man_r
                
                if 690 <= mouse[0] <= 740 and 250 <= mouse[1] <=300:
                    player_r.surf = captain_l
                    player_r.surf_l = captain_l
                    player_r.surf_r = captain_r

                if 690 <= mouse[0] <= 740 and 350 <= mouse[1] <=400:
                    player_r.surf = hulk_l
                    player_r.surf_l = hulk_l
                    player_r.surf_r = hulk_r

                if 690 <= mouse[0] <= 740 and 450 <= mouse[1] <=500:
                    player_r.surf = spider_l
                    player_r.surf_l = spider_l
                    player_r.surf_r = spider_r

                if 330 <= mouse[0] <= 470 and 520 <= mouse[1] <= 560:
                    pygame.mixer.music.load("Avengers_Theme_Music.mp3")
                    pygame.mixer.music.play(loops=-1)
                    waiting2 = False

                    

        mouse = pygame.mouse.get_pos()

        # Czesc gracza po lewej

        if 60 <= mouse[0] <= 110 and 150 <= mouse[1] <= 200:
            pygame.draw.rect(win,color_light,[60,150,50,50])
        else:
            pygame.draw.rect(win,color_dark,[60,150,50,50])
            win.blit(iron_man_r, (300,130))
            draw_text(win, "Iron Man", 30, 210, 160)

        if 60 <= mouse[0] <= 110 and 250 <= mouse[1] <= 300:
            pygame.draw.rect(win,color_light,[60,250,50,50])
        else:
            pygame.draw.rect(win,color_dark,[60,250,50,50])
            win.blit(captain_r, (300,230))
            draw_text(win, "Capitan America", 30, 210, 260)

        if 60 <= mouse[0] <= 110 and 350 <= mouse[1] <= 400:
            pygame.draw.rect(win,color_light,[60,350,50,50])

        else:
            pygame.draw.rect(win,color_dark,[60,350,50,50])
            win.blit(hulk_r, (300,330))
            draw_text(win, "Hulk", 30, 210, 360)

        if 60 <= mouse[0] <= 110 and 450 <= mouse[1] <= 500:
            pygame.draw.rect(win,color_light,[60,450,50,50])
        else:
            pygame.draw.rect(win,color_dark,[60,450,50,50])
            win.blit(spider_r, (300,430))
            draw_text(win, "Spider-Man", 30, 210, 460)

        # czesc gracza po prawej

        if 690 <= mouse[0] <= 740 and 150 <= mouse[1] <= 200:
            pygame.draw.rect(win,color_light,[690,150,50,50])
        else:
            pygame.draw.rect(win,color_dark,[690,150,50,50])
            win.blit(iron_man_l, (450,130))
            draw_text(win, "Iron Man", 30, 590, 160)


        if 690 <= mouse[0] <= 740 and 250 <= mouse[1] <= 300:
            pygame.draw.rect(win,color_light,[690,250,50,50])
        else:
            pygame.draw.rect(win,color_dark,[690,250,50,50])
            win.blit(captain_l, (450,230))
            draw_text(win, "Capitan America", 30, 590, 260)


        if 690 <= mouse[0] <= 740 and 350 <= mouse[1] <= 400:
            pygame.draw.rect(win,color_light,[690,350,50,50])
        else:
            pygame.draw.rect(win,color_dark,[690,350,50,50])
            win.blit(hulk_l, (450,330))
            draw_text(win, "Hulk", 30, 590, 360)


        if 690 <= mouse[0] <= 740 and 450 <= mouse[1] <= 500:
            pygame.draw.rect(win,color_light,[690,450,50,50])
        else:
            pygame.draw.rect(win,color_dark,[690,450,50,50])
            win.blit(spider_l, (450,430))
            draw_text(win, "Spider-Man", 30, 590, 460)


        if 330 <= mouse[0] <= 470 and 520 <= mouse[1] <= 560:
            pygame.draw.rect(win,color_light,[330,520,140,40])
        else:
            pygame.draw.rect(win,color_dark,[330,520,140,40])
            draw_text(win, 'Fight', 30, 400, 523)
            

        

        pygame.display.update()


clock = pygame.time.Clock() 

run = True
game_over = True
game_over_2 = True
game_over_3 = True

while run:
    # plansza początkowa/końcowa i inicjalizacja gry
    if game_over:
        menu_startu()
        game_over = False
        pygame.time.delay(10)

        # stwórz instację obiektu gracza
        player_l = Player_l()
        player_r = Player_r()

        # kontenery obiektów 
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player_l)
        all_sprites.add(player_r)
        belkas = pygame.sprite.Group()

        # dodawanie belek


        belka1 = Belka(400,460,600)
        all_sprites.add(belka1)
        belkas.add(belka1)
        
        belka2 = Belka(400,300,400)
        all_sprites.add(belka2)
        belkas.add(belka2)

        

        bullets_l = pygame.sprite.Group()
        bullets_r = pygame.sprite.Group()

    if game_over_2:
        menu_wyboru_postaci()
        game_over_2 = False
    

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
            elif event.key == K_SPACE: 
                player_l.shoot()
            elif event.key == K_LEFT:
                player_l.xvel = -4
                player_l.surf = player_l.surf_l
            elif event.key == K_RIGHT:
                player_l.xvel = 4
                player_l.surf = player_l.surf_r
            elif event.key == K_UP:
                if player_l.rect.y==520 or player_l.rect.y==382 or player_l.rect.y==222:
                    player_l.yvel = -30
            elif event.key == K_a:
                player_r.xvel = -4
                player_r.surf = player_r.surf_l
            elif event.key == K_d:
                player_r.xvel = 4
                player_r.surf = player_r.surf_r
            elif event.key == K_w:
                if player_r.rect.y==520 or player_r.rect.y==382 or player_r.rect.y==222:
                    player_r.yvel = -30
            elif event.key == K_z:
                player_r.shoot()
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                player_l.xvel = 0 
            elif event.key == K_RIGHT:
                player_l.xvel = 0
            elif event.key == K_a:
                player_r.xvel = 0
            elif event.key == K_d:
                player_r.xvel = 0




    



    player_l.update()
    player_l.gravity()
    player_r.update()
    player_r.gravity()
    bullets_r.update()
    bullets_l.update()


    win.blit(tlo,(0,0))

    for entity in all_sprites:
        win.blit(entity.surf, entity.rect)

    draw_lives(win, 100, 5, player_l.lives, player_l.surf_r)
    draw_lives(win, szerokosc-150, 5, player_r.lives, player_r.surf_l)

    pygame.display.update()
    clock.tick(FPS)


    if player_r.lives == 0 or player_l.lives == 0:
        if game_over_3:
            pygame.mixer.music.load("victory.mp3")
            pygame.mixer.music.play(loops=-1)
            menu_koncowe()
            game_over_3 = False

    




pygame.mixer.music.stop()
pygame.mixer.quit()

pygame.quit()

