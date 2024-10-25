import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TaxrateTest{


	

	@Test
	public void testThatCheckTheRoadTaxOfAVehecile(){
		

		Taxrate tax = new Taxrate();
		

		double result = tax.taxcalculator(1000000);
	
		assertEquals(150000, result);

}



}