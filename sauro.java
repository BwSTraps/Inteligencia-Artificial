package cladistica;

public class sauro {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String [][] base= {
				{"tortuga","queratina"},
				{"gallo","queratina"},
				{"cocodrilo","queratina"},
				{"iguana","queratina"},
				
				
				{"gato","gm"},
				{"oso","gm"},
				{"ballena","gm"},
				{"delfin","gm"},
				
				
				{"queratina","oviparo"},
				{"oviparo","sauropsido"},
				{"sauropsido","tetrapodo"},
				
				
				{"gm","viviparo"},
				{"viviparo","mamalia"},
				{"mamalia","tetrapodo"},
				
				
				{"tetrapodo","vertebrado"}
		};
		
		//1 tiene
		//2 vive en
		
		String [][] base2= {
				{"tortuga","queratina","1"},
				{"tortuga","agua","2"},
				{"tortuga","tierra","2"},
				
				{"gallo","queratina","1"},
				{"gallo","garras","1"},
				{"gallo","tierra","2"},
				
				{"cocodrilo","queratina","1"},
				{"cocodrilo","garras","1"},
				{"cocodrilo","tierra","2"},
				{"cocodrilo","agua","2"},
				
				{"iguana","queratina","1"},
				{"iguana","garras","1"},
				{"iguana","tierra","2"},
				
				{"gato","pelo","1"},
				{"gato","G. mamarias","1"},
				{"gato","tierra","2"},
				
				{"oso","pelo","1"},
				{"oso","G. mamarias","1"},
				{"oso","tierra","2"},
				
				{"ballena","agua","2"},
				{"ballena","G. mamarias","1"},
				

				{"delfin","agua","2"},
				{"delfin","G. mamarias","1"},
				
		};
		
		String animal="cocodrilo";
		String tiene="garras";
		String vive="tierra";
		String pivote=animal;
		String pertenece="viviparo";
		int cont3=0;
			
				for(int x=0;x<base.length;x++) {
				if(pivote.equals(base[x][0])) {
					System.out.println(base[x][0]+"  es  "+base[x][1]);
					pivote=base[x][1];
					if(pertenece.equals(pivote)) {
						cont3++;
					}
				}
				}
				System.out.println(""+cont3);
				System.out.println("\n");
				
				int cont = 0;
				int cont2 = 0;
				
				for(int x=0;x<base2.length;x++) {
					if(animal.equals(base2[x][0])) {
						
						if(base2[x][2].equals("1")) {System.out.println(base2[x][0]+"  tiene  "+base2[x][1]);
						
						if(base2[x][1].equals(tiene)) {cont++;}
						}
						if(base2[x][2].equals("2")) {System.out.println(base2[x][0]+"  vive en  "+base2[x][1]);
						
						if(base2[x][1].equals(vive)) {cont2++;}
						
						}
						
						
					}
					}
			
				if(cont>0) {
					System.out.println(""+animal+" si tiene "+tiene);
				}
				else {System.out.println("FALSO el "+animal+" NO tiene "+tiene);}
				if(cont2>0) {
					System.out.println(""+animal+" si vive en "+vive);
						
				}
				else {
					System.out.println("FALSO el "+animal+" NO vive en "+vive);
				}
				
				if(cont3>0) {
					System.out.println(""+animal+" pertenece al grupo "+pertenece);
						
				}
				else {
					System.out.println("FALSO el "+animal+" NO pertenece al grupo "+pertenece);
				}
				
	}

}
