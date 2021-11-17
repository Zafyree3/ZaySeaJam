import pygame
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

    def draw(self):
        pygame.draw.rect(screen,(255, 94, 94),(self.x,self.y,self.width,self.height))


dock = block(70,460,140,40,(112, 78, 65))
sand = block(0,0,100,500,(222, 194, 146))
edge = block(100,0,5,500,(115, 91, 52))
blocks = [sand,edge,dock]

def drawAll():
    screen.fill((32, 93, 179))

    for block in blocks:
        block.draw()

    # character
    user.draw()

    pygame.display.update()

user = player(400,250)
running = True
while running:
    clock.tick(30)

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