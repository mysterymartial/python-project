
public class DiscountCalc{
	

	public static double discountchecker(double price,  double discountPercent){

		double discount = 0;

		double calc = price * (discountPercent/100);
		
		double calc1 = price - calc;
		discount = calc1;
		
		return discount;



}



}