import random 
import datetime
count_exact_answer = 0
count_wrong_answer = 0

for number in range(10):
	number1 = random.randrange(31, 61)
	number2 = random.randrange(1, 30)
	result = number1 - number2
	
	question = int(input(f"What is {number1} - {number2}: "))

	if question < 1 or type(question) != int:
		print("Invalid input")
	else:

		if result == question:
			count_exact_answer+=1
			print("Good!")

		else:
			count_wrong_answer +=1
			print("Try again!")
		
	if count_exact_answer > count_wrong_answer:
		
		print(f"Good! You won {count_exact_answer} times")

	else:
		print(f"Oops! You lost {count_wrong_answer} times")
	