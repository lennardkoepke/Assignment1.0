import pygame
import random

SCREEN_WIDTH = 2500
SCREEN_HEIGHT = 300

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Animation with Random Background")

background_files = [
    "background1.jpg.webp",
    "background2.jped.jpe",
    "Background3.jpg.webp"

]

background_image = pygame.image.load(random.choice(background_files)).convert()
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

img = pygame.image.load("E30.png").convert_alpha()

img = pygame.transform.scale(img, (250,200))



class Drive:
    def __init__(self):
        self.speed =55
        self.x = 100
        self.y = 100

    def forward(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.x += self.speed
            if self.x > SCREEN_WIDTH:
                self.x = -150

            screen.blit(background_image, (0, 0))
            screen.blit(img, (self.x, self.y))
            pygame.display.flip()

        pygame.quit()


    def reverse(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(self.speed)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.x -= self.speed
            if self.x < 0:
                self.x = 2500

            screen.blit(background_image, (0, 0))
            screen.blit(img, (self.x, self.y))
            pygame.display.flip()




Drive().reverse()
