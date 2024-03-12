import pygame
import os
pygame.mixer.init()


FPS = 60
WIDTH, HEIGHT = 1400, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dance Dance Revolution")


RED = (250, 0, 0)

ARROW_VEL = 2

class Arrow:
    def __init__(self, image, x_coord, y_coord = HEIGHT):
        self.image = image
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.target = "MISS"

    def move(self):     #move arrows up the screen 
        self.y_coord -= ARROW_VEL
        if self.y_coord <= -1 * self.image.get_height():        #if arrow is completely off screen
            return True 
        else:
            return False
        
    def target_zone(self):  #find how close arrow is to target
        if self.y_coord <= 9 and self.y_coord >= 21:
            self.target = "PERFECT"


    def draw(self):     #blit image on screen
        WINDOW.blit(self.image, (self.x_coord, self.y_coord))
            
RIGHT_ARROW = Arrow(pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "uparrow.png")), -90), 883) 
UP_ARROW = Arrow(pygame.image.load(os.path.join("Assets", "uparrow.png")), 700) #hits outline at y = 12
DOWN_ARROW = Arrow(pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "uparrow.png")), 180), 525) 
LEFT_ARROW = Arrow(pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "uparrow.png")), 90), 336) 

BACKGROUND = SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.jpg")), (WIDTH, HEIGHT))

def draw_window(active_arrows):
    WINDOW.blit(BACKGROUND, (0,0))  
    for arrow in active_arrows:
        arrow.draw()
    LEFT_ARROW.y_coord = 21
    LEFT_ARROW.draw()
    pygame.display.update()



def main():
    active_arrows = [RIGHT_ARROW]
    clock = pygame.time.Clock()
    run = True
    pygame.mixer.music.load("life_burst.mp3")
    #pygame.mixer.music.play()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close window if user quits
                run = False
        for arrow in active_arrows: #remove arrows that player misses
            arrow.move() 
             
      
        draw_window(active_arrows)      #update window each time loop executes
    pygame.quit()
    


main()