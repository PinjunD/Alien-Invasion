import sys
import pygame
import time
from random import randint
from settings import Settings
from ship import Ship
from bullet import Bullet1,Bullet2,Bullet3,Bullet4,Bullet5,Bullet6,Bullet7
from alien import Alien
from button import Button
import copy
class AlienInvasion:
    def __init__(self):
        pygame.init()

        #设置
        pygame.display.set_caption("Alien Invasion")
        self.zan = 0
        self.settings = Settings()
        self.R6 = False
        self.ganrao = False
        self.gaoraotime = 0
        self.xglo = 0
        self.yglo = 0
        self.point = 0
        self.screen = self.settings.screen
        self.time = 0
        self.ship = Ship(self)
        self.ship1 = Ship(self)
        self.ship1.ex = False
        self.ship1.time = -1
        self.play_button = Button(self, "play", 0)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.ship_sound = self.settings.ship
        self.boom_sound = self.settings.boom_sound
#开始游戏
    def run_game(self):
        self.settings.bgm.play()

        while True:
            self._check_events()
            if self.zan % 2 == 0:
                self._create_fleet()
                self.time += 1
                pygame.mouse.set_visible(False)
            else:
                pygame.mouse.set_visible(True)
            self._updata_screen()
#更新画面
    def _updata_screen(self):
        self.score_button = Button(self, f"{self.point}",1)
        self.settings.fill_bj()
        self.ship.blitme()
        if self.zan % 2 == 0:
            self.ship.updata()
            self.yiguanbi()
            if self.ship1.ex:
                self.ship1.blitme()
                self.ship1.updata()
            self.bullets.update()
            self._updata_aliens()
            self._updata_bullets()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet() 
            self._buls_aliens()
            self.won_or_lose()
        else:
            self.play_button.draw_button()
        self.aliens.draw(self.screen)
        self.score_button.draw_button()
        pygame.display.flip()
#按键设置
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.zan += 1
                if event.key == pygame.K_p:
                    sys.exit()
                if self.zan % 2 == 0:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                        self.ship1.moving_left = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                        self.ship1.moving_right = True
                    if event.key == pygame.K_UP:
                        self.ship.moving_down = True
                        self.ship1.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_up = True
                        self.ship1.moving_down = True
                    if event.key == pygame.K_a:
                        self.pinga()
                    if event.key == pygame.K_q:
                        self.settings.change_bullet_height(5)
                    if event.key == pygame.K_e:
                        self.daodan1()
                    if event.key == pygame.K_w:
                        self.ship.qiehuan()
                        a = self.ship.wuqi
                        if a == 0:
                            self.ship.s0()
                            self.ship1.s0()
                        elif a == 1:
                            self.ship.s1()
                            self.ship1.s1()
                        elif a == 2:
                            self.ship.s2()
                            self.ship1.s2()
                        elif a == 3:
                            self.ship.s3()
                            self.ship1.s3()
                        elif a == 4:
                            self.ship.s4()
                            self.ship1.s4()
                        elif a == 5:
                            self.ship.s5()
                            self.ship1.s5()
                    if event.key == pygame.K_1:
                        self.ship.s0()
                        self.ship1.s0()
                        self.ship.wuqi = 0
                    if event.key == pygame.K_2:
                        self.ship.s1()
                        self.ship1.s1()
                        self.ship.wuqi = 1
                    if event.key == pygame.K_3:
                        self.ship.s2()
                        self.ship1.s2()
                        self.ship.wuqi = 2
                    if event.key == pygame.K_4:
                        self.ship.s3()
                        self.ship1.s3()
                        self.ship.wuqi = 3
                    if event.key == pygame.K_5:
                        self.ship.s4()
                        self.ship1.s4()
                        self.ship.wuqi = 4
                    if event.key == pygame.K_6:
                        self.ship.s5()
                        self.ship1.s5()
                        self.ship.wuqi = 5

                    if event.key == pygame.K_r:
                        self.R6 = True
                        self.dazhao()
                    if event.key == pygame.K_u:
                        self.daodan3()
                        self.daodan5()
                    if event.key == pygame.K_k:
                        self.waigua()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                    self.ship1.moving_left = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                    self.ship1.moving_right = False
                if event.key == pygame.K_UP:
                    self.ship.moving_down = False
                    self.ship1.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_up = False
                    self.ship1.moving_down = False
                if event.key == pygame.K_q:
                    self.settings.change_bullet_height(1/5)
                if event.key == pygame.K_r:
                    self.R6 = False

#点击设置
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and self.zan % 2 == 1:
            self.zan += 1

#创建一批外星人
    def _create_fleet(self):
        #i = 0
        #while( i < self.settings.aliens_num ):
        if len(self.aliens)<100 and self.time%100==0:
            #i+=1
            k1 = randint(0,self.settings.screen_width)
            k2 = randint(0, self.settings.screen_height/8)
            alien = Alien(self)
            alien.rect.x = k1
            alien.rect.y = k2
            self.aliens.add(alien)
#开火
    def pinga(self):
        new_bullet = Bullet1(self)
        if self.ship1.ex :
            new_bullet1 = Bullet1(self)
            new_bullet1.rect.midbottom = self.ship1.rect.midtop
            self.bullets.add(new_bullet1)
        self.bullets.add(new_bullet)
    def daodan2(self):
        new_bullet = Bullet2(self)
        if self.ship1.ex :
            new_bullet1 = Bullet2(self)
            new_bullet1.rect.midbottom = self.ship1.rect.midtop
            self.bullets.add(new_bullet1)
        self.bullets.add(new_bullet)
    def daodan3(self):
        new_bullet = Bullet3(self)
        if self.ship1.ex :
            new_bullet1 = Bullet3(self)
            new_bullet1.rect.midbottom = self.ship1.rect.midtop
            self.bullets.add(new_bullet1)
        self.bullets.add(new_bullet)
    def daodan1(self):
        new_bullet = Bullet2(self)
        if self.ship1.ex:
            new_bullet1 = Bullet2(self)
            new_bullet1.rect.midbottom = self.ship1.rect.midtop
            self.bullets.add(new_bullet1)
        self.bullets.add(new_bullet)
    def daodan4(self):
        new_bullet = Bullet4(self)
        if self.ship1.ex :
            new_bullet1 = Bullet4(self)
            new_bullet1.rect.midbottom = self.ship1.rect.midtop
            self.bullets.add(new_bullet1)
        self.bullets.add(new_bullet)
    def daodan5(self):
        new_bullet = Bullet5(self)
        if self.ship1.ex :
            new_bullet1 = Bullet5(self)
            new_bullet1.rect.midbottom = self.ship1.rect.midtop
            self.bullets.add(new_bullet1)
        self.bullets.add(new_bullet)
    def jiguang(self):
        new_bullets = Bullet7(self)
        if self.ship1.ex :
            new_bullet1 = Bullet7(self)
            new_bullet1.tp = 1
            self.bullets.add(new_bullet1)
        self.bullets.add(new_bullets)
#子弹爆炸
    def _updata_bullets(self):
        for bul in self.bullets.sprites():
            if bul.rect.bottom < 0:
                self.bullets.remove(bul)
            #1号子弹
            if bul.name == 'b1':
                if bul.time != -1:
                    self.bullets.remove(bul)
            #3号子弹
            elif bul.name == 'b3':
                if bul.time != -1:
                    bul.speed = 0
                    bul.image = self.settings.bullet2zha0
                    r = bul.rect
                    a = self.boom_sound
                    a.fadeout(500)
                    a.play()
                    if self.time - 15 > bul.time and bul.time != -1:
                        #bul.shanbi = False
                        bul.image = self.settings.bullet2zha1
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                    if self.time - 20 > bul.time and bul.time != -1:
                        bul.image = self.settings.bullet2zha2
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                    if self.time - 30 > bul.time and bul.time != -1:
                        bul.image = self.settings.bullet2zha3
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                    if self.time - 35 > bul.time and bul.time != -1:
                        bul.image = self.settings.bullet2zha4
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                    if self.time - 40 > bul.time and bul.time != -1:
                        self.bullets.remove(bul)

            #四号子弹
            elif bul.name == 'b4':
                if self.time % 6 == 0:
                    bul.image = self.settings.bullet4_image1
                elif self.time % 17 == 1 or self.time % 13 == 2 or self.time % 17 == 3:
                    bul.image = self.settings.bullet4_image2
                elif self.time % 17 == 4 or self.time % 13 == 5 or self.time % 17 == 6:
                    bul.image = self.settings.bullet4_image3
                elif self.time % 17 == 7 or self.time % 13 == 8 or self.time % 17 == 9:
                    bul.image = self.settings.bullet4_image4
                elif self.time % 17 == 10 or self.time % 13 == 11 or self.time % 17 == 12:
                    bul.image = self.settings.bullet4_image5
                else:
                    bul.image = self.settings.bullet4_image6
                if bul.time != -1:
                    bul.speed = 0
                    r = bul.rect
                    #if self.time - 15 > bul.time and bul.time != -1:
                        #bul.shanbi = False
                    if self.time - 30 > bul.time and bul.time != -1:

                        if self.time % 4 == 0:
                            bul.image = self.settings.bullet4_image_b1
                        elif self.time % 4 == 1:
                            bul.image = self.settings.bullet4_image_b2
                        elif self.time % 4 == 2:
                            bul.image = self.settings.bullet4_image_b3
                        else:
                            bul.image = self.settings.bullet4_image_b4
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                    if self.time - 1000 > bul.time and bul.time != -1:
                        self.bullets.remove(bul)
            # 五号子弹
            elif bul.name == 'b5':
                if bul.time != -1:
                    self.gaoraotime = bul.time
                    bul.speed = 0
                    bul.shanbi = False
                    r = bul.rect
                    if self.time - 10 > bul.time and bul.time != -1:
                        bul.image = self.settings.heidong1
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                    if self.time - 20 > bul.time and bul.time != -1:
                        bul.speed = 0
                        bul.image = self.settings.heidong2
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                    if self.time - 30 > bul.time and bul.time != -1:
                        if (self.time %128)//16 == 0:
                            bul.image = self.settings.heidong3
                        elif (self.time %128)//16 == 1:
                            bul.image = self.settings.heidong31
                        elif (self.time %128)//16 == 2:
                            bul.image = self.settings.heidong32
                        elif (self.time %128)//16 == 3:
                            bul.image = self.settings.heidong33
                        elif (self.time %128)//16 == 4:
                            bul.image = self.settings.heidong34
                        elif (self.time %128)//16 == 5:
                            bul.image = self.settings.heidong35
                        elif (self.time %128)//16 == 6:
                            bul.image = self.settings.heidong36
                        elif (self.time %128)//16 == 7:
                            bul.image = self.settings.heidong37
                        bul.rect = bul.image.get_rect()
                        bul.rect.center = r.midtop
                        self.ganrao = True
                        self.xglo = bul.rect.centerx
                        self.yglo = bul.rect.centery
                    if self.time - 300 > bul.time and bul.time != -1:
                        self.bullets.remove(bul)
            # 七号子弹
            elif bul.name == 'b7':
                if 1-self.R6 or (self.time - 1000 > bul.time and bul.time != -1):
                    self.bullets.remove(bul)
                if bul.tp == 1 and 1-self.ship1.ex:
                    self.bullets.remove(bul)
            elif bul.name =='feiji':
                self.ship_sound.play()
                if bul.rect.left > self.settings.rect.right:
                    self.bullets.remove(bul)

#外星人更新
    def _updata_aliens(self):
        for alien in self.aliens.sprites():
            if self.time %3 == 1:
                alien.b = 1
            else:
                alien.b = 0
            if self.time %10 == 1:
                alien.t = 1
            else:
                alien.t = 0
            if self.ganrao:
                alien.luoxian_move(self.xglo,self.yglo,self.time-self.gaoraotime)
            else:
                alien.updata()
            if self.time-self.gaoraotime>300:
                self.ganrao = False


            if len(alien.time) != 0:
                if self.time - 20 > alien.time[-1] and alien.baozha:
                        self.aliens.remove(alien)

                        self.point += 1
                if self.time - 150 > alien.time[-1] and 1-alien.baozha:
                        alien.wudi = False
                        alien.image = self.settings.alien_image
#碰撞检测
    def _buls_aliens(self):
        for bul in self.bullets.sprites():
            for alien in self.aliens.sprites():
                a1 = bul.rect.right < alien.rect.right
                a2 = bul.rect.right > alien.rect.left
                b1 = bul.rect.left < alien.rect.right
                b2 = bul.rect.left > alien.rect.left
                c1 = bul.rect.bottom > alien.rect.top
                c2 = bul.rect.top < alien.rect.bottom
                d = bul.rect.right > alien.rect.right and  bul.rect.left < alien.rect.left
                if ((a1 and a2 )or( b1 and b2 )or d)and c1 and c2 and 1 - alien.baozha and 1-alien.wudi:
                    if bul.time == -1:
                        bul.time = self.time
                    if alien.life > 0:
                        alien.life -= 1
                        alien.time.append(self.time)
                        alien.shanbi = True
                        alien.jin = 0
                        if bul.shanbi:
                            alien.wudi = True
                            alien.shanbi = True

                    elif alien.life == 0 :
                        if bul.name != 'b5':
                            alien.baozha =True
                            alien.image = self.settings.alien_baozha
                            alien.time.append(self.time)



                if bul.shanbi and len(alien.time) != 0 and alien.shanbi:
                    if self.time - 10 > alien.time[-1]:
                        alien.image = self.settings.shanbi
                    if self.time - 10 > alien.time[-1]:
                        """""
                        alien.rect.bottom += 100
                        alien.shanbi = False
                        """
                        alien.jin += 1
                        if alien.jin %2 ==0 :
                            alien.rect.bottom += 1
                            if alien.jin > 150:
                                alien.shanbi = False
#胜负判定
    def won_or_lose(self):
        a=0
        for alien in self.aliens:
            if alien.rect.bottom>self.settings.screen_height:
                a=1
                self.aliens.remove(alien)
            else:
                continue
        if a == 1:
            print("You lose!")
            #time.sleep(1)
            #sys.exit()
        elif len(self.aliens) == 0:
            time.sleep(1)
            #sys.exit()
#大招
    def dazhao(self):
        if self.ship.wuqi == 0:
            self.jinengyi()
        elif self.ship.wuqi == 1:
            self.daodan3()
        elif self.ship.wuqi == 2:
            self.daodan4()
        elif self.ship.wuqi == 3:
            self.daodan5()
        elif self.ship.wuqi == 4:
            fj = Bullet6(self)
            self.bullets.add(fj)
        elif self.ship.wuqi == 5:
            self.jiguang()
#一技能
    def jinengyi(self):
        self.ship1.rect.midbottom = self.ship.rect.midbottom
        self.ship1.rect.centerx = self.settings.screen_width - self.ship1.rect.centerx
        self.ship1.ex = True
        if self.ship1.time == -1:
            self.ship1.time = self.time
#一技能关闭
    def yiguanbi(self):
        if self.time - 2000 > self.ship1.time  :
            self.ship1.ex = False
            self.ship1.time = -1
#外挂
    def waigua(self):
        for alien in self.aliens.sprites():
            alien.life = 0

#主程序
if  __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
