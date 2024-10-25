import java.util.Scanner;
public class Factoria{
	public static void main(String[]args){
        
        	int number= 0;
		long factoria= 1;
		long negation;
		
		

		Scanner sc= new Scanner(System.in);
       
     		System.out.println("ENTER A NUMBER");
			number= sc.nextInt();



	for(int i=1; i<=number; i++){

		factoria*= i;
			}


			
			System.out.println("YOUR FACTORIA IS " + factoria);
			
		}
		}