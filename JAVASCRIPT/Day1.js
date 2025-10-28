let count_exact_answer = 0;
let count_wrong_answer = 0;

	let number1 = Math.random(31, 61);
	let number2 = Math.random(1, 30);
	let result = number1 - number2;
	
	let toRun = 1;

	while(toRun < 11){
	toRun++
	
	if (question < 1){
	
		console.log("Invalid input");
	}else{

		if (result == question){
			count_exact_answer+=1;
			console.log("Good! You won");
	
		}else{
			count_wrong_answer +=1;
			console.log("Try again! You lost");
		}

		if (count_exact_answer > count_wrong_answer){
		
			console.log("Good! You won %d times", count_exact_answer);

		}else{
			console.log("Oops! You lost %d times", count_wrong_answer);
		}
	}

}