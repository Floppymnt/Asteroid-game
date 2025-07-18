import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    
    pass_fail = pygame.init()
    print(f"pygame initialized with {pass_fail[0]} modules loaded successfully and {pass_fail[1]} modules failed to load.")
    
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    print(f"Initialized screen with:\nwidth: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    
    pygame.display.set_caption("Asteroids Game")


    while True:

        # Handle events
        for event in pygame.event.get():


            if event.type == pygame.QUIT: #quit the game
                print("USER EXIT EVENT: closing with exit code 0")
                # pygame.quit()
                return



        screen.fill("black")
        pygame.display.flip()




if __name__ == "__main__":
    main()
