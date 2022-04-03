
from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, img,spd=10, x=400, y=200, w=65, h=65):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.spd = spd
        self.rect.x = x
        self.rect.y = y 
    def draw(self):
        win.blit(self.image,(self.rect.x, self.rect.y))



class Racket(GameSprite):
    def move1(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x >0:
            self.rect.x -= self.spd
        if keys_pressed[K_DOWN] and self.rect.x < win_width-int(win_width/9):
            self.rect.x += self.spd

    def move2(self):
        keys_pressed=key.get_pressed()
        if keys_pressed[K_W] and self.rect.x >0:
            self.rect.x -= self.spd
        if keys_pressed[K_S] and self.rect.x < win_width-int(win_width/9):
            self.rect.x += self.spd


class Ball(GameSprite):
    def move1(self):
        pass

    
        





win_width = 800
win_height = 400



win = display.set_mode((win_width, win_height))
display.set_caption('PingPong')

bg = transform.scale(image.load('bg.jpg'), (win_width, win_height))


mixer.init()
mixer.music.load("tennis.ogg")
mixer.music.play()
hit_sond = mixer.Sound('hit.ogg')




ball = Ball ('ball.png')
racket1 = Racket('racket.png', 10, win_width/2 - 370, win_height/2 )
racket2 = Racket('racket.png', 10, win_width/2 + 300, win_height/2 )


FPS = 60
clock = time.Clock()

game = True
stop = False



while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

        

    

    win.fill((100,155,255))
    ball.draw()
    racket1.draw()
    racket2.draw()

    display.update()
    clock.tick(FPS)

