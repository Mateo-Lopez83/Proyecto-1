package proy2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Principal {
	
	

	public static void main(String[] args) throws Exception {
		Principal instancia = new Principal();
		int cases = 1;
		HashSet<Integer> atomos_libres= new HashSet<Integer>();
		ArrayList<Vertice> parejas = new ArrayList<>();
		HashMap<Integer, Integer> num_indice = new HashMap<Integer, Integer>();
		HashMap<Integer, Integer> indice_num = new HashMap<Integer, Integer>();
		parejas.add(new Vertice(1,3));
		parejas.add(new Vertice(-6,3));
		parejas.add(new Vertice(1,7));
		int w1 = 3;
		int w2 = 5;
		int tamanio = parejas.size();
		int contador = 0;
		for (Vertice pareja:parejas) {
			if (!indice_num.containsValue(pareja.v1)) {
				indice_num.put(contador, pareja.v1);
				num_indice.put(pareja.v1, contador);
				contador++;
			}
			if (!indice_num.containsValue(pareja.v2)) {
				indice_num.put(contador, pareja.v2);
				num_indice.put(pareja.v2, contador);
				contador++;
			}
			if (!indice_num.containsValue(-pareja.v1)) {
				indice_num.put(contador, -pareja.v1);
				num_indice.put(-pareja.v1, contador);
				contador++;
			}
			if (!indice_num.containsValue(-pareja.v2)) {
				indice_num.put(contador, -pareja.v2);
				num_indice.put(-pareja.v2, contador);
				contador++;
			}
			
			atomos_libres.add(pareja.v1);
			atomos_libres.add(pareja.v2);
			atomos_libres.add(-pareja.v1);
			atomos_libres.add(-pareja.v2);
			int[][]matriz = instancia.matrizInicial(tamanio, w1,w2, indice_num);
		}
		
		
		
		
		
		
	}
	
	
	
	public int calc_LTP (int m1, int m2, int w1, int w2) {
		if ((m1>= 0 && m2>=0 )|| (m1<0 && m2<0)) return 1+ (Math.abs(Math.abs(m1)-Math.abs(m2))%w1);
		else return w2 - (Math.abs(Math.abs(m1)-Math.abs(m2))%w2);
	}
	public int[][] matrizInicial (int n, int w1, int w2, HashMap<Integer, Integer> indice_num){
		int[][] matriz = new int[n][n];
		for (int i =0; i<n; i++) {
			for (int j = 0; j<n; j++) {
				int m1 = indice_num.get(i);
				int m2 = indice_num.get(j);
				if (m1==m2) matriz[i][j] = (int) 10e7;
				else matriz[i][j] = calc_LTP(m1,m2, w1, w2);
			}
		}
		 for (int i = 0; i < n; i++) {
	            for (int j = 0; j < n; j++) {
	                System.out.print(matriz[i][j] + " ");
	            }
	            System.out.println(); 
		 }
		return matriz;
	}
	
	
}
class Vertice{
	public int v1;
	public int v2;
	public Vertice(int v1, int v2) {
		this.v1 = v1;
		this.v2 = v2;
	}
}
