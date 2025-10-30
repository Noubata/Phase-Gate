import java.util.Scanner; 
import java.util.Random;
public class Day1{
public static void main(String...args){
Scanner input = new Scanner(System.in);
int count_exact_answer = 0;
int count_wrong_answer = 0;

	Random repeat = new Random();
	

	int toRun = 1;
	while(true){
	int number1 = repeat.nextInt(91)+34;
	int number2 = repeat.nextInt(33)+1;
	int result = number1 - number2;

	System.out.printf("What is %d - %d%n ", number1, number2 + toRun);
	int question = input.nextInt();
	toRun++;
	if (toRun > 10){
	break;
	}
	if (question < 1){
	
		System.out.println("Invalid input");
	}else{

		if (result == question){
			count_exact_answer+=1;
			System.out.println("Good! You won");
	
		}else{
			count_wrong_answer +=1;
			System.out.println("Try again! You lost");
		}

		if (count_exact_answer > count_wrong_answer){
		
			System.out.printf("Good! You won %d times\n", count_exact_answer);

		}else{
			System.out.printf("Oops! You lost %d times\n", count_wrong_answer);
		}
	}
	}
	}

}