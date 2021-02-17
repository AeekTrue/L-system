import math
import pygame
from point import Point
from random import randrange
from colors import *


class Pen:
	angle = -90

	def __init__(self, surface, pos: Point, color=(0, 255, 0), width=1):
		self.position: Point = pos
		self.color = color
		self.width: int = width
		self.surface: pygame.Surface = surface

	def get_rad_vector(self):
		x = math.cos(math.radians(self.angle))
		y = math.sin(math.radians(self.angle))
		return Point(x, y)

	def draw_forward(self, px: int):
		radius_vector = self.get_rad_vector()
		delta_vector = radius_vector * px
		delta_vector.x, delta_vector.y = int(delta_vector.x), int(delta_vector.y)
		go_to: Point = self.position + delta_vector
		pygame.draw.line(self.surface, self.color, self.position.get(), go_to.get(), self.width)
		self.position = go_to

	def go_forward(self, px: int):
		radius_vector = self.get_rad_vector()
		delta_vector = radius_vector * px
		delta_vector.x, delta_vector.y = int(delta_vector.x), int(delta_vector.y)
		go_to: Point = self.position + delta_vector
		self.position = go_to

	def rotate(self, degree: int):
		self.angle += degree

	def set_pen(self, pos: Point, ang: int, width: int):
		self.position = pos
		self.angle = ang
		self.width = width

	def get_pen(self):
		return self.position, self.angle, self.width

	
	def leaf(self):
		color = (randrange(100, 255), 100, 100)
		size = randrange(self.width + 2, self.width + 5)
		if randrange(0, 100) < 10:
			color = RED
			size = self.width + 6
		pygame.draw.circle(self.surface, color, self.position.get(), 4)
