import pygame
import os

class Street():
    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "Road2.png")), (800, 600))
        self.x = 200
        self.y = 0
        self.speed = 5
        self.rect1 = pygame.Rect(self.x, 0, 109, 600)
        self.rect2 = pygame.Rect(self.x + 691, 0, 109, 600)

    def Draw(self, screen):
        screen.blit(self.img, (self.x, self.y-600))
        screen.blit(self.img, (self.x, self.y))
        self.y = self.y + self.speed
        if self.y == 600:
            self.y = 0

        pygame.draw.rect(screen, "red", self.rect1, 2)
        pygame.draw.rect(screen, "red", self.rect2, 2)