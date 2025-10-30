test_list = [4, 9, 25, 49, 100, 6]
def perfect_square(test_list):
	count = 0
	newBox = test_list
	for number in test_list:
		new_number = number**0.5 * number**0.5
		if new_number == number:
			newBox[count]= True
		else:
			newBox[count]= False
		count += 1
	return newBox

			
print(perfect_square(test_list))





