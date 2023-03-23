from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__()
        self.speed = speed
        self.player_image = transform.scale(image.load(player_image), (size_w, size_h))
        self.rect = self.player_image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__(player_image, x, y, speed, size_w, size_h)
        self.bullets = []

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 400:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.draw(screen)
            bullet.update()

class Player2(GameSprite):
    def __init__(self, player_image, x, y, speed, size_w, size_h):
        super().__init__(player_image, x, y, speed, size_w, size_h)
        self.bullets = []

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.player_image, (self.rect.x, self.rect.y))
        for bullet in self.bullets:
            bullet.draw(screen)
            bullet.update()

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed

        if player.rect.colliderect(ball.rect):
            self.speed = self.speed * (-1)
        if player2.rect.colliderect(ball.rect):
            self.speed = self.speed * (-1)
background = transform.scale(image.load("Fon.png"), (700, 500))
player = Player("Ukrainian.png", 50, 200, 5, 100, 100)
player2 = Player2("Poland.png", 550, 200, 5, 100, 100)
ball = Ball("Pytin.png", 300, 200, 5, 50, 50)
window = display.set_mode((700, 500))
run = True
clock = time.Clock()

while run:
    #обробка подій
    for e in event.get():
        if e.type == QUIT:
            run = False
    #draw
    window.blit(background, (0, 0))
    player.draw(window)
    player2.draw(window)
    ball.draw(window)
    #оновлення обєктів
    player.update()
    player2.update()
    ball.update()
    display.update()
    clock.tick(60)
