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
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.collected = 0
        self.cash = 0
        self.nearshop = 0
        self.lvlcapacity = 1
        self.maxcollect = (self.lvlcapacity ** 2) * 5
        self.lvlprice = 1
        self.price = self.lvlprice
        self.lvlspd = 1
        self.spd = 5 * self.lvlspd

    def draw(self):

        pygame.draw.rect(screen,(255, 94, 94),(self.x,self.y,self.width,self.height))
        pygame.draw.rect(screen,(255,255,255),(self.x+5,self.y-15,self.width-10,5))
        pygame.draw.rect(screen, (0, 255, 0), (self.x + 5, self.y - 15, (self.width - 10) * (self.collected / self.maxcollect), 5))

    def drawHitbox(self):
        pygame.draw.rect(screen,(255,0,0),self.hitbox)

    def updateHitbox(self):
        self.hitbox = (self.x,self.y,self.x+self.width,self.y+self.height)

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
    #user.drawHitbox()

    if user.nearshop == 1:
        nearshoptext = font.render('Press \'E\' to open shop.', True, (0,0,0),(255,255,255))
        screen.blit(nearshoptext, (300, 400))

    scoretext = font.render('Cash: $'+ str(user.cash), True,(33, 69, 97))
    screen.blit(scoretext, (120,10))

    pygame.display.update()

font = pygame.font.SysFont('Poppins',20,True)
user = player(400,250)
running = True
itemTick = 0
items = []
openShop = -1
while running:
    clock.tick(30)

    itemTick += 1
    if itemTick % 90 == 0:
        items.append(item(r.randint(210,700),r.randint(10,430),(r.randint(0,255),r.randint(0,255),r.randint(0,255))))

    for i in items:
        #print(i.hitbox, user.hitbox)
        if (i.hitbox[0] >= user.hitbox[2]) or (i.hitbox[2] <= user.hitbox[0]) or (i.hitbox[1] >= user.hitbox[3]) or (i.hitbox[3] <= user.hitbox[1]):
            pass
        else:
            if user.collected < user.maxcollect:
                user.collected += 1
                items.pop(items.index(i))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and user.y > 0 and openShop == -1:
        user.y -= user.spd
    if keys[pygame.K_s] and openShop == -1:
        if user.x < 210:
            if user.y + user.height < 460:
                user.y += user.spd
        else:
            if user.y + user.height < height:
                user.y += user.spd
    if keys[pygame.K_a] and openShop == -1:
        if user.y + user.height > 460:
            if user.x > 210:
                user.x -= user.spd
        else:
            if user.x > 105:
                user.x -= user.spd
    if keys[pygame.K_d] and user.x < width - user.width and openShop == -1:
        user.x += user.spd
    if keys[pygame.K_e] and user.nearshop == 1:
        openShop = 1
        print('open shop')
    if keys[pygame.K_ESCAPE]:
        openShop = -1
        print('close shop')


    if user.x < 230 and user.y + user.height > 445:
        user.nearshop = 1
        user.cash += user.collected * user.price
        user.collected = 0
    else:
        user.nearshop = 0



    user.updateHitbox()
    drawAll()

pygame.quit()