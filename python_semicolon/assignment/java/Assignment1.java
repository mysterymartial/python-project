import java.util.Scanner;
public class Assignment1{
	public static void main(String[] args){
	Scanner sc= new Scanner(System.in);

	 int number = 0;
	  int  sum = 0;



while (number != 2 && number != 1){
		System.out.println("Enter a number greater than 1 and 2");
		number= sc.nextInt();
		if(number != 1 && number != 2)
			sum = sum + number;
		
System.out.println("your sum is \n"+ sum);

}

}

}	





















