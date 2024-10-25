public class Taxrate{

	public static double taxcalculator ( int price){

		double tax = 1;

		if(price < 1000000){
			tax = price * 10/100;
				return tax;
			

			}


		 if(price >= 1000000 && price <= 3000000){
				tax = price * 15/100;
				return tax;
		}

				System.out.print(tax);

		 if(price >= 3000000 && price <= 5000000){
	
				tax = price * 20/100;

				return tax;
}

		if(price > 5000000){

			tax = price * 25/100;

				
			}

				return tax;	

			}

	


	

}