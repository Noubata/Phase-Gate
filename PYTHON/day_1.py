import random 
import datetime
count_exact_answer = 0
count_wrong_answer = 0

for number in range(10):
	number1 = random.randrange(31, 61)
	number2 = random.randrange(1, 30)
	result = number1 - number2
	

	try:
		question = int(input(f"What is {number1} - {number2}: "))
		if question < 1:
			raise ValueError ("Invalid input brother!")
		if question == result:
			count_exact_answer+=1
			print("Good!")

		else:
			print("Wrong guess. Try once more")
			question = int(input(f"What is {number1} - {number2}: "))
			count_wrong_answer +=1
			if question:
				print("You no get brain!")
			
	except ValueError:
		print("Enter a valid input!")
		question = int(input(f"What is {number1} - {number2}: "))
		if question == result:
			print("Good!")
			continue

print(" ")
if count_exact_answer > count_wrong_answer:
		
	print(f"Good! You got {count_exact_answer} out of 10")

else:
	print(f"Oops! You lost {count_wrong_answer} out of 10")

	