import pygame
import socket, asyncore
from fractions import Fraction

pygame.init()


#SOCKET
'''class HTTPClient(asyncore.dispatcher):

    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket()
        self.connect( (host, 85) )
        self.buffer = bytes('GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' %
                            (path, host), 'ascii')

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print(self.recv(8192))

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

client = HTTPClient('localhost', '/')
asyncore.loop()
print('PASS')'''


#Constants
screenWidth = 500
screenHeight = 500

#ANIMATION
walkRight = [pygame.image.load('walkRight/R0.png'), pygame.image.load('walkRight/R1.png'), pygame.image.load('walkRight/R2.png'), pygame.image.load('walkRight/R3.png'), pygame.image.load('walkRight/R4.png')]
walkLeft = [pygame.image.load('walkLeft/L0.png'), pygame.image.load('walkLeft/L1.png'), pygame.image.load('walkLeft/L2.png'), pygame.image.load('walkLeft/L3.png'), pygame.image.load('walkLeft/L4.png')]
walkUp = [pygame.image.load('walkUp/U0.png'), pygame.image.load('walkUp/U1.png'), pygame.image.load('walkUp/U2.png'), pygame.image.load('walkUp/U3.png'), pygame.image.load('walkUp/U4.png')]
walkDown = [pygame.image.load('walkDown/D0.png'), pygame.image.load('walkDown/D1.png'), pygame.image.load('walkDown/D2.png'), pygame.image.load('walkDown/D3.png'), pygame.image.load('walkDown/D4.png')]

walkUpRight = [pygame.image.load('walkUpRight/UR0.png'), pygame.image.load('walkUpRight/UR1.png'), pygame.image.load('walkUpRight/UR2.png'), pygame.image.load('walkUpRight/UR3.png'), pygame.image.load('walkUpRight/UR4.png')]
walkUpLeft = [pygame.image.load('walkUpleft/UL0.png'), pygame.image.load('walkUpleft/UL1.png'), pygame.image.load('walkUpleft/UL2.png'), pygame.image.load('walkUpleft/UL3.png'), pygame.image.load('walkUpleft/UL4.png')]
walkDownRight = [pygame.image.load('walkDownRight/DR0.png'), pygame.image.load('walkDownRight/DR1.png'), pygame.image.load('walkDownRight/DR2.png'), pygame.image.load('walkDownRight/DR3.png'), pygame.image.load('walkDownRight/DR4.png')]
walkDownLeft = [pygame.image.load('walkDownLeft/DL0.png'), pygame.image.load('walkDownLeft/DL1.png'), pygame.image.load('walkDownLeft/DL2.png'), pygame.image.load('walkDownLeft/DL3.png'), pygame.image.load('walkDownLeft/DL4.png')]

bg = pygame.image.load('background.png')

ui_reload = [pygame.image.load('ui_reload/R0.png'), pygame.image.load('ui_reload/R1.png'), pygame.image.load('ui_reload/R2.png'), pygame.image.load('ui_reload/R3.png'), pygame.image.load('ui_reload/R4.png'), pygame.image.load('ui_reload/R5.png')]
ui = pygame.image.load('UI.png')

char = pygame.image.load('idle/up.png')
charDown = pygame.image.load('idle/down.png')
charLeft = pygame.image.load('idle/left.png')
charRight = pygame.image.load('idle/right.png')

charUpRight = pygame.image.load('idle/upright.png')
charUpLeft = pygame.image.load('idle/upleft.png')
charDownRight = pygame.image.load('idle/downright.png')
charDownLeft = pygame.image.load('idle/downleft.png')

clock = pygame.time.Clock()

#Creates Window
win = pygame.display.set_mode((screenWidth, screenHeight))

#Sets Caption
pygame.display.set_caption("AlphaV0.0.1")

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

#Inventory Class
class inventory(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def search():
        pass

    def draw(self, win):
        pass
        
#Projectile Class
class projectile(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

        self.vel = 15

        self.pos = pygame.Vector2(self.x, self.y)
        self.set_target((0,0))

    def set_target(self, pos):
        self.target = pygame.Vector2(pos)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length < self.vel:
            self.pos = self.target
        elif move_length != 0:
            move.normalize_ip()
            move = move * self.vel
            self.pos += move
            
        #self.rect.topleft = list(int (v) for v in self.pos)

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
    
options = 0

#Redraw Function
def redrawGameWindow():
    win.blit(bg, (0,0))
    ui.draw(win)
    ai.draw(win)
    player.draw(win)

    for bullet in bullets:
        bullet.draw(win)
        bullet.update()
            
        
    pygame.display.update()

#Game Loop
player = player(100, 100, 32, 32)
ui = ui(0, screenHeight - 100, 0)
ai = enemy(250, 250, 32, 32, 100, 50)
shootLoop = 0
ammo = 0
reload = False
bullets = []
run = True
while run:
    clock.tick(15)

    if ammo == 5:
        reload = True

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    #QUIT GAME LOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #ACTIONS CONDITIONALS
    keys = pygame.key.get_pressed()
    mouse_buttons = pygame.mouse.get_pressed()

    #SHOOTING LOOP
    for bullet in bullets:
        if bullet.y - bullet.radius < ai.hitbox[1] + ai.hitbox[3] and bullet.y + bullet.radius > ai.hitbox[1]:
            if bullet.x + bullet.radius > ai.hitbox[0] and bullet.x - bullet.radius < ai.hitbox[0] + ai.hitbox[2]:
                ai.hit()
                bullets.pop(bullets.index(bullet))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        
        '''if bullet.x < screenWidth and bullet.x > 0:
            f = Fraction(abs(rel_y/rel_x))
            if bullet.facing == 2:
                print('pass 2')
                bullet.x += bullet.vel
            elif bullet.facing == 3:
                print('pass 3')
                bullet.x -= bullet.vel
            elif bullet.facing == 4:
                print('pass 4')
                bullet.x -= bullet.vel * f[1]
                bullet.y -= bullet.vel * f[0]
            elif bullet.facing == 6:
                bullet.x += bullet.vel * f[1]
                bullet.y -= bullet.vel * f[0]
        else:
            bullets.pop(bullets.index(bullet))

        if bullet.y < screenHeight - 115 and bullet.y > 0:
            f = Fraction(abs(rel_y/rel_x))
            if bullet.facing == 0:
                bullet.y -= bullet.vel
            elif bullet.facing == 1:
                bullet.y += bullet.vel
            elif bullet.facing == 5:
                bullet.x -= bullet.vel * f[1]
                bullet.y += bullet.vel * f[0]
            elif bullet.facing == 7:
                bullet.x += bullet.vel * f[1]
                bullet.y += bullet.vel * f[0]
        else:
            bullets.pop(bullets.index(bullet))'''

    facing = 0
    if mouse_buttons[0] and shootLoop == 0 and ammo < 5:
        if player.left:
            if player.up:
                facing = 4 #Facing Up Left
            elif player.down:
                facing = 5 #Facing Down Left
            else:
                facing = 3 #Facing Left
        elif player.right:
            if player.up:
                facing = 6 #Facing Up Right
            elif player.down:
                facing = 7 #Facing Down Right
            else:
                facing = 2 #Facing Right
        elif player.down:
            if player.left:
                facing = 5 #Facing Down Left
            elif player.right:
                facing = 7 #Facing Down Right
            else:
                facing = 1 #Facing Down
        elif player.up:
            if player.right:
                facing = 6 #Facing Up Right
            elif player.left:
                facing = 4 #Facing Up Left
            else:
                facing = 0 #Facing Up

        ammo += 1
        shootLoop = 1
            
        if len(bullets) < 5:
            if facing == 3:
                bullets.append(projectile(round(player.x - 18 + player.width //2), round(player.y + player.height //2), 2, (0,0,0)))
                ui.pos = ammo
            elif facing == 2:
                bullets.append(projectile(round(player.x + 18 + player.width //2), round(player.y + player.height //2), 2, (0,0,0)))
                ui.pos = ammo
            elif facing == 1:
                bullets.append(projectile(round(player.x + player.width //2), round(player.y + 18 + player.height //2), 2, (0,0,0)))
                ui.pos = ammo
            elif facing == 0:
                bullets.append(projectile(round(player.x + player.width //2), round(player.y - 18 + player.height //2), 2, (0,0,0)))
                ui.pos = ammo

    #RELOADING LOOP
    if keys[pygame.K_r] and reload:
        for x in range(5):
            ammo -=1
            ui.pos = ammo
        reload = False
        
    #MOVEMENT CONDITIONALS    
    if keys[pygame.K_w] and player.y > player.vel:
        player.y -= player.vel
        player.right = False
        player.left = False
        player.up = True
        player.down = False

        if keys[pygame.K_d] and player.y > player.vel:
            player.x += player.vel
            player.right = True
            player.left = False
        elif keys[pygame.K_a] and player.y > player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False
        
        player.moving = True
    elif keys[pygame.K_s] and player.y < screenHeight - 100 - player.height - player.vel:
        player.y += player.vel
        player.right = False
        player.left = False
        player.up = False
        player.down = True

        if keys[pygame.K_d] and player.x < screenWidth - player.width - player.vel:
            player.x += player.vel
            player.right = True
            player.left = False
        elif keys[pygame.K_a] and player.x > player.vel:
            player.x -= player.vel
            player.left = True
            player.right = False
        
        player.moving = True
    elif keys[pygame.K_a] and player.x > player.vel:
        player.x -= player.vel
        player.right = False
        player.left = True
        player.up = False
        player.down = False

        if keys[pygame.K_w] and player.x > player.vel:
            player.y -= player.vel
            player.up = True
            player.down = False
        elif keys[pygame.K_s] and player.x > player.vel:
            player.y += player.vel
            player.down = True
            player.up = False
        
        player.moving = True
    elif keys[pygame.K_d] and player.x < screenWidth - player.width - player.vel:
        player.x += player.vel
        player.right = True
        player.left = False
        player.up = False
        player.down = False

        if keys[pygame.K_w] and  player.x < screenWidth - player.width - player.vel:
            player.y -= player.vel
            player.up = True
            player.down = False
        elif keys[pygame.K_s] and  player.x < screenWidth - player.width - player.vel:
            player.y += player.vel
            player.down = True
            player.up = False
        
        player.moving = True
    else:
        player.walkCount = 0
        player.moving = False

    #MENU CONDITIONALS
    if keys[pygame.K_ESCAPE]:
        if options == 0:
            print('OPEN OPTIONS')
            options += 1
        else:
            print('CLOSE OPTIONS')
            options -= 1

    redrawGameWindow()

pygame.quit()
