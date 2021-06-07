from pygame import *
window = display.set_mode((700, 500))
display.set_caption("ping pong")
class Game_sprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,scale_x,scale_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(scale_x,scale_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class Player(Game_sprite):
    def updateR(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y >= 2:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y  <= 340:
            self.rect.y += self.speed
    def updateL(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y >= 2:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y  <= 340:
            self.rect.y += self.speed
class Ball(Game_sprite):
    def update(self,x,y,upy):
        self.rect.x += x
        if upy:
            self.rect.y -= y
background = transform.scale(image.load("grass.jpg"),(700, 500))
game_rendering = True
player1 = Player("player.png",20,250,20,150,5)
player2 = Player("player.png",670,250,20,150,5)
ball = Ball("Tennis_Ball.png",350,250,50,50,0)
dx = 2
dy = 2
p = True
font.init()
font = font.Font(None,50)
timer = font.render("3", 1,(255,0,0))
over = font.render("Game over", 1,(255,0,0))
play_time = True
updatey = False
clock = time.Clock()
while game_rendering:
    if p:
        start_time = time.get_ticks()
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game_rendering = False
    if play_time:
        current_time = time.get_ticks()
        if sprite.collide_rect(ball,player1) or sprite.collide_rect(ball,player2):
            dx *= -1
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            dy *= -1
        if current_time-start_time >= 3000:
            updatey = True
        window.blit(background,(0,0))
        player1.updateL()
        player1.reset()
        player2.updateR()
        player2.reset()
        ball.update(dx,dy,updatey)
        ball.reset()
        display.update()
        if ball.rect.x <= 0 or ball.rect.x >= 700:
            window.blit(over,(300,200))
            play_time = False
        if p:
            window.blit(timer,(300,100))
            display.update()
            time.wait(1000)
            timer = font.render("2", 1,(255,0,0))
            window.blit(timer,(350,100))
            display.update()
            time.wait(1000)
            timer = font.render("1", 1,(255,0,0))
            window.blit(timer,(400,100))
            display.update()
            time.wait(1000)
            timer = font.render("0", 1,(255,0,0))
            start_time = time.get_ticks()
            p = False
