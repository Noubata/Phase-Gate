import random 

count_exact_answer = 0
count_wrong_answer = 0
print(" ")
print("			==== QUIZZ GAME ====")
print(" ")
print("			Ayo my man, let's have fun")
for number in range(10):
	number1 = random.randrange(6, 100)
	number2 = random.randrange(7, 30)
	result = number1 * number2
	
	answer1 = random.randrange(50, 2000)
	answer2 = random.randrange(22, 1789)
	print(" ")
	

	try:
		
		print(f"If your young brother ask you how much is {number1} * {number2} what would be your answer?: ")
		
		print(" ")
		print(f"A.{answer1}")
		print(f"B.{result}")
		print(f"C.{answer2}")
		print(" ")

		question = int(input("Do not Enter letters(A, B, C), the answer only: "))
		if question < 1:
			raise ValueError ("Invalid input brother!")
		if question == result:
			count_exact_answer+=1
			print("Oga you get sense o! Nice one")
			print(" ")

		else:
			print("See this one! Wrong guess")
			count_wrong_answer +=1
			print(" ")
	except ValueError:
		print("Enter a valid input!")
		#question = int(input(f"If your young brother ask you how much is {number1} * {number2} what would be your answer?: "))
		
print(" ")
if count_exact_answer > count_wrong_answer:
		
	print(f"Good! You got {count_exact_answer} out of 10")

else:
	print(f"Oops! You got {count_wrong_answer} out of 10")

	