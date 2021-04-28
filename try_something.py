


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

################################################################################


class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 14), movement_range=(-1, 2)):
        self.size = random.randrange(size_range[0],size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.movement_range = movement_range

    def move(self):
        self.move_x = random.randrange(self.movement_range[0],self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0],self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0: self.x = 0
        elif self.x > self.x_boundary: self.x = self.x_boundary
        
        if self.y < 0: self.y = 0
        elif self.y > self.y_boundary: self.y = self.y_boundary


####################################################################################


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