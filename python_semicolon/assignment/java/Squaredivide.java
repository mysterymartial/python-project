import java.util.Scanner;
public class Squaredivide{


	public static double divide_square( double number){

		double square = 0;
		if (number % 5 == 0){
			square = Math.sqrt(number);
				return square;

		}


		else {

			return number % 5;

		}

}



	public static void main (String...args){

	Scanner sc= new Scanner(System.in);
	System.out.println("Enter a number");

	int number = sc.nextInt();
	double result = divide_square(number);
	System.out.printf("%.2f", result); 
}	

}