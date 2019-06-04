import pygame

#Enemy Class
class enemy(object):
    walkRight = [pygame.image.load('enemy/walkRight/R0.png'), pygame.image.load('enemy/walkRight/R1.png'), pygame.image.load('enemy/walkRight/R2.png'), pygame.image.load('enemy/walkRight/R3.png'), pygame.image.load('enemy/walkRight/R4.png')]
    walkLeft = [pygame.image.load('enemy/walkLeft/L0.png'), pygame.image.load('enemy/walkLeft/L1.png'), pygame.image.load('enemy/walkLeft/L2.png'), pygame.image.load('enemy/walkLeft/L3.png'), pygame.image.load('enemy/walkLeft/L4.png')]
    walkUp = [pygame.image.load('enemy/walkUp/U0.png'), pygame.image.load('enemy/walkUp/U1.png'), pygame.image.load('enemy/walkUp/U2.png'), pygame.image.load('enemy/walkUp/U3.png'), pygame.image.load('enemy/walkUp/U4.png')]
    walkDown = [pygame.image.load('enemy/walkDown/D0.png'), pygame.image.load('enemy/walkDown/D1.png'), pygame.image.load('enemy/walkDown/D2.png'), pygame.image.load('enemy/walkDown/D3.png'), pygame.image.load('enemy/walkDown/D4.png')]

    def __init__(self, x, y, width, height, length, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.length = length
        self.health = health

        self.hitbox = (self.x + 6, self.y + 6, 28, 60)

        self.initial_x = x
        self.initial_y = y

        self.path = [self.x - self.length, self.x + self.length]
        self.walkCount = 0
        self.vel = 5

    def draw(self,win):
        self.move()
        if self.walkCount + 1 == 5:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1

        self.hitbox = (self.x + 6, self.y + 6, 19, 19)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        print('hit')
        pass
