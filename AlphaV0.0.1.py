import pygame
import socket, asyncore
from Player import player
from Projectile import projectile
from AI import enemy
from UI import ui

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
bg = pygame.image.load('background.png')

clock = pygame.time.Clock()

#Creates Window
win = pygame.display.set_mode((screenWidth, screenHeight))

#Sets Caption
pygame.display.set_caption("AlphaV0.0.1")


#Inventory Class
class inventory(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def search():
        pass

    def draw(self, win):
        pass
    
#Redraw Function
def redrawGameWindow():
    win.blit(bg, (0,0))
    ui.draw(win)
    ai.draw(win)
    player.draw(win)

    for bullet in bullets:
        bullet.draw(win)
            
        
    pygame.display.update()

#Game Loop
player = player(100, 100, 32, 32)
ui = ui(0, screenHeight - 100, 0)
ai = enemy(250, 250, 32, 32, 100, 50)
shootLoop = 0
ammo = 0
options = 0
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

        #OLD MECHANISM FOR SHOOTING
        if bullet.x < screenWidth and bullet.x > 0:
            if bullet.facing == 2:
                bullet.x += bullet.vel
            elif bullet.facing == 3:
                bullet.x -= bullet.vel
            elif bullet.facing == 4:
                bullet.x -= bullet.vel
                bullet.y -= bullet.vel
            elif bullet.facing == 6:
                bullet.x += bullet.vel
                bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

        if bullet.y < screenHeight - 100 - bullet.vel and bullet.y > 0:
            if bullet.facing == 0:
                bullet.y -= bullet.vel
            elif bullet.facing == 1:
                bullet.y += bullet.vel
            elif bullet.facing == 4:
                bullet.x -= bullet.vel
                #bullet.y -= bullet.vel
            elif bullet.facing == 6:
                bullet.x += bullet.vel
                bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    facing = 0
    if keys[pygame.K_SPACE] and shootLoop == 0 and ammo < 5:
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
                bullets.append(projectile(round(player.x - 18 + player.width //2), round(player.y + player.height //2), 2, (0,0,0), facing))
                ui.pos = ammo
            elif facing == 2:
                bullets.append(projectile(round(player.x + 18 + player.width //2), round(player.y + player.height //2), 2, (0,0,0), facing))
                ui.pos = ammo
            elif facing == 1:
                bullets.append(projectile(round(player.x + player.width //2), round(player.y + 18 + player.height //2), 2, (0,0,0), facing))
                ui.pos = ammo
            elif facing == 0:
                bullets.append(projectile(round(player.x + player.width //2), round(player.y - 18 + player.height //2), 2, (0,0,0), facing))
                ui.pos = ammo
            elif facing == 4:
                bullets.append(projectile(round(player.x - 18 + player.width //2), round(player.y - 18 + player.height //2), 2, (0,0,0), facing))
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

        if keys[pygame.K_d] and player.x < screenWidth - player.width - player.vel and player.y < player.vel:
            player.x += player.vel
            player.right = True
            player.left = False
        elif keys[pygame.K_a] and player.x > player.vel and player.y > player.vel:
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

        if keys[pygame.K_w] and player.x > player.vel and player.y > 0:
            print('pass')
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

        if keys[pygame.K_w] and player.y > 0 and player.x < screenWidth - player.width - player.vel:
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

    redrawGameWindow()

pygame.quit()
