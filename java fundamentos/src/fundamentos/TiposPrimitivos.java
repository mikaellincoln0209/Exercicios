package fundamentos;

public class TiposPrimitivos {
	public static void main(String[] args) {
		//Informações Do Funcionario
		
		//Tipos Numericos Inteiros
		byte AnosDeEmpresa = 23;
		short NumeroDeVoos = 542;
		int ID = 56789;
		long PontosAcumulados = 3_134_845_225L;
		
		//Tipos Numericos Reais
		float Salario = 11_445.44F;
		double VendasAcumuladas = 2_991_768_103.01;
		
		//Tipo Booleano
		boolean EstaDeFerias = false; //True
		
		//Tipo caractere
		char Status = 'A'; //ativo
		
		//Dias De Empresa
		System.out.println(AnosDeEmpresa * 365);
		
		//Numero De Viagens
		System.out.println(NumeroDeVoos / 2);
		
		//Pontos Por Real
		System.out.println(PontosAcumulados / VendasAcumuladas);
		
		System.out.println(ID + " ganha --> " + Salario);
		System.out.println("Ferias ?" + EstaDeFerias);
		System.out.println("Status: " + Status);
	}
}
