package mapreduce;

import java.util.ArrayList;

/*
 * Classe que genera un registre on es guarda cada vegada que apareix una paraula
 * dins d'un text o conjunt de textos determinat.
 */
public class MapParaules {
	
	/*
	 * Prova. 
	 */
	public static void main(String args[]) {
		
		MapParaules map = new MapParaules();
		
		ArrayList<String> llista = new ArrayList<String>();
		
		llista.add("A");
		llista.add("B");
		llista.add("C");
		llista.add("B");
		llista.add("A");
		llista.add("A");
 		llista.add("B");
		llista.add("A");
		
		ArrayList<Tupla<String>> diccionariParaules = map.mapping(llista);
		
		for (Tupla<String> tupla : diccionariParaules) {
			System.out.println(tupla.getClau() + " " + tupla.getValor());
		}
	}
	
	/*
	 * Dividieix els fitxers de text per a que els pugui processar el generador de Tuples.
	 */
	public void splitting(String nomFitxer) {
		int contador = 0;
		
		while (contador < 100 /* || no s'ha trobat un punt*/) {
			contador++;
		}
		
	}

	/*
	 * Conta el nombre de vegades que apareixen les paraules d'un fragment determinat.
	 */
	public ArrayList<Tupla<String>> mapping(ArrayList<String> fragment) {
		ArrayList<Tupla<String>> registreContadorParaules = new ArrayList<Tupla<String>>();
		
		for (String paraulaActual : fragment) {
			Tupla<String> novaTupla = new Tupla<String>(paraulaActual, 1);
			registreContadorParaules.add(novaTupla);
		}
		
		return registreContadorParaules;
	}

}
