# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock=pygame.time.Clock()
    dt=0
    
    #adding groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots=pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    asteroid_field=AsteroidField()

    player=Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for updatable_item in updatable:
            updatable_item.update(dt)
        
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for sh in shots:
                if asteroid.check_collision(sh):
                    asteroid.split()
                    sh.kill()
       
       
        screen.fill((0,0,0))
        for drawable_item in drawable:
            drawable_item.draw(screen)
    
        pygame.display.flip()
        dt=clock.tick(60)/1000


if __name__ == "__main__":
    main()