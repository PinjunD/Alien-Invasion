import pygame.font

class Button:
    def __init__(self, ai_game, msg, type):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #按钮大小
        self.width, self.height = 200, 50
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if type == 0:
            self.button_color = (200, 200, 255)
            self.rect.center = self.screen_rect.center
        else:
            self.rect.midtop = self.screen_rect.midtop
        self.prep(msg)

    def prep(self, msg):
        if type == 0:
            self.m_image = self.font.render(msg, True, self.text_color, self.button_color)
        else:
            self.m_image = self.font.render(msg, True, self.text_color)
        self.m_image_rect = self.m_image.get_rect()
        self.m_image_rect.center = self.rect.center

    def draw_button(self):
        if type == 0:
            self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.m_image, self.m_image_rect)




