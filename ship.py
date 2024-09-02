import pygame

class Ship:

    def __init__(self, ai_game):
        self.wuqi=0
        self.setting = ai_game.settings
        self.speed =self.setting.ship_speed
        self.bul_speed = ai_game.settings.bullet_speed
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/paotai0.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    def updata(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.x+=self.speed
        if self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.x-=self.speed
        if self.moving_up and self.rect.bottom<self.screen_rect.bottom:
            self.rect.y+=self.speed
        if self.moving_down and self.rect.top>self.screen_rect.top:
            self.rect.y-=self.speed


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def qiehuan(self):
        self.wuqi += 1
        self.wuqi %= 6

    def s0(self):
        #self.speed *= 5
        #self.bul_speed *= 5
        self.speed = self.setting.ship_speed
        self.bul_speed = self.setting.bullet_speed
        self.image = pygame.image.load('images/paotai0.png')

    def s1(self):
        self.speed = self.setting.ship_speed
        self.bul_speed = self.setting.bullet_speed
        self.setting.bullet_color=(0,0,255)
        self.image = pygame.image.load('images/paotai1.png')
        #self.image = pygame.image.load('images/sunchonglin.png')
    def s2(self):
        self.speed = self.setting.ship_speed
        self.bul_speed = self.setting.bullet_speed
        self.setting.bullet_color = (255, 0, 0)
        self.image = pygame.image.load('images/paotai2.png')

    def s3(self):
        self.speed = self.setting.ship_speed
        self.bul_speed= self.setting.bullet_speed
        self.setting.bullet_color = (255, 0, 255)
        self.image = pygame.image.load('images/paotai3.png')

    def s4(self):
        self.speed = self.setting.ship_speed
        self.bul_speed = self.setting.bullet_speed
        self.setting.bullet_color = (255, 255, 0)
        self.image = pygame.image.load('images/paotai4.png')

    def s5(self):
        self.speed = self.setting.ship_speed
        self.bul_speed = self.setting.bullet_speed
        self.setting.bullet_color = (0, 255, 255)
        self.image = pygame.image.load('images/paotai5.png')
        #self.image = pygame.image.load('images/sunchonglin.png')


