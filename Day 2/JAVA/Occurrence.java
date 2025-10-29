import java.util.ArrayList;
public class Occurrence{
	public static int getPositionOfTheChar(String letters, char ch ){
		int firstIndexNewWord = 0;
		for(int count = 0; count < letters.length(); count++){
			if(letters.charAt(count) == ch){
				firstIndexNewWord = count;
					break;
			}
		}
		return firstIndexNewWord;
		}
}