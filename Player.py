import pygame

walkRight = [pygame.image.load('walkRight/R0.png'), pygame.image.load('walkRight/R1.png'), pygame.image.load('walkRight/R2.png'), pygame.image.load('walkRight/R3.png'), pygame.image.load('walkRight/R4.png')]
walkLeft = [pygame.image.load('walkLeft/L0.png'), pygame.image.load('walkLeft/L1.png'), pygame.image.load('walkLeft/L2.png'), pygame.image.load('walkLeft/L3.png'), pygame.image.load('walkLeft/L4.png')]
walkUp = [pygame.image.load('walkUp/U0.png'), pygame.image.load('walkUp/U1.png'), pygame.image.load('walkUp/U2.png'), pygame.image.load('walkUp/U3.png'), pygame.image.load('walkUp/U4.png')]
walkDown = [pygame.image.load('walkDown/D0.png'), pygame.image.load('walkDown/D1.png'), pygame.image.load('walkDown/D2.png'), pygame.image.load('walkDown/D3.png'), pygame.image.load('walkDown/D4.png')]

walkUpRight = [pygame.image.load('walkUpRight/UR0.png'), pygame.image.load('walkUpRight/UR1.png'), pygame.image.load('walkUpRight/UR2.png'), pygame.image.load('walkUpRight/UR3.png'), pygame.image.load('walkUpRight/UR4.png')]
walkUpLeft = [pygame.image.load('walkUpleft/UL0.png'), pygame.image.load('walkUpleft/UL1.png'), pygame.image.load('walkUpleft/UL2.png'), pygame.image.load('walkUpleft/UL3.png'), pygame.image.load('walkUpleft/UL4.png')]
walkDownRight = [pygame.image.load('walkDownRight/DR0.png'), pygame.image.load('walkDownRight/DR1.png'), pygame.image.load('walkDownRight/DR2.png'), pygame.image.load('walkDownRight/DR3.png'), pygame.image.load('walkDownRight/DR4.png')]
walkDownLeft = [pygame.image.load('walkDownLeft/DL0.png'), pygame.image.load('walkDownLeft/DL1.png'), pygame.image.load('walkDownLeft/DL2.png'), pygame.image.load('walkDownLeft/DL3.png'), pygame.image.load('walkDownLeft/DL4.png')]

char = pygame.image.load('idle/up.png')
charDown = pygame.image.load('idle/down.png')
charLeft = pygame.image.load('idle/left.png')
charRight = pygame.image.load('idle/right.png')

charUpRight = pygame.image.load('idle/upright.png')
charUpLeft = pygame.image.load('idle/upleft.png')
charDownRight = pygame.image.load('idle/downright.png')
charDownLeft = pygame.image.load('idle/downleft.png')

#Player Class
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.health = 100

        self.vel = 10

        self.hitbox = (self.x + 6, self.y + 6, 19, 19)

        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.moving = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 5:
            self.walkCount = 0
            
        if not self.moving:
            if self.right:
                if self.up:
                    win.blit(charUpRight, (self.x,self.y))
                elif self.down:
                    win.blit(charDownRight, (self.x,self.y))
                else:
                    win.blit(charRight, (self.x,self.y))
            elif self.left:
                if self.up:
                    win.blit(charUpLeft, (self.x,self.y))
                elif self.down:
                    win.blit(charDownLeft, (self.x,self.y))
                else:
                    win.blit(charLeft, (self.x,self.y))
            elif self.up:
                if self.right:
                    win.blit(charUpRight, (self.x,self.y))
                elif self.left:
                    win.blit(charUpLeft, (self.x,self.y))
                else:
                    win.blit(char, (self.x,self.y))
            elif self.down:
                if self.right:
                    win.blit(charDownRight, (self.x,self.y))
                elif self.left:
                    win.blit(charDownLeft, (self.x,self.y))
                else:
                    win.blit(charDown, (self.x,self.y))
            else:
                win.blit(char, (self.x,self.y))
        else:
            if self.right:
                if self.up:
                    win.blit(walkUpRight[self.walkCount], (self.x,self.y))
                elif self.down:
                    win.blit(walkDownRight[self.walkCount], (self.x,self.y))
                else:
                    win.blit(walkRight[self.walkCount], (self.x,self.y))
                self.walkCount += 1
            elif self.left:
                if self.up:
                    win.blit(walkUpLeft[self.walkCount], (self.x,self.y))
                elif self.down:
                    win.blit(walkDownLeft[self.walkCount], (self.x,self.y))
                else:
                    win.blit(walkLeft[self.walkCount], (self.x,self.y))
                self.walkCount += 1
            elif self.up:
                if self.right:
                    win.blit(walkUpRight[self.walkCount], (self.x,self.y))
                elif self.left:
                    win.blit(walkUpLeft[self.walkCount], (self.x,self.y))
                else:
                    win.blit(walkUp[self.walkCount], (self.x,self.y))
                self.walkCount += 1
            elif self.down:
                if self.right:
                    win.blit(walkDownRight[self.walkCount], (self.x,self.y))
                elif self.left:
                    win.blit(walkDownLeft[self.walkCount], (self.x,self.y))
                else:
                    win.blit(walkDown[self.walkCount], (self.x,self.y))
                self.walkCount += 1

        self.hitbox = (self.x + 6, self.y + 6, 19, 19)
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)    
