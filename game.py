#Put your Python code in here.


import pygame
import random
import scratch
from random import randrange
from blob import Blob

STARTING_COLOR1_BLOBS = 20
STARTING_COLOR2_BLOBS = 20
STARTING_COLOR3_BLOBS = 20
STARTING_COLOR4_BLOBS = 20
STARTING_COLOR5_BLOBS = 20

WIDTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (204, 255, 255)
COLOR1 = (51, 153, 255)     #blue
COLOR2 = (204, 102, 255)    #purple
COLOR3 = (51, 204, 51)      #green
COLOR4 = (255, 80, 80)      #coral
COLOR5 = (255, 204, 0)      #yellow

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

def draw_environment(blob_list):
    game_display.fill(BACKGROUND_COLOR)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()

    pygame.display.update()
    

#generate random colors
def generate_color(self):
    r = random.randrange(255)
    g = random.randrange(225)
    b = random.randrange(225)
    return (r, g, b)

#def color_list(blob)
    #generate list of 5 
#loop 



def main():
    color_list = scratch.color_list()
    for color in color_list:
        color1_blobs = dict(enumerate([Blob(color, WIDTH, HEIGHT) for i in range(STARTING_COLOR1_BLOBS)]))
    # color2_blobs = dict(enumerate([Blob(color, WIDTH, HEIGHT) for i in range(STARTING_COLOR2_BLOBS)]))
    # color3_blobs = dict(enumerate([Blob(color, HEIGHT) for i in range(STARTING_COLOR3_BLOBS)]))
    # color4_blobs = dict(enumerate([Blob(WIDTH, HEIGHT) for i in range(STARTING_COLOR4_BLOBS)]))
    # color5_blobs = dict(enumerate([Blob(WIDTH, HEIGHT) for i in range(STARTING_COLOR5_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([color1_blobs]) 
        clock.tick(60)



        

if __name__ == '__main__':
    while True:    

        main()

