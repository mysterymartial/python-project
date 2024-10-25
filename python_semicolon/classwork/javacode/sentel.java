import java.util.Scanner;
public class Sentel{
	public static void main(String [] args){
System.out.println("Welcome to The Mysterious Bank of Africa");
Scanner sc= new Scanner(System.in);


 String sentinel = new String();
 double balance = 0;



while (!sentinel.equals("D")){

	System.out.println("Enter A to deposit and Enter B to withdrawal and C to check balance");
	      	   	
			sentinel = sc.next();
	switch (sentinel){
	

		case "A":
			 System.out.println("Enter the amount you want to deposit");
			 double deposit= sc.nextDouble();
			balance= balance + deposit;
				break;

		case "B":

			 System.out.println("Enter the amount you want to withdrawl");
			 double withdrawl= sc.nextDouble();
			 if(balance == 0 || withdrawl > balance){
				System.out.println("You cannot withdrawal");

	}
			else {
			      	balance= balance - withdrawl; 
}
				
				break;

		case "C":
				if(balance == 0)
					System.out.println("insufficient funds");
                  	  System.out.println("Your balance is " + balance);
				break;

		
		
}

 }


}

}