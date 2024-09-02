import pygame
class Settings:
    """储存设置的类"""
    def __init__(self):
        """初始化"""
        self.bj = pygame.image.load('images/bj.png')
        self.rect = self.bj.get_rect()
        self.screen_width= self.rect.right
        self.screen_height = self.rect.height
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))

        self.ship_speed = 2
        self.bullet2_image = pygame.image.load('images/zidan.png')
        self.bullet2zha0 = pygame.image.load('images/guang.png')
        self.bullet2zha1 = pygame.image.load('images/baozha_1.png')
        self.bullet2zha2 = pygame.image.load('images/baozha_2.png')
        self.bullet2zha3 = pygame.image.load('images/baozha_31.png')
        self.bullet2zha4 = pygame.image.load('images/baozha_.png')
        self.bullet3_image = pygame.image.load('images/zidan2.png')
        self.bullet4_image1 = pygame.image.load('images/burn0.png')
        self.bullet4_image2 = pygame.image.load('images/burn01.png')
        self.bullet4_image3 = pygame.image.load('images/burn02.png')
        self.bullet4_image4 = pygame.image.load('images/burn03.png')
        self.bullet4_image5 = pygame.image.load('images/burn04.png')
        self.bullet4_image6 = pygame.image.load('images/burn05.png')
        self.bullet4_image_b1 = pygame.image.load('images/burn1.png')
        self.bullet4_image_b2 = pygame.image.load('images/burn10.png')
        self.bullet4_image_b3 = pygame.image.load('images/burn20.png')
        self.bullet4_image_b4 = pygame.image.load('images/burn30.png')
        self.alien_image = pygame.image.load('images/alien.png')
        self.heidong1 = pygame.image.load('images/heidong1.png')
        self.heidong2 = pygame.image.load('images/heidong2.png')
        self.heidong3 = pygame.image.load('images/heidong3.png')
        self.heidong31 = pygame.image.load('images/heidong31.png')
        self.heidong32 = pygame.image.load('images/heidong32.png')
        self.heidong33 = pygame.image.load('images/heidong33.png')
        self.heidong34 = pygame.image.load('images/heidong34.png')
        self.heidong35 = pygame.image.load('images/heidong35.png')
        self.heidong36 = pygame.image.load('images/heidong36.png')
        self.heidong37 = pygame.image.load('images/heidong37.png')
        self.shanbi = pygame.image.load('images/shanbi.png')
        self.feiji = pygame.image.load('images/feiji_.png')
        self.feiji_speed = 3
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 50
        self.bullet_color = (0 , 255, 0)
        self.aliens_num = 1
        self.alien_baozha=pygame.image.load('images/baozha.png')
        self.alien_speed = 1
        self.boom_sound = pygame.mixer.Sound("sounds/boom.mp3")
        self.boom_sound.set_volume(0.5)
        self.ship = pygame.mixer.Sound("sounds/ship.mp3")
        self.ship.set_volume(0.5)
        self.bgm = pygame.mixer.Sound("sounds/B.flac")
        self.bgm.set_volume(2)
    def change_bullet_height(self,k):
        self.bullet_height*=k



    def change_bullet_speed(self, k):
        self.bullet_speed+=k

    def fill_bj(self):
        self.screen.blit(self.bj, self.rect)

