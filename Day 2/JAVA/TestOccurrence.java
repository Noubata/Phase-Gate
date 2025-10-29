import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestOccurrence{

	@Test
	public void testThatItemscollectInput(){

	Occurrence change = new Occurrence();

	String word = change.index("Beny");

	assertEquals("Byne", word);

	}
}