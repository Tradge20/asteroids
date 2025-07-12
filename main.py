from constants import *
from player import Player
from circleshape import CircleShape
import pygame



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    
    
    clock = pygame.time.Clock()
    dt = 0
    
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        dt = clock.tick(60) / 1000.0
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)   
        for sprite in drawables:
            sprite.draw(screen)
            
        
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
