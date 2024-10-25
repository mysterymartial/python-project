import java.util.Scanner;
public class Newjob{
       public static void main(String[]args){

          int number;
          Scanner sc= new Scanner(System.in);
          System.out.println("ENTER A SET OF INTEGERS");
          number= sc.nextInt();
          int orgnumber= number;

          int reverse= 0;

          while(number!=0)
          {

         reverse=reverse*10 + number%10;
         number= number/10;
	

            
        }

         if(orgnumber==reverse){

               System.out.println("THIS IS A PALINDROME NUMBER");
     
                 }
 
        else{

              System.out.println("THIS IS NOT A PALINDROME NUMBER");
        
               }
        }
       }