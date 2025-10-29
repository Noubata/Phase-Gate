public class UniqueElement{

	public int [] theArrayItself(int [] nums){

		int count = 0;
		int number = nums[1];
		
		for(int index = 0; index < nums.length; index++){
		
		if (number != nums[index]){
		
		count+=number;
		}
		}
		int [] result = new int[count];
		return result;

	}

}