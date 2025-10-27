import java.util.random;
import java.util.Scanner; 
public class Day1{
public static void main(String...args){
int count_exact_answer = 0;
int count_wrong_answer = 0;


	for (int toRun = 1; toRun < 11; toRun++){
	int number1 = random(31, 61);
	int number2 = random(1, 30);
	int result = number1 - number2;
	
	int question = System.out.printf("What is %d - %d: ", number1, number2);
	if (question < 1){
	
		System.out.print("Invalid input");
	}else{

		if (result == question){
			count_exact_answer+=1;
			System.out.print("Good! You won");
	
		}else{
			count_wrong_answer +=1;
			System.out.print("Try again! You lost");
		}

		if (count_exact_answer > count_wrong_answer){
		
			System.out.printf("Good! You won times", count_exact_answer);

		}else{
			System.out.printf("Oops! You lost times", count_wrong_answer);
		}
	}
	}
	}

}