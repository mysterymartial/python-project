import java.util.Scanner;
import java.security.SecureRandom;
public class Guessgame{

	public static void main(String...args){
	
	System.out.println("Welcome to my guess gaming app");
	Scanner sc= new Scanner(System.in);
	SecureRandom computer = new SecureRandom();
	int output = computer.nextInt(1000) + 1;

	int gamer = 0;
	int factor1 = 0;
	int factor2 = 0;
	int sentel = -1;
	System.out.println("Enter any number to start the game or -1 to exist");
	int userinput = 0;
	userinput = sc.nextInt();

	while(userinput != sentel){
		System.out.println("Enter any number between 1 and 1000");
			gamer = sc.nextInt();

		if(gamer == output){

			System.out.println("Congratulation you gussed right");
				

}


		else if(gamer > output){
				System.out.println("Your guess is too high");
					factor1++;

}


		else {


			System.out.println("Your guess is too low");
					factor2++;
		}
			
			System.out.println("Enter any number to continue and -1 to exist");
				userinput = sc.nextInt();

			
			
}


		System.out.println("This is the total number of times you choosed numbers that are too high " + factor1);
		System.out.println("This is the total number of times you choosed numbers too low " + factor2);

}

}	
		

	