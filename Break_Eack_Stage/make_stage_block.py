import pygame
import sys
from pygame.locals import *


pygame.init()
mainClock = pygame.time.Clock()

# basic setting
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Make Map Tool')

# font
basicFont = pygame.font.SysFont(None, 48)
nextFont = pygame.font.SysFont(None, 15)

# R, G, B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (229, 57, 53)
YELLOW = (253, 216, 53)
GREEN = (124, 176, 66)
BLUE = (3, 155, 229)


BLOCK_SIZE = 20
KEYS = {pygame.K_w: 'up', pygame.K_s: 'down', pygame.K_a: 'left_', pygame.K_d: 'right', pygame.K_r: 'stop'}


# save block
def make_move_block(axis_x, axis_y, color, block_direction):
    block1 = {'left': axis_x, 'top': axis_y, 'color': color, 'dir': block_direction}
    list_movblock.append(block1)


def make_stop_block(axis_x, axis_y, color):
    block2 = {'left': axis_x, 'top': axis_y, 'color': color}
    list_block.append(block2)


list_movblock = []
list_block = []
block_direction = 'up'

# outline
for i in range(30):
    gg = {'left': i * BLOCK_SIZE, 'top': 0, 'color': BLACK}
    gh = {'left': i * BLOCK_SIZE, 'top': 380, 'color': BLACK}
    list_block.append(gg)
    list_block.append(gh)

for i in range(20):
    gg = {'left': 0, 'top': i * BLOCK_SIZE, 'color': BLACK}
    gh = {'left': 580, 'top': i * BLOCK_SIZE, 'color': BLACK}
    list_block.append(gg)
    list_block.append(gh)


# file
# please input your computer path
file_mov = open(
    "C:\\Users\\(###)\\STAGE6_move",
    'w', encoding='utf-8')
file_stop = open(
    "C:\\Users\\(###)\\STAGE6_stop",
    'w', encoding='utf-8')


# Start #
while True:
    windowSurface.fill(WHITE)

    dir_text = nextFont.render('W- up, RED/ S- down, BLUE/ A- left_, YELLOW/ D- right, GREEN', True, BLACK, WHITE)
    dir_text_Rect = dir_text.get_rect()
    dir_text_Rect.left = 260
    dir_text_Rect.top = 30
    windowSurface.blit(dir_text, dir_text_Rect)


    for event in pygame.event.get():

        # quit and saving file
        if event.type == QUIT:
            data1 = "{}".format(list_movblock)
            file_mov.write(data1)
            data2 = "{}".format(list_block)
            file_stop.write(data2)
            file_mov.close()
            file_stop.close()

            pygame.quit()
            sys.exit()

        # make block
        if event.type == pygame.KEYDOWN:
            if event.key in KEYS:
                block_direction = KEYS[event.key]

            # delete move block by pressing key C
            if event.key == pygame.K_c:
                last_block = list_movblock[-1]
                list_movblock.remove(last_block)

            # delete stop block by pressing key V
            if event.key == pygame.K_v:
                last_block = list_block[-1]
                list_block.remove(last_block)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                # make move block
                if block_direction == 'up':
                    mouse_x, mouse_y = event.pos
                    ke_x = (mouse_x // BLOCK_SIZE) * BLOCK_SIZE
                    ke_y = (mouse_y // BLOCK_SIZE) * BLOCK_SIZE
                    make_move_block(ke_x, ke_y, RED, block_direction)

                elif block_direction == 'down':
                    mouse_x, mouse_y = event.pos
                    ke_x = (mouse_x // BLOCK_SIZE) * BLOCK_SIZE
                    ke_y = (mouse_y // BLOCK_SIZE) * BLOCK_SIZE
                    make_move_block(ke_x, ke_y, BLUE, block_direction)

                elif block_direction == 'left_':
                    mouse_x, mouse_y = event.pos
                    ke_x = (mouse_x // BLOCK_SIZE) * BLOCK_SIZE
                    ke_y = (mouse_y // BLOCK_SIZE) * BLOCK_SIZE
                    make_move_block(ke_x, ke_y, YELLOW, block_direction)

                elif block_direction == 'right':
                    mouse_x, mouse_y = event.pos
                    ke_x = (mouse_x // BLOCK_SIZE) * BLOCK_SIZE
                    ke_y = (mouse_y // BLOCK_SIZE) * BLOCK_SIZE
                    make_move_block(ke_x, ke_y, GREEN, block_direction)

                # make stop block
                elif block_direction == 'stop':
                    mouse_x, mouse_y = event.pos
                    ke_x = (mouse_x // BLOCK_SIZE) * BLOCK_SIZE
                    ke_y = (mouse_y // BLOCK_SIZE) * BLOCK_SIZE
                    make_stop_block(ke_x, ke_y, BLACK)

    # display
    for j in list_movblock:
        a = j['left']
        b = j['top']
        pygame.draw.rect(windowSurface, j['color'], (a, b, BLOCK_SIZE, BLOCK_SIZE))

    for j in list_block:
        a = j['left']
        b = j['top']
        pygame.draw.rect(windowSurface, j['color'], (a, b, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.update()
    mainClock.tick(5)