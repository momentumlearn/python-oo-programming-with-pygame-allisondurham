#Put your Python code in here.


import pygame
import random
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
    

def main():
    color1_blobs = dict(enumerate([Blob(COLOR1, WIDTH, HEIGHT) for i in range(STARTING_COLOR1_BLOBS)]))
    color2_blobs = dict(enumerate([Blob(COLOR2, WIDTH, HEIGHT) for i in range(STARTING_COLOR2_BLOBS)]))
    color3_blobs = dict(enumerate([Blob(COLOR3, WIDTH, HEIGHT) for i in range(STARTING_COLOR3_BLOBS)]))
    color4_blobs = dict(enumerate([Blob(COLOR4, WIDTH, HEIGHT) for i in range(STARTING_COLOR4_BLOBS)]))
    color5_blobs = dict(enumerate([Blob(COLOR5, WIDTH, HEIGHT) for i in range(STARTING_COLOR5_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_environment([color1_blobs, color2_blobs, color3_blobs, color4_blobs, color5_blobs])
        clock.tick(60)

if __name__ == '__main__':
    while True:    

        main()