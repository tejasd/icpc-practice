#!/usr/bin/python

# B - Mastering Mastermind
# ACM ECNA 2015 Practice Set
# Tejas Deshpande

import collections

def calculateR(code, guess):

	r = 0

	for i in range(len(code)):
		if code[i] == guess[i]:
			code[i] = ''
			guess[i] = ''
			r += 1

	updated_code = []
	updated_guess = []
	for code_element, guess_element in zip(code, guess):
		if code_element != '':
			updated_code.append(code_element)
			updated_guess.append(guess_element)

	return (updated_code, updated_guess, r)

def calculateS(code, guess):
	s = 0

	code.sort()
	guess.sort()

	code = collections.deque(code)
	guess = collections.deque(guess)

	while (len(code) > 0 and len(guess) > 0):
		if (code[0] == guess[0]):
			code.popleft()
			guess.popleft()
			s += 1
		elif (code[0] < guess[0]):
			code.popleft()
		else:
			guess.popleft()

	return s

if __name__ == "__main__":
	input_line = raw_input()
	input_line = input_line.split(" ")
	_, code, guess = input_line

	code, guess, r = calculateR(list(code), list(guess))
	s = calculateS(code, guess)

	print r, s



