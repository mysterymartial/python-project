import java.util.Scanner;
public class TemperatureConverter{

	
	public static double fahrenheit ( ){
		double faraday = 0;
		int counter = 0;
	
	for(int count = 0; count <=100; count++){

	 faraday =  (9 / 5) * count + 3;
		counter++;

}

		return faraday;


}



	public static void main (String...args){
					
		double result = fahrenheit();

		System.out.println(result);


}


} 