import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.shanbi = True
        self.time = -1
        self.speed = ai_game.ship.bul_speed
        self.screen = ai_game.screen
        self.settings = ai_game.settings

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)


class Bullet1(Bullet):

    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.shanbi = True
        self.time = -1
        self.name='b1'
        self.color=self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bullet2(Bullet):

    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.name = 'b2'
        self.speed = ai_game.ship.bul_speed*10
        self.image = ai_game.settings.bullet2_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

class Bullet3(Bullet):

    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.name = 'b3'
        self.speed = ai_game.ship.bul_speed//2
        self.image = ai_game.settings.bullet3_image
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)


class Bullet4(Bullet):

    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.name = 'b4'
        self.speed = ai_game.ship.bul_speed*3
        self.image = pygame.image.load('images/burn0.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

class Bullet5(Bullet):

    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.shanbi = True
        self.time = -1
        self.name = 'b5'
        self.image = pygame.image.load('images/jiguang1.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

class Bullet6(Bullet):

    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.aliens = ai_game.aliens
        self.name = 'feiji'
        self.image = self.settings.feiji
        self.rect = self.image.get_rect()
        self.rect.right = self.settings.rect.left
        self.avg = 0
        for alien in self.aliens:
            self.avg+=alien.rect.y
        self.avg /= len(self.aliens)
        self.rect.top = self.avg
    def update(self):
        self.rect.x+=1

class Bullet7(Bullet):

    def __init__(self,ai_game):
        super().__init__(ai_game)
        self.tp = 0
        self.name='b7'
        self.color=self.settings.bullet_color
        self.height = self.settings.bullet_height
        self.width = self.settings.bullet_width
        self.rect = pygame.Rect(0, 0, self.width,self.height)
        self.ship = ai_game.ship
        self.ship1 = ai_game.ship1
        self.rect.midbottom = ai_game.ship.rect.midtop
    def update(self):
        if self.height < self.settings.rect.height:
            self.height += self.speed*3
        if self.height+2 > self.settings.rect.height:
            if self.width < self.settings.bullet_width * 5:
                self.width += 5
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if self.tp == 0:
            self.rect.midbottom = self.ship.rect.midtop
        elif self.tp == 1 :
            self.rect.midbottom = self.ship1.rect.midtop
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)