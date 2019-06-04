import pygame

ui_reload = [pygame.image.load('ui_reload/R0.png'), pygame.image.load('ui_reload/R1.png'), pygame.image.load('ui_reload/R2.png'), pygame.image.load('ui_reload/R3.png'), pygame.image.load('ui_reload/R4.png'), pygame.image.load('ui_reload/R5.png')]
ui = pygame.image.load('UI.png')

screenWidth = 500
screenHeight = 500

#UI Class
class ui(object):
    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = 0

        self.reload = False
        
    def draw(self, win):
        if(self.reload):
            for x in range(6):
                win.blit(ui_reload[x], (self.x,self.y))
        else:
            win.blit(ui_reload[self.pos], (0, screenHeight - 100))
