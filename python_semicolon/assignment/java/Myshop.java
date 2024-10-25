import java.util.Scanner;
public class Myshop{

	public static double shoping(double amount, double payment){

		double change= 0;
		change = payment - amount;

		return change;

}




	public static void main(String...args){

	Scanner sc= new Scanner(System.in);
	System.out.println("Enter the cost amount of the goods the customer is buying");
	double amount = sc.nextDouble();
	System.out.println("Enter the amount the customer pay in");
	double pay = sc.nextDouble();
	double change = shoping(amount, pay);
	System.out.printf("your change is %.1f penisis", change);

	

}


}