package fundamentos;

import java.util.Scanner;

public class Convers�o {
	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		
		System.out.print("Informe o primeiro salario:\n");
		String valor1 = entrada.next().replace("," , ".");
		
		System.out.print("Informe o segundo salario:\n");
		String valor2 = entrada.next().replace("," , ".");
		
		System.out.print("Informe o terceiro salario:\n");
		String valor3 = entrada.next().replace("," , ".");
		
		double salario1 = Double.parseDouble(valor1);
		double salario2 = Double.parseDouble(valor2);
		double salario3 = Double.parseDouble(valor3);
		
		double media = (salario1 + salario2 + salario3) /3;
		System.out.println("A media entre os sal�rios � " + media);
		
		entrada.close();
	}

}
