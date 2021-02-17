import random
from pen import Pen


class LSystem:
	instruction = ''
	axiom = None
	rules = None
	pen: Pen = None
	iterations: int = 0
	len_segment: int = 5
	stack = []
	custom_angle = 0

	@classmethod
	def instruction_gen(cls, iters):
		result = cls.axiom
		for k in range(iters):
			result_tmp = ''
			for ch in result:
				if ch not in cls.rules:
					result_tmp += ch
				elif type(cls.rules[ch]) is tuple:
					result_tmp += random.choice(cls.rules[ch])
				else:
					result_tmp += cls.rules[ch]
			result = result_tmp
		cls.instruction = result

	@classmethod
	def action(cls, char):
		if char == 'F' or char == '0':
			cls.pen.draw_forward(cls.len_segment)
		elif char == 'f':
			cls.pen.go_forward(cls.len_segment)
		elif char == '+':
			cls.pen.rotate(90)
		elif char == '-':
			cls.pen.rotate(-90)
		elif char == '>':
			cls.pen.rotate(45)
		elif char == '<':
			cls.pen.rotate(-45)
		elif char == '*':
			cls.pen.rotate(cls.custom_angle)
		elif char == '#':
			cls.pen.rotate(-cls.custom_angle)
		elif char == '[':
			cls.stack.append(cls.pen.get_pen())
		elif char == ']':
			cls.pen.set_pen(*cls.stack.pop(-1))
		else:
			return 1
		return 0

	@classmethod
	def draw(cls, iterations: int = 1):
		assert cls.axiom is not None and cls.rules is not None, "You must override vars axiom and rules"
		cls.instruction_gen(iterations)
		for character in cls.instruction:
			cls.action(character)


class Paporotnic(LSystem):
	axiom = '0'
	rules = {
		'0': '[-F][+F]F',
		'F': 'F0'
	}

		
class PythagorasTree(LSystem):
	axiom = '0'
	rules = {
		'1': '11',
		'0': '1[0]0',
		'[': '[',
		']': ']'
	}

	@classmethod
	def action(cls, char):

		if char == '1':
			cls.pen.draw_forward(cls.len_segment)
		if char == '0':
			cls.pen.draw_forward(cls.len_segment)
			cls.pen.leaf()
		elif char == '[':
			cls.stack.append(cls.pen.get_pen())
			cls.pen.rotate(-45)
		elif char == ']':
			cls.pen.set_pen(*cls.stack.pop(-1))
			cls.pen.rotate(45)


class PlantA(LSystem):
	axiom = 'F'
	custom_angle = 25.7
	rules = {
		'[': '[',
		']': ']',
		'*': '*',
		'#': '#',
		'F': 'F[*F]F[#F]F'
	}


class PlantD(LSystem):
	axiom = 'X'
	custom_angle = 20
	rules = {
		'[': '[',
		']': ']',
		'*': '*',
		'#': '#',
		'X': 'F[*X]F[#X]*X',
		'F': 'FF'
	}


class PlantE(LSystem):
	axiom = 'X'
	custom_angle = 25.7
	rules = {
		'[': '[',
		']': ']',
		'*': '*',
		'#': '#',
		'X': 'F[*X][#X]FX',
		'F': 'FF'
	}


class PlantZ(LSystem):
	axiom = 'X'
	custom_angle = 25
	rules = {
		'X': 'F#[[X]*X]*F[*FX]#X',
		'F': 'FF'
	}

class PythagorasTree_plus(LSystem):
	axiom = '0'
	rules = {
		'1': '21',
		'0': ('1[+0]0', '1[-0]0', '1[-0][+0]0', '1[-0]+0', '1-0', '1+0', '10'),
		}

	@classmethod
	def instruction_gen(cls, iters):
		result = cls.axiom
		for k in range(iters):
			result_tmp = ''
			for ch in result:
				if ch not in cls.rules:
					result_tmp += ch
				elif type(cls.rules[ch]) is tuple:
					result_tmp += random.choice(cls.rules[ch])
				else:
					result_tmp += cls.rules[ch]
			result = result_tmp
		cls.instruction = result

	@classmethod
	def action(cls, char):
		len_branch = cls.len_segment
		len_branch += random.randrange(-10, 10)
		ang = 40
		if char in ['1', '2', 'l', 'r']:
			cls.pen.draw_forward(len_branch)
		elif char == '0':
			cls.pen.draw_forward(len_branch)
			cls.pen.leaf() 
		elif char == '[':
			cls.pen.width -= 1
			cls.stack.append(cls.pen.get_pen())
		elif char == '-':
			cls.pen.rotate(-ang + random.randrange(0, 11))
		elif char == ']':
			cls.pen.set_pen(*cls.stack.pop(-1))
		elif char == '+':
			cls.pen.rotate(ang + random.randrange(-10, 1))
