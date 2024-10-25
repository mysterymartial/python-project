import java.util.Scanner;

public class Separate{

	public static void main(String...args){
	Scanner sc= new Scanner(System.in);
	int numbers = 0;
	System.out.println("Enter five integer numbers");
	


	while(true){
		
		numbers = sc.nextInt();
	
		

	
		
		int lastnumber = numbers % 10;   
		int lastdivide = numbers / 10;    
		int fourthnumber = lastdivide % 10;  
		int fourthdivide = lastdivide / 10;
		int thridnumber = fourthdivide % 10;
		int thirddivide = fourthdivide / 10;
		int secondnumber = thirddivide % 10;
		int seconddivide = thirddivide / 10;
		int firstnumber = seconddivide % 10;
		System.out.println("Enter five integer numbers");


   
	System.out.println(firstnumber + secondnumber + thridnumber + fourthnumber + lastnumber);
	System.out.println("Enter five integer numbers");
	

	
}

	

}

}