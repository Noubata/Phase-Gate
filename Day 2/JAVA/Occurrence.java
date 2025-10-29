public class Occurrence{


	public static String index(String TheWord){
		char aCharacter= 'e';
		String aString = "";
		for(int eachString = 0; eachString < TheWord.length(); eachString++){
		char letter = TheWord.charAt(eachString);
		if (aCharacter == 'e'){
			break;
		}
		aString += letter;
		}
		return TheWord;
	}

} 

