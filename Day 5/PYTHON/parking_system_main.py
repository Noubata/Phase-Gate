from parking_system import my_parking, parking_status, park_car, leave_parking
status = my_parking()
while True:


	print("""
	====== WELCOME TO YOUR FAVORITE CAR PARKING =====

		1. CHECK PARKING STATUS

		2. PARK CAR

		3. LEAVE PARKING
	
	
	""")

	question = int(input("Enter your choice: "))

	match question:

		case 1: 
			print(parking_status(status))
		case 2:
			try:
				car_number = int(input("Enter your car number: "))
				park_car(status, car_number)  
			except ValueError:
				raise ValueError("Enter valid input")
		case 3:
			try:
				car_number = int(input("Welcome back bro! What is your car number: "))
				leave_parking(status, car_number)
			except ValueError:
				raise ValueError("Enter valid input")