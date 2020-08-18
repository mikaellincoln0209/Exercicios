package fundamentos;

public class Temperatura {
	public static void main(String[] args) {
		final int x = 32;
		final int y = 5;
		final int z = 9;
		double fahrenheit = 86;
		double celsius = (fahrenheit - x) * y / z;
		
		System.out.println(celsius);
	}
}
