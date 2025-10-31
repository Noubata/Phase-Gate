def my_parking():

	car_lists = {'Space 1' : None, 'Space 2' : None, 'Space 3' : None, 'Space 4' : None, 'Space 5' : None, 'Space 6' : None, 'Space 7' : None, 'Space 8' : None, 'Space 9' : None, 'Space 10' : None, 'Space 11' : None, 'Space 12' : None, 'Space 13' : None, 'Space 14' : None, 'Space 15' : None, 'Space 16' : None, 'Space 17' : None, 'Space 18' : None, 'Space 19' : None, 'Space 20' : None}

	return car_lists


def parking_status(car_lists):
	
	count = 0
	count1 = 0
	for available_space in car_lists.values():

		if not available_space:
			count+=1
		else:
			count1+=1
		
	result = print(f"{count1} occupied space and {count} empty space")
	return result


def park_car(car_lists, car_number):

	for available_space1, available_space2 in car_lists.items():

		if not available_space2:
	
			car_lists[available_space1] = car_number
			result = print(f"Your car N:{car_number} is parked in {available_space1}.")
			return result
		else:
			return
			print("No slots no dey")


def leave_parking(car_lists, car_number):

	for available_space1, available_space2 in car_lists.items():

		if car_number == available_space2:
			car_lists.get(car_number)
			result = print(f"Car N:{car_number} your are leaving {available_space1} oo.")
			return result
		else:
			result = print(f"Car N:{car_number} no dey! You no get car for here.")
			return result
