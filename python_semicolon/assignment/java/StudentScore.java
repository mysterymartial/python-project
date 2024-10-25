import java.util.Scanner;
public class StudentScore{

	public static void main(String...args){
		Scanner sc= new Scanner(System.in);
		
		int sum1 = 0;
		int sum2 = 0;
		int score = 0;

		for(int count=1; count<=15; count++){

			System.out.println("Enter a student score");
			score= sc.nextInt();

			if (score>=45){
				
				System.out.println("this student passed my subject");
				sum1++;

		
			}

			
			else{
				
				System.out.println("this student failed my subject");
					sum2++;

			
			}







}

	System.out.println("The total student that passed my subject is " + sum1);
	System.out.println("The total student that falied my subject is " + sum2);

}

}