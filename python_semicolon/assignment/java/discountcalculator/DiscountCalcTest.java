import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class DiscountCalcTest{

	@Test
	public void canCalculateDiscountPercentage(){

	DiscountCalc calc = new DiscountCalc();
	double result = calc.discountchecker(150, 15);
	assertEquals(127.5, result);

}


}