import pygame
import os
import random

class Obstacle():
    def __init__(self):
        self.posx = 310
        self.posy = 0
        self.speed = 2
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "car_blue.png")), (150, 180))
        self.rect = pygame.Rect(self.posx, self.posy, 150, 180)
        self.count = 0

    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect, 2)

        screen.blit(self.img, (self.posx, self.posy))
        self.posy = self.posy + self.speed
        self.rect.y = self.posy
        self.rect.x = self.posx

        if self.posy >= 600:
            self.posy = -180
            self.posx = random.randint(310, 790)
            self.count = self.count + 1
  
