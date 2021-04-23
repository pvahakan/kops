#!/usr/bin/env python3

import os
import pygame
import random

letters = ['h', 'j', 'k', 'l']
running = True

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

r = 95

pygame.init()

font = pygame.font.SysFont(None, 150)
h_img = font.render('H', True, WHITE)
j_img = font.render('J', True, WHITE)
k_img = font.render('K', True, WHITE)
l_img = font.render('L', True, WHITE)

win = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Speed tester')

def random_letter():
    i = random.randint(0, 3)
    return letters[i]

def update_time(x):
    if x > 1:
        return x - 0.1 * x
    elif x <= 0.4:
        return 0.4
    elif x < 0.6:
        return x - 0.005 * x
    elif x <= 1:
        return x - 0.03 * x

def cli_print():
    os.system('clear')
    i = letters.index(random_letter())
    for l in letters:
        if l == letters[i]:
            print(l.upper(), end='\t')
        else:
            print(l, end='\t')
    print()

def draw_game(letter, score):

    win.fill(BLACK)
    score_img = font.render(str(score), True, WHITE)

    w_h, w_j, w_k, w_l = 5, 5, 5, 5

    if letter == 'h':
        w_h, w_j, w_k, w_l = 0, 5, 5, 5
    elif letter == 'j':
        w_h, w_j, w_k, w_l = 5, 0, 5, 5
    elif letter == 'k':
        w_h, w_j, w_k, w_l = 5, 5, 0, 5
    elif letter == 'l':
        w_h, w_j, w_k, w_l = 5, 5, 5, 0

    pygame.draw.circle(win, RED, (100, 300), r, width=w_h)
    win.blit(h_img, (100-37, 300-37))
    pygame.draw.circle(win, YELLOW, (300, 300), r, width=w_j)
    win.blit(j_img, (300-37, 300-37))
    pygame.draw.circle(win, GREEN, (500, 300), r, width=w_k)
    win.blit(k_img, (500-37, 300-37))
    pygame.draw.circle(win, BLUE, (700, 300), r, width=w_l)
    win.blit(l_img, (700-37, 300-37))

    win.blit(score_img, (370, 60))

    pygame.display.update()

def draw_empty_circles():
    w = 5
    win.fill(BLACK)
    pygame.draw.circle(win, RED, (100, 300), r, width=w)
    win.blit(h_img, (100-37, 300-37))
    pygame.draw.circle(win, YELLOW, (300, 300), r, width=w)
    win.blit(j_img, (300-37, 300-37))
    pygame.draw.circle(win, GREEN, (500, 300), r, width=w)
    win.blit(k_img, (500-37, 300-37))
    pygame.draw.circle(win, BLUE, (700, 300), r, width=w)
    win.blit(l_img, (700-37, 300-37))

    pygame.display.update()

if __name__ == "__main__":
    t = 1.3
    pressed_keys = []
    correct_keys = []
    score = 0
    while running:
        l = random_letter()
        t = update_time(t)

        draw_game(l, score)
        pygame.time.delay(round(t*1000))

        draw_empty_circles()
        pygame.time.delay(200)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    pressed_keys.append('h')
                elif event.key == pygame.K_j:
                    pressed_keys.append('j')
                elif event.key == pygame.K_k:
                    pressed_keys.append('k')
                elif event.key == pygame.K_l:
                    pressed_keys.append('l')


        correct_keys.append(l)

        if correct_keys != pressed_keys:
            print('Game over')
            print('Your score: ', score)
            running = False
            break
        else:
            score += 1

pygame.quit()