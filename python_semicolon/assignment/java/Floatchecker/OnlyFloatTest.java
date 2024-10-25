
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class OnlyFloatTest{


	@Test
	public void canCheckeWhetheryourTwoValuesAreFloat(){

	OnlyFloat check = new OnlyFloat();

	float result =check.only_decimal(2.2, 3.3);
	assertEquals(2, result);


}


}