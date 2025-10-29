import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.BeforeEach;
public class TestBuyMoto{

	public Price userInput ;
	@BeforeEach
	public void Test(){
	userInput = new Price();
	}
	
	

	public void testThatItemsHaveFixedPrice(){

	double result = userInput.items();

	assertEquals(100000, result);

	}
	
	@Test
	public void testThatItemscollectInput(){

	double result = userInput.items(2);

	assertEquals(2, result);

	}


}

