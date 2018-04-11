import random
num = random.randint(1, 100)
while True:
		   print('Guess a number between 1 and 100')
		   guess = input()
		   i = int(guess)
		   if i == num:
			   print('You are right!')
			   break
		   elif i < num:
			   print('Guess higher')
		   elif i > num:
			   print('Guess lower')
