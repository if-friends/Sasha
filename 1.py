import pygame
pygame.init()

dis_w = 800
dis_h = 800
win = pygame.display.set_mode([dis_w, dis_h])

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([100, 100])
        self.image.fill([255, 255, 255])
        self.rect = self.image.get_rect()
        self.rect.x = x  
        self.rect.y = y 

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.right > dis_w:
            self.rect.right = dis_w
        if self.rect.bottom > dis_h:
            self.rect.bottom = dis_h

player = Player(100, 100)
pl_group = pygame.sprite.Group()
pl_group.add(player)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    pl_group.update()
    win.fill([0,0,0])
    pl_group.draw(win)
    pygame.display.update()