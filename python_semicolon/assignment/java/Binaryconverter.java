import java.util.Scanner;
public class Binaryconverter{

	Scanner sc= new Scanner(System.in);
	public static int baseConverter(String binary){
		int decimalvalue = Integer.parseInt (binary, 2);
		

		return decimalvalue;

	}


	public static void main(String...args){
	Scanner sc= new Scanner(System.in);
	
	System.out.println("Enter your binary number");
	String binary= sc.next();
	int answer = baseConverter(binary);
	System.out.printf("your binary %s in decimal base is %d", binary, answer);

}



}