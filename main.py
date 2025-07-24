import pygame
from constants import *
from player import player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    
    pass_fail = pygame.init()
    print(f"pygame initialized with {pass_fail[0]} modules loaded successfully and {pass_fail[1]} modules failed to load.")
    

    #creat a clock object for fps cap
    clock = pygame.time.Clock()
    dt = 0
    print("Clock initialized.")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    print(f"Initialized screen with:\nwidth: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    
    pygame.display.set_caption("Asteroids Game")


    
    print(f"Player initialized")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.containers  = (updatable, drawable)
    
    asteroid_field = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroid_field)
    
    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (updatable,drawable,shots)

    print("Sprite groups initialized.")

    obstacles = AsteroidField()
    player_sprite = player(SCREEN_WIDTH /2, SCREEN_HEIGHT / 2,PLAYER_RADIUS)



    while True:

        # Handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT: #quit the game
                print("USER EXIT EVENT: exiting game loop.")
                # pygame.quit()
                return

            #pass    

        screen.fill("black") 
        for sprite in drawable:
            sprite.draw(screen) 
        # player_sprite.draw(screen)
        pygame.display.flip()

        dt =  clock.tick(FPS) / 1000.0 # cap the frame rate to FPS and get delta time
        updatable.update(dt)

        for asteroid in asteroid_field:
            
            if player_sprite.collide(asteroid):
                print("Collision detected between player and asteroid.\nGAME OVER!")
                return  # Exit the game loop on collision

            #pass


        


       
        




if __name__ == "__main__":
    main()
