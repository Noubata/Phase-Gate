let count_exact_answer = 0;
let count_wrong_answer = 0;


	for (int toRun = 1; toRun < 11; toRun++){
	let number1 = random(31, 61);
	let number2 = random(1, 30);
	let result = number1 - number2;
	
	let question = console.log("What is %d - %d: ", number1, number2);
	if (question < 1){
	
		console.log("Invalid input");
	}else{

		if (result == question){
			count_exact_answer+=1;
			System.out.print("Good! You won");
	
		}else{
			count_wrong_answer +=1;
			console.log("Try again! You lost");
		}

		if (count_exact_answer > count_wrong_answer){
		
			console.log("Good! You won times", count_exact_answer);

		}else{
			console.log("Oops! You lost times", count_wrong_answer);
		}
	}

}