import pygame
import os

class Car():
    def __init__(self):
        self.x = 150
        self.y = 180
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "car.png")), (self.x, self.y))
        self.posx = 400
        self.posy = 400
        self.colortop = "blue"
        self.colorleft = "blue"
        self.colorright = "blue"
        self.count = 0
        self.rect = pygame.Rect(self.posx, self.posy, self.x, self.y)
     
    def Draw(self, screen):
        self.colortop = screen.get_at((int(self.posx+75), int(self.posy-130)))
        self.colorleft = screen.get_at((int(self.posx-10), int(self.posy+90)))
        self.colorright = screen.get_at((int(self.posx+160), int(self.posy+90)))

        pygame.draw.line(screen, "green", (self.posx+75, self.posy), (self.posx+75, self.posy-130), 3)
        pygame.draw.circle(screen, self.colortop, (self.posx+75, self.posy-130), 8)

        pygame.draw.line(screen, "green", (self.posx-10, self.posy+90), (self.posx+160, self.posy+90), 3)
        pygame.draw.circle(screen, self.colorright, (self.posx+160, self.posy+90), 8)
        pygame.draw.circle(screen, self.colorleft, (self.posx-5, self.posy+90), 8)
        
        screen.blit(self.img, (self.posx, self.posy))

        pygame.draw.rect(screen, "red", self.rect, 2)
        self.rect.x = self.posx

        if self.colortop == (255,0,0,255) or self.colorleft == (255,0,0,255) or self.colorright == (255,0,0,255):
            self.count = self.count + 1
            print(f"Sensor detectado: {self.count}")