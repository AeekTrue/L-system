#!/usr/bin/python3
from pen import Pen
from point import Point
from l_systems import *
from colors import *
import pygame
import time
pygame.init()


ITERATIONS = 11
BRANCH_W = ITERATIONS + 1
BRANCH_COLOR = (75, 0x2c, 0x08)
BRANCH_SIZE = 10
BACKGROUND_COLOR = BLACK
FIELD_W = 2000
FIELD_H = 2000
start_pos = Point(FIELD_W // 2, FIELD_H // 2 + FIELD_H // 3)

WIDTH = pygame.display.Info().current_w
HEIGHT =  pygame.display.Info().current_h
DISPLAY_CENTRE = (WIDTH // 2, HEIGHT // 2)
blit_x, blit_y = DISPLAY_CENTRE[0] - FIELD_W//2, DISPLAY_CENTRE[1] - FIELD_H//2

sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
field = pygame.Surface((FIELD_W, FIELD_H))
field.fill(BACKGROUND_COLOR)

p = PythagorasTree_plus
p.pen = Pen(field, start_pos, BRANCH_COLOR, width=BRANCH_W)
p.len_segment = BRANCH_SIZE
p.draw(ITERATIONS)

sc.blit(field, (blit_x, blit_y))
pygame.display.update()
pygame.image.save(field, "PythagorasTree_plus.png")

# main loop
moved = False
move_way = 0
clock = pygame.time.Clock()
FPS = 2
while 1:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == 27:
				exit()
			elif event.key in [273, 274, 275, 276]:
				move_way = event.key
				moved = True
			elif event.key == 32:
				#generate next tree
				field.fill(BACKGROUND_COLOR)
				p.pen = Pen(field, start_pos, BRANCH_COLOR, width=BRANCH_W)
				p.draw(ITERATIONS)
		if event.type == pygame.KEYUP:
			if event.key in [273, 274, 275, 276]:
				moved = False

	if moved:
		if move_way == 273:
			blit_y += 25
		if move_way == 274:
			blit_y -= 25
		if move_way == 275:
			blit_x -= 25
		if move_way == 276:
			blit_x += 25
	
	#generate next tree
	#field.fill(BACKGROUND_COLOR)
	#p.pen = Pen(field, start_pos, BRANCH_COLOR, width=BRANCH_W)
	#p.draw(ITERATIONS)

	sc.blit(field, (blit_x, blit_y))
	pygame.display.update()
	clock.tick(FPS)
	sc.fill(GRAY)
