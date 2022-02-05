def combine(first, second, last = 15):
	print(first + last)

def get_length(first, second):
	return len(first) + len(second)

length = get_length("something old"[0:10], "something new"[10:])

def mystery(puzzle):
	return puzzle + 'y'

def enigma(conundrum, riddle):
	return mystery(riddle * 2) + mystery(conundrum)

stmt = enigma('x', 'zz')
