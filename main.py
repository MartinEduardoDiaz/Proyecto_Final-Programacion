import pygame 
import config
from screens import MainScreen



pygame.init()

class Game():
    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((config.WIN_HEIGHT,config.WIN_WIDTH))
        pygame.display.set_caption("Fangs of The Underworld")
        pygame.display.set_icon(config.ICON)
        self.screen_scene = MainScreen(self)
        self.GameOver = False
    
    def change_screen(self, new_screen):
        self.screen_scene = new_screen
    
    def run(self):
        while not self.GameOver:
            self.screen.fill((0,0,0))
            self.screen_scene.draw()
            self.screen_scene.events()
            pygame.display.flip()
        
    

if __name__ == "__main__":
    game  = Game() 
    game.run()