import pygame
import os
import time
import threading
pygame.mixer.init()


FPS = 60
WIDTH, HEIGHT = 1400, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dance Dance Revolution")



ARROW_VEL = 14

class Arrow:
    def __init__(self, image, x_coord, y_coord = HEIGHT):
        self.image = image
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.target = "MISS"

    def move(self):     #move arrows up the screen 
        self.y_coord -= ARROW_VEL
        self.target_zone()
        #if self.y_coord <= -1 * self.image.get_height():        #if arrow is completely off screen
        if self.y_coord <= 10:        #if arrow is completely off screen
            return True 
        else:
            return False
        
    def target_zone(self):  #find how close arrow is to target
        if 8 <= self.y_coord < 22:
            self.target = "PERFECT"
        
        elif 25 <= self.y_coord < 45:
            self.target = "GREAT"

        elif 45 <= self.y_coord < 65:
            self.target = "GOOD"

        elif self.y_coord >= 65:
            self.target = "MISS"


    def draw(self):     #blit image on screen
        WINDOW.blit(self.image, (self.x_coord, self.y_coord))
           
RIGHT_ARROW = Arrow(pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "uparrow.png")), -90), 883) 
UP_ARROW = Arrow(pygame.image.load(os.path.join("Assets", "uparrow.png")), 700) #hits outline at y = 12
DOWN_ARROW = Arrow(pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "uparrow.png")), 180), 527) 
LEFT_ARROW = Arrow(pygame.transform.rotate(pygame.image.load(os.path.join("Assets", "uparrow.png")), 90), 336) 

BACKGROUND = SPACE = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "background.jpg")), (WIDTH, HEIGHT))

active_arrows = []

def draw_window(active_arrows):
    WINDOW.blit(BACKGROUND, (0,0))  
    for arrow in active_arrows:
        arrow.draw()
    pygame.display.update()

def arrow_mapping():
    pygame.mixer.music.load("life_burst.mp3")
    active_arrows.append(LEFT_ARROW)
    time.sleep(0.5)
    active_arrows.append(RIGHT_ARROW)
    time.sleep(0.25)
    pygame.mixer.music.play()
    
    
  


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #close window if user quits
                run = False
        for arrow in active_arrows: #moves arrows and removes arrows that player misses or go off screen
            if arrow.move():
                active_arrows.remove(arrow)
            
                
             
      
        draw_window(active_arrows)      #update window each time loop executes
    pygame.quit()
    


t1 = threading.Thread(target=arrow_mapping).start()
main()
