import java.util.Scanner;
public class Interest{

public static double interestRate(int amount,  int years){
	double result;
	int interest = 7;
	int sumOfInterest = 1 + interest;
	double interestCalc = Math.pow(sumOfInterest, years);
	 result = amount * interestCalc;
		return result;

}



	public static void main(String...args){
	Scanner sc= new Scanner(System.in);
	double answer = 0;
	System.out.println("Enter the amount of your monthly pay");
	int amount = sc.nextInt();

	for(int count = 1; count <= 30; count++){
		
		 answer = Interest.interestRate( amount, count);

		System.out.printf("This is the interest %f and this the years %d%n ", answer, count);
		


}

	

}

}