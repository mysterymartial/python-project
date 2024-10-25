import java.util.Scanner;
public class Timeconverter{
	

	public static long getSeconds (int day, int hour, int mintues, int second){

		long hourInSeconds = hour * 3600;
		long mintuesInSeconds = mintues * 60;
		long seconds = hourInSeconds + mintuesInSeconds + second;

		return seconds;




}


	public static void main(String...args){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter your day");
		int day = sc.nextInt();
		System.out.println("Enter your hour");
		int hour = sc.nextInt();
		System.out.println("Enter your mintues");
		int mintues = sc.nextInt();
		System.out.println("Enter your second");
		int second = sc.nextInt();
		long result = getSeconds(day,hour,mintues,second);
		System.out.println(result);
		


}

}




