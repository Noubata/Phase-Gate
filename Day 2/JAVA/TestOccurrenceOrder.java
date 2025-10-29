import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestOccurrenceOrder{

	@Test
	public void testThatIndexcollectsInput(){

	OccurrenceOrder change = new OccurrenceOrder();

	int word = change.index(1,2,2,3,4,4,5,6,6,7);

	assertEquals(1,2,3,4,5,6,7);

	}
}