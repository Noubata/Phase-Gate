import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestUniqueElement{

	@Test
	public void testThatEachIndexIsUnique(){

	UniqueElement user = new UniqueElement();
	int [] number = {1,2,3,2};
	int [] element = user.theArrayItself(number);

	assertEquals(4,element);
	}

}