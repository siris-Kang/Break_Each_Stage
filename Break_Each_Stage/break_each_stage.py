import pygame
import sys
import time
import random
from pygame.locals import *


# view time score
def time_score():
    now_time = time.time() - start_time
    time_text = nextFont.render('TIME : %.0f' % now_time, True, BLACK, WHITE)
    time_textRect = time_text.get_rect()

    time_textRect.left = 500
    time_textRect.top = 25
    windowSurface.blit(time_text, time_textRect)
    Time = now_time
    return Time

# game over
def game_over():
    finish_text = basicFont.render('GAME OVER', True, WHITE, RED)
    finish_textRect = finish_text.get_rect()

    finish_textRect.centerx = windowSurface.get_rect().centerx
    finish_textRect.centery = windowSurface.get_rect().centery

    windowSurface.blit(finish_text, finish_textRect)

# game complete
def game_complete():
    finish_text = basicFont.render('STAGE CLEAR', True, WHITE, GREEN)
    finish_textRect = finish_text.get_rect()

    finish_textRect.centerx = windowSurface.get_rect().centerx
    finish_textRect.centery = windowSurface.get_rect().centery

    finish_score_text = nextFont.render('You Took %.0f Seconds!!' % Time, True, GRAY, WHITE)
    finish_scoreRect = finish_score_text.get_rect()

    finish_scoreRect.centerx = windowSurface.get_rect().centerx
    finish_scoreRect.top = 230

    windowSurface.blit(finish_text, finish_textRect)
    windowSurface.blit(finish_score_text, finish_scoreRect)

# draw block at screen
def draw_block(windowSurface, color, position):
    block = pygame.Rect(position[1], position[0],BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.rect(windowSurface, color, block)


# draw button at screen
def button(msg, color, a, b, c, d):
    pygame.draw.rect(windowSurface, color, (a, b, c, d))
    textSurf = nextFont.render(msg, True, BLACK)
    textRect = textSurf.get_rect()

    textRect.center = (a + (c/2), b + (d/2))
    windowSurface.blit(textSurf, textRect)

# change to next stage
def next_stage(a, b, c, d):
    global flag
    global start
    global gamecomplete
    global start_time
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if a < mouse[0] < a + c and b < mouse[1] < b + d and click[0] == 1:
        flag += 1
        windowSurface.fill(WHITE)
        start_time = time.time()
        start = 'go'
        gamecomplete = False

# restart the stage when game over
def restart(a, b, c, d):
    global start
    global gameover
    global start_time
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if a < mouse[0] < a + c and b < mouse[1] < b + d and click[0] == 1:
        windowSurface.fill(WHITE)
        gameover = False
        start = 'go'
        start_time = time.time()

# open file
def action(flag):
    if flag == 1:
        file_mov = open("STAGE1_move", 'r', encoding = 'utf-8')
        file_stop = open("STAGE1_stop", 'r', encoding = 'utf-8')
        return file_mov, file_stop

    if flag == 2:
        file_mov = open("STAGE2_move", 'r', encoding = 'utf-8')
        file_stop = open("STAGE2_stop", 'r', encoding = 'utf-8')
        return file_mov, file_stop

    if flag == 3:
        file_mov = open("STAGE3_move", 'r', encoding = 'utf-8')
        file_stop = open("STAGE3_stop", 'r', encoding = 'utf-8')
        return file_mov, file_stop

    if flag == 4:
        file_mov = open("STAGE4_move", 'r', encoding = 'utf-8')
        file_stop = open("STAGE4_stop", 'r', encoding = 'utf-8')
        return file_mov, file_stop

    if flag == 5:
        file_mov = open("STAGE5_move", 'r', encoding = 'utf-8')
        file_stop = open("STAGE5_stop", 'r', encoding = 'utf-8')
        return file_mov, file_stop

# draw game main screen
def story_1():
    global story1
    global story2

    windowSurface.blit(storyimg1, (0,0))
    button("GO!", SKYBLUE1, 400, 280, 80, 30)
    mouse = pygame.mouse.get_pos()
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 400 < mouse[0] < 400 + 80 and 280 < mouse[1] < 280 + 30:
            story1 = False
            story2 = True
    pygame.display.update()
    mainClock.tick(10)

# draw how to play screen
def story_2():
    global story2
    global game_go

    windowSurface.blit(storyimg2, (0,0))
    button("GAME START", SKYBLUE1, 250, 270, 120, 30)
    mouse = pygame.mouse.get_pos()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if 250 < mouse[0] < 250 + 120 and 270 < mouse[1] < 270 + 30:
            story2 = False
            game_go = 1
    pygame.display.update()
    mainClock.tick(10)


pygame.init()
mainClock = pygame.time.Clock()

# basic setting
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Break Each Stage')

# font
basicFont = pygame.font.SysFont(None, 48)
nextFont = pygame.font.SysFont(None, 24)

# R, G, B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (3, 155, 229)
GREEN = (124, 176, 66)
RED = (229, 57, 53)
YELLOW = (253, 216, 53)
GRAY = (100, 100, 100)
SKYBLUE1 = (100, 181, 246)
SKYBLUE2 = (232, 234, 246)
PINK1 = (240, 98, 146)

# set image
storyimg1 = pygame.image.load("first_image.jpg")
storyimg1 = pygame.transform.scale(storyimg1, (600, 400))
storyimg2 = pygame.image.load("second_image.jpg")
storyimg2 = pygame.transform.scale(storyimg2, (600, 400))

# init time score
Time = 0

# Key setting
KEY = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left_', pygame.K_RIGHT: 'right'}

# init main block(we move it)
main_block_position = [40, 40]

BLOCK_SIZE = 20
MOVESPEED = int(BLOCK_SIZE/2)

main_block_direction = 'right'

# game value
gamecomplete = False
gameover = False

flag = 1
start = 'go'
game_go  = 0

story1 = True
story2 = False


# Start #
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(WHITE)

    # display game start screen
    if story1 == True:
        story_1()
    if story2 == True:
        story_2()
        start_time = time.time()
    
    # read file
    if game_go == 1:
        if start == 'go':
            main_block_position = [40, 40]
            windowSurface.fill(WHITE)

            file_mov, file_stop = action(flag)
            stage1_mov = file_mov.read()
            stage1 = file_stop.read()
            list_movblock = eval(stage1_mov)
            list_block = eval(stage1)
            file_mov.close()
            file_stop.close()
            start = 'stop'

        windowSurface.fill(WHITE)
        
        # set game start, end spot
        pygame.draw.rect(windowSurface, SKYBLUE2, (20, 20, 40, 40))
        pygame.draw.rect(windowSurface, SKYBLUE2, (540, 340, 40, 40))

        main_block_rect = (main_block_position[1], main_block_position[0], BLOCK_SIZE, BLOCK_SIZE)

        # GAME COMPLETE
        if main_block_rect == (560, 360, 20, 20) or main_block_rect == (540, 360, 20, 20) or main_block_rect == (560, 340, 20, 20) or main_block_rect == (540, 340, 20, 20):
            gamecomplete = True
        
        # GAME OVER when main block overlap
        for b in list_movblock:
            movblock_rect = (b['left'], b['top'], BLOCK_SIZE, BLOCK_SIZE)
            if main_block_rect == movblock_rect:
                gameover = True

        for c in list_block:
            block_rect = (c['left'], c['top'], BLOCK_SIZE, BLOCK_SIZE)
            if main_block_rect == block_rect:
                gameover = True

        # game over
        if gameover == True:
            windowSurface.fill(WHITE)
            game_over()
            time_score()
            button('RESTART', YELLOW, 240, 300, 120, 30)
            restart(240, 300, 120, 30)
            start_time = time.time()
            
        # game clomplete
        elif gamecomplete == True:
            windowSurface.fill(WHITE)
            game_complete()
            time_score()
            button('NEXT STAGE', YELLOW, 240, 300, 120, 30)
            next_stage(240, 300, 120, 30)
            start_time = time.time()


        else:
            Time = time_score()
            if event.type == pygame.KEYDOWN:
                if event.key in KEY:
                    main_block_direction = KEY[event.key]
                    if main_block_direction == 'up':
                        if  main_block_position[0] - BLOCK_SIZE != 0:
                            main_block_position[0] -= BLOCK_SIZE

                    elif main_block_direction == 'down':
                        if main_block_position[0] + BLOCK_SIZE != WINDOWHEIGHT - BLOCK_SIZE:
                            main_block_position[0] += BLOCK_SIZE

                    elif main_block_direction == 'left_':
                        if main_block_position[1] - BLOCK_SIZE != 0:
                            main_block_position[1] -= BLOCK_SIZE

                    elif main_block_direction == 'right':
                        if main_block_position[1] + BLOCK_SIZE != WINDOWWIDTH - BLOCK_SIZE:
                            main_block_position[1] += BLOCK_SIZE

            draw_block(windowSurface, BLACK, main_block_position)
                                
            # move block
            for i in list_movblock:
                if i['dir'] == 'up':
                    for j in list_movblock:
                        a = j['left']
                        b = j['top']
                        for k in list_block:
                            c = k['left']
                            d = k['top']
                            haha = (a, b - 20, BLOCK_SIZE, BLOCK_SIZE)
                            hahaha = (c, d , BLOCK_SIZE, BLOCK_SIZE)
                            if haha == hahaha:
                                j['dir'] = 'down'
                    if  i['top'] - BLOCK_SIZE != 0:
                        i['top'] -= MOVESPEED
                    else:
                        i['dir'] = 'down'

                elif i['dir'] == 'down':
                    for j in list_movblock:
                        a = j['left']
                        b = j['top']
                        for k in list_block:
                            c = k['left']
                            d = k['top']
                            haha = (a, b + 20, BLOCK_SIZE, BLOCK_SIZE)
                            hahaha = (c, d , BLOCK_SIZE, BLOCK_SIZE)
                            if haha == hahaha:
                                j['dir'] = 'up'
                    if  i['top'] + BLOCK_SIZE != WINDOWHEIGHT - BLOCK_SIZE:
                        i['top'] += MOVESPEED
                    else:
                        i['dir'] = 'up'

                elif i['dir'] == 'left_':
                    for j in list_movblock:
                        a = j['left']
                        b = j['top']
                        for k in list_block:
                            c = k['left']
                            d = k['top']
                            haha = (a - 20, b, BLOCK_SIZE, BLOCK_SIZE)
                            hahaha = (c, d, BLOCK_SIZE, BLOCK_SIZE)
                            if haha == hahaha:
                                j['dir'] = 'right'
                    if i['left'] - BLOCK_SIZE != 0:
                        i['left'] -= MOVESPEED
                    else:
                        i['dir'] = 'right'

                elif i['dir'] == 'right':
                    for j in list_movblock:
                        a = j['left']
                        b = j['top']
                        for k in list_block:
                            c = k['left']
                            d = k['top']
                            haha = (a + 20, b, BLOCK_SIZE, BLOCK_SIZE)
                            hahaha = (c, d, BLOCK_SIZE, BLOCK_SIZE)
                            if haha == hahaha:
                                j['dir'] = 'left_'
                    if  i['left'] + BLOCK_SIZE != WINDOWWIDTH - BLOCK_SIZE:
                        i['left'] += MOVESPEED
                    else:
                        i['dir'] = 'left_'

            for j in list_movblock:
                a = j['left']
                b = j['top']
                pygame.draw.rect(windowSurface, PINK1, (a, b, BLOCK_SIZE, BLOCK_SIZE))
            
            for j in list_block:
                a = j['left']
                b = j['top']
                pygame.draw.rect(windowSurface, SKYBLUE1, (a, b, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.update()
        mainClock.tick(10)