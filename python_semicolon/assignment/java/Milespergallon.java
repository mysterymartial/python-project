import java.util.Scanner;
public class Milespergallon{

	public static void main(String...args){
	int userinput;
	int counter = 0;
	int sum = 0;
	int average = 0;
	Scanner sc= new Scanner(System.in);
	System.out.println("Welcome to my miles per gallon calculator");
	System.out.println("Enter any number to procced and -1 to exit");
	userinput = sc.nextInt();
	
	while(userinput != -1){

		System.out.println("Enter miles driven");
		int driven = sc.nextInt();
		System.out.println("Enter amount of gallons of fuel used");
		int gallons = sc.nextInt();
		int miles_gallon = driven / gallons;
		counter++;
		System.out.println("Your miles per gallons is " + miles_gallon);
		sum += miles_gallon;
		average = sum / counter;
		System.out.println("Enter any number to procced and -1 to exit");
			userinput = sc.nextInt();


}


		System.out.println("The total miles per gallon is " + sum);
		System.out.println("The average of miles per gallon is " + average);

}

}
	

		
		
	
	
	