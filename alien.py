import pygame
from pygame.sprite import Sprite
from random import randint
import math
class Alien(Sprite):

    def __init__(self,ai_game):
        super().__init__()
        self.baozha = False
        self.jin = 0
        self.wudi = False
        self.shanbi = False
        self.speed = ai_game.settings.alien_speed
        self.bul = ai_game.bullets
        self.time = []
        self.life = 1

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = ai_game.settings.alien_image
        self.rect = self.image.get_rect()
        self.direction = randint(0, 1)
        self.p = 1
        self.jian = 1
        self.r = 1
        self.l = 0
        self.t = 0
        self.b = 0


    def updata(self):
        a = self.find_zidan()
        self.duobi_zidan(a)
        self.smoothly_move()
        self.move_right()
        self.move_left()
        self.move_top()
        self.move_bottom()


#检测攻击
    def find_zidan(self):
        a = []
        b = []
        s = 0
        for bul in self.bul:
            a1 = bul.rect.centerx < self.rect.centerx + 2* self.rect.width
            a2 = bul.rect.centerx > self.rect.centerx - 2* self.rect.width
            a3 = bul.rect.top > self.rect.bottom
            if a1 and a2 and a3:
                self.jian = 1
                a.append(bul.rect.centerx)
                b.append(1 / (bul.rect.top - self.rect.bottom))
            else:
                self.jian = 0
        """#加权位置
        if len(b) !=0 :
            for i in range(len(a)):
                s = a[i] * b[i]
            s = s / sum(b)"""
        #无穷范数
        if len(b) != 0:
            ii = b.index(max(b))
            s = a[ii]
        return s

#躲避
    def duobi_zidan(self,a):
        if self.jian and self.life == 0:
            if a < self.rect.centerx:
                self.r = 1
                self.l = 0
            else:
                self.r = 0
                self.l = 1




#外星人运动
    def move_right(self):
        if self.rect.right<self.screen_rect.right and self.r:
            self.rect.x+=self.speed
    def move_left(self):
        if self.rect.left > self.screen_rect.left and self.l:
            self.rect.x-=self.speed
    def move_bottom(self):
        if self.b:
            self.rect.y+=self.speed
    def move_top(self):
        if self.rect.top>self.screen_rect.top and self.t:
            self.rect.y-=self.speed

#方向改变
    def direction_change(self):
        if 1-self.jian :
            self.l = 1 - self.l
            self.r = 1 - self.r



#平稳运动
    def smoothly_move(self):
        if self.rect.right == self.screen_rect.right:
            self.r = 0
            self.l = 1
        if self.rect.left == 0:
            self.r = 1
            self.l = 0
        self.p+=1
        if self.p % 100 == 0:
            a = randint(0, 1)
            if a:
                self.direction_change()
                """""
        if self.wudi:
            self.r = 0
            self.l = 0
            self.b = 0
            self.t = 0
        elif 1-self.r and 1-self.l:
            self.r = self.direction
            self.l = 1 - self.direction
            """""





#brown运动
    def brown_move(self):
        a = randint(0, 1)
        b = randint(0, 100)
        if a ==1 and self.rect.right<self.screen_rect.right:
            self.move_right()
        elif a==0 and self.rect.left>self.screen_rect.left:
            self.move_left()
        if b ==0 :
            self.move_top()
        elif b==1 and self.rect.x<self.screen_rect.top:
            self.move_bottom()
#螺旋线运动
    def luoxian_move(self,p1,p2,t):
        dx = -(self.rect.x-p1) + (self.rect.y - p2)
        dy = -(self.rect.x-p1) - (self.rect.y - p2)
        self.rect.x += dx * 0.005
        self.rect.y += dy * 0.005




