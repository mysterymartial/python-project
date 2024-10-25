import java.lang.Math;
import java.util.Scanner;
public class Large{
       public static void main(String[]args){
       int number= 0;
   
       int highest= Integer.MIN_VALUE;
       int lowest= Integer.MAX_VALUE;

       Scanner sc= new Scanner(System.in);
		System.out.println("ENTER FIVE INTERGER NUMBERS");

              
 for(int i=0; i<5; i++){
	   number= sc.nextInt();

        
          

 if(number>highest){
     highest= number;

             }
 if (number < lowest){
            lowest= number;
                     
 		}

                      
        }


		System.out.println("YOUR HIGHEST NUMBER IS " + highest);
		System.out.println("YOUR LOWEST NUMBER IS " + lowest);
   


        }
       }

      