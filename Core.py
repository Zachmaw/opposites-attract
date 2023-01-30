version = "Vinfdev"
if __name__ == "__main__":
    print(version)

# pygame template - skeleton for a new pygame project
import pygame
import random# Cosmic radiation, hehehe


cellSize = 32
gridWidth = 10
gridHeight = 10
WIDTH = cellSize * gridWidth
HEIGHT = cellSize * gridHeight
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Opposites-Attract")
clock = pygame.time.Clock()

class Particle(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.radius = 8
        self.image = pygame.Surface((self.radius*2, self.radius*2))
        
        pygame.draw.circle(self.image, WHITE, self.rect.center, self.radius)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.center = pos
        self.speedx = 0
        self.speedy = 0
#     def update(self):

# class Mob(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image_orig = random.choice(mob_images)
#         self.image_orig.set_colorkey(BLACK)
#         self.image = self.image_orig.copy()
#         self.rect = self.image.get_rect()
#         self.radius = int(self.rect.width * 0.85 / 2)
#         # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
#         self.rect.x = random.randrange(WIDTH - self.rect.width)
#         self.rect.y = random.randrange(-150, -40)
#         self.speedy = random.randrange(2, 5)
#         self.speedx = random.randrange(-1, 2)
#         self.rot = 0
#         self.rot_speed = random.randrange(-8, 9)
#         self.last_update = pygame.time.get_ticks()


    def update(self, cols):
        if self.rect.right > WIDTH - 4:
            self.rect.right = WIDTH - 4
        if self.rect.left < 4:
            self.rect.left = 4
        
        # log prevSpeed
        self.prevSpeedx = self.speedx
        self.prevSpeedy = self.speedy
        self.speedx = 0
        self.speedy = 0
        # calculate new vectors from colisions
        
        # adjust pos
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # check for colisions
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.bounce("y")

#     def update(self):
#         self.rotate()
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy
#         if self.rect.top > HEIGHT +10 or self.rect.right < 0 or self.rect.left > WIDTH:# if goes off screen
#             self.rect.x = random.randrange(WIDTH - self.rect.width)
#             self.rect.y = random.randrange(-150, 0 - self.rect.height)
#             self.speedy = 1

    def bounce(self, axis:str):
        if axis == "x":
            self.speedx *= -1
        elif axis == "y":
            self.speedy *= -1


background = pygame.Surface(screen.get_rect())
background.fill(BLACK)
for x in range(0, 8, 2):
    for y in range(0, 8, 2):
        pygame.draw.rect(background, (0,0,0), (x*size, y*size, size, size))


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
# player = Player()
# all_sprites.add(player)
# for i in range(8):
    # m = Mob()
    # all_sprites.add(m)
    # mobs.add(m)

# Game loop
running = True
while running:
    clock.tick(FPS)# keep loop running at the right speed
    for event in pygame.event.get():# Process input (events)
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                # player.shoot()
                pass

    all_sprites.update()

    # check bullet hit mob
    # hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    # for hit in hits:
    #     m = Mob()
    #     all_sprites.add(m)
    #     mobs.add(m)

    #check if mob hit player
    # hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    # if hits:
    #     running = False

    # Draw / render
    screen.fill(BLACK)
    # screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()