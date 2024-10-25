import java.util.Scanner;
public class Newwork{

	public static void main(String...args){
	String response1 = "yes";
	
	Scanner sc= new Scanner(System.in);
	System.out.println("What is your problem ?:");
	String problem = sc.nextLine();
	System.out.println("Have you had this problem before");
	String answer = sc.next();
	

	if(answer == response1)
	
		System.out.println("Well you have it again");


	else
	
		System.out.println("Well you have it now");


}


}





	

		