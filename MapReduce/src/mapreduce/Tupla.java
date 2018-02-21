package mapreduce;

/*
 * Classe que guarda una parella de valors.
 */
public class Tupla<C> {
	
	private final C clau;
	private final int valor;
	
	public Tupla(C clau, int valor) {
		this.clau = clau;
		this.valor = valor;
	}
	
	public C getClau() {
		return this.clau;
	}
	
	public int getValor() {
		return this.valor;
	}
	
	/*
	 * Comprova si la clau de la tupla actual és igual a la clau de una
	 * tupla dónada.
	 */
	public boolean clauEsIgual(Tupla<C> tupla) {
		return this.clau.equals(tupla.getClau());	
	}
}
