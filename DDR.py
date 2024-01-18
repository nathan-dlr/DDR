import pygame
import os
pygame.mixer.init()

FPS = 60
WIDTH, HEIGHT = 1400, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dance Dance Revolution")


RED = (250, 0, 0)

ARROW_VEL = 5

class Arrow:
    def __init__(self, image, x_coord, y_coord = HEIGHT):
        self.image = image
        self.x_coord = x_coord
        self.y_coord = y_coord

    def move(self):     #move arrows up the screen 
        self.y_coord -= ARROW_VEL
        if self.y_coord <= -1 * self.image.get_height():        #if arrow is completely off screen
            return True 
        else:
            return False

    def draw(self):     #blit image on screen
        WINDOW.blit(self.image, (self.x_coord, self.y_coord))
            

LEFT_ARROW = Arrow(pygame.image.load(os.path.join("Assets", "leftarrow.png")), 500) 



def draw_window(active_arrows):
    WINDOW.fill(RED)  
    for arrow in active_arrows:
        arrow.draw()
    pygame.display.update()



def main():
    active_arrows = [LEFT_ARROW]
    clock = pygame.time.Clock()
    run = True
    left = True
    #pygame.mixer.music.load("life_burst.mp3")
    #pygame.mixer.music.play()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       #close window if user quits
                run = False
        for arrow in active_arrows:     #remove arrows that player misses
            miss = arrow.move() 
            if  miss == True:
                active_arrows.remove(arrow)     

        draw_window(active_arrows)      #update window each time loop executes
    pygame.quit()
    


main()