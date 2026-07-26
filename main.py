import pygame
from car import Car
from street import Street
from obstacle import Obstacle

pygame.init()
pygame.display.set_caption("Car Game")
pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 600))
font = pygame.font.Font(None, 36)


def menu():
    """Returns True to play, False to quit."""
    while True:
        screen.fill("green")
        screen.blit(font.render("1 - Jogar", True, "blue"), (10, 25))
        screen.blit(font.render("2 - Sair",  True, "blue"), (10, 60))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        key = pygame.key.get_pressed()
        if key[pygame.K_1]:
            return True
        if key[pygame.K_2]:
            return False

        clock.tick(60)


def game():
    car = Car()
    street = Street()
    obstacle = Obstacle()
    colliders = 0
    start_time = pygame.time.get_ticks()  # resets every new game
    last_collision_time = 0               # cooldown control

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # quit game entirely

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.posx -= 5
        if keys[pygame.K_RIGHT]:
            car.posx += 5

        # collision with cooldown (1 second between counts)
        now = pygame.time.get_ticks()
        if car.rect.colliderect(obstacle.rect) or \
           car.rect.colliderect(street.rect1) or \
           car.rect.colliderect(street.rect2):
            if now - last_collision_time > 1000:
                colliders += 1
                last_collision_time = now

        # draw
        screen.fill("green")
        street.Draw(screen)
        obstacle.draw(screen)
        car.Draw(screen)

        elapsed = (now - start_time) // 1000
        screen.blit(font.render(f"Fase: {obstacle.count}", True, "blue"), (10, 25))
        screen.blit(font.render(f"Tempo: {elapsed}s",      True, "blue"), (10, 60))
        screen.blit(font.render(f"Danos: {colliders}",     True, "blue"), (10, 90))

        pygame.display.update()
        clock.tick(60)


# --- main loop ---
while True:
    if not menu():
        break
    if not game():
        break

pygame.quit()