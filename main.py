import pygame
import random as r
pygame.init()

width = 800
height = 500

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("Sea Cleaning Life")
clock = pygame.time.Clock()

class block(object):
    def __init__(self,x,y,width,height,colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.hitbox = (x,y,width,width)

    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height))
        #pygame.draw.rect(screen,(250,0,0), self.hitbox,2)

class player(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 55
        self.height = 30
        self.vel = 5
        self.hitbox = (x,y,x+self.width,y+self.height)

    def draw(self):
        pygame.draw.rect(screen,(255, 94, 94),(self.x,self.y,self.width,self.height))

class item(object):
    def __init__(self,x,y,colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.width = 15
        self.height = 15
        self.hitbox = (x,y,x+15,y+15)

    def draw(self):
        pygame.draw.rect(screen,self.colour,(self.x,self.y,self.width,self.height))

dock = block(70,460,140,40,(112, 78, 65))
sand = block(0,0,100,500,(222, 194, 146))
edge = block(100,0,5,500,(115, 91, 52))
blocks = [sand,edge,dock]

def drawAll():
    screen.fill((60, 146, 214))

    for block in blocks:
        block.draw()

    for item in items:
        item.draw()

    # character
    user.draw()

    scoretext = font.render('Score: '+ str(score), True,(33, 69, 97),)
    screen.blit(scoretext, (120,10))

    pygame.display.update()

score = 0
font = pygame.font.SysFont('Poppins',20,True)
user = player(400,250)
running = True
itemTick = 0
items = []
while running:
    clock.tick(30)
    itemTick += 1
    if itemTick == 90:
        itemTick = 0
        items.append(item(r.randint(210,700),r.randint(10,430),(r.randint(0,255),r.randint(0,255),r.randint(0,255))))

    for i in items:
        print(i.hitbox)
        if i.hitbox[0] > user.hitbox[0] and i.hitbox[2] < user.hitbox[2]:
            if i.hitbox[1] > user.hitbox[1] and i.hitbox[3] < user.hitbox[3]:
                print('collide')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and user.y > 0:
        user.y -= user.vel
    if keys[pygame.K_s]:
        if user.x < 210:
            if user.y + user.height < 460:
                user.y += user.vel
        else:
            if user.y + user.height < height:
                user.y += user.vel
    if keys[pygame.K_a]:
        if user.y + user.height > 460:
            if user.x > 210:
                user.x -= user.vel
        else:
            if user.x > 105:
                user.x -= user.vel
    if keys[pygame.K_d] and user.x < width - user.width:
        user.x += user.vel

    drawAll()

pygame.quit()