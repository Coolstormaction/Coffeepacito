import pygame as py
import sys
import os 

class EndScreen:
    py.init()
    def __init__(self, highscore, point, width, height):
        self.DIMEN = (width, height)
        self.highscore = highscore
        self.width = width
        self.height = height
        self.point = point
        
    def run(self):
        DIMEN = self.DIMEN
        WIDTH = self.width 
        HEIGHT = self.height 
        high_score = self.highscore
        point = self.point 
        endscreen = py.display.set_mode(DIMEN)
        running = True
        endpic = py.image.load('assets/endscreen.png').convert_alpha()
        py.display.set_caption("Game over")
        font = py.font.Font('assets/vampire-wars.ttf', 32)

        while running:
            endscreen.blit(endpic, (0, 0))
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    sys.exit()

                if event.type == py.KEYDOWN:  
                    if event.key == py.K_SPACE: os.system("make")

            py.init()
            gameover = font.render(f'Game over', True, (0, 0, 0))
            highscoretext = font.render(f'Highscore - {high_score}', True, (0, 0, 0))
            scoretext = font.render(f"Score - {point}", True, (0, 0, 0))
            gameoverrect = gameover.get_rect()
            gameoverrect.center = (WIDTH // 2, 200)
            highscoretextrect = highscoretext.get_rect()
            highscoretextrect.center = (WIDTH // 2, HEIGHT // 2)
            scoretextrect = scoretext.get_rect()
            scoretextrect.center = (WIDTH // 2, 400)
            endscreen.blit(gameover, gameoverrect)
            endscreen.blit(highscoretext, highscoretextrect)
            endscreen.blit(scoretext, scoretextrect)
            py.display.update()























































































































































































































































































































































































































































































































































































































































































#you found the easter egg
#uwU