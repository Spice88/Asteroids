import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
AsteroidField.containers = (updatables)
Shot.containers = (shots, updatables, drawables)

asteroidfield = AsteroidField()

def main():

    pygame.init

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    clock = pygame.time.Clock()
    dt = 0

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))

        updatables.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game over!")
                running = False

            for bullet in shots:
                if asteroid.check_collisions(bullet):
                    asteroid.kill()
                    bullet.kill()

        for thing in drawables:
            thing.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000


    



if __name__ == "__main__":
    main()
