class Point:
	x = 0
	y = 0

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return f'<Point({self.x};{self.y})>'

	def __add__(self, other):
		if type(other) == int:
			x = self.x + other
			y = self.y + other
		elif type(other) == Point:
			x = self.x + other.x
			y = self.y + other.y
		else:
			raise TypeError
		return Point(x, y)

	def __mul__(self, other):
		if type(other) == int:
			x = self.x * other
			y = self.y * other
		elif type(other) == Point:
			x = self.x * other.x
			y = self.y * other.y
		else:
			raise TypeError
		return Point(x, y)

	def set(self, x, y):
		self.x = x
		self.y = y

	def get(self):
		return self.x, self.y
