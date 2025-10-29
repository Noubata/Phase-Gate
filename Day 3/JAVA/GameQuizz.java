import java.util.Scanner;
import java.util.Random;
public class GameQuizz{

	public static void main(String...args){
	
	Scanner input = new Scanner(System.in);

		int count_exact_answer = 0;
		int count_wrong_answer = 0;
		System.out.println(" ");
		System.out.println("let's play a game");

		for (int number = 0; number <= 10; number++){

		int number1 = (int)(Math.random() * 101);
		int number2 = (int)(Math.random() * 500);
		int result = number1 * number2;
	
		int answer1 = 30 + (int)(Math.random() * 2000);
		int answer2 = 33 + (int)(Math.random() * 1789);


		System.out.println(" ");
		
		
		System.out.printf("If I ask you how much is %d * %d what would be your answer\n?: ",number1, number2);		

		System.out.println(" ");
		System.out.printf("A.",answer1);
		System.out.printf("B.",result);
		System.out.printf("C.",answer2);
		System.out.println(" ");

		System.out.println("Do not Enter letters(A, B, C), the answer only: ");
		int question = input.nextInt();
		
		if (question == result){
			count_exact_answer+=1;
			System.out.println("Yesssirrr! Nice one");
			System.out.println(" ");

		}else{
			System.out.println("Hahaha! Wrong guess");
			count_wrong_answer +=1;
			System.out.println(" ");
		}
		System.out.println("Enter a valid input!");
		
	}


	}

}