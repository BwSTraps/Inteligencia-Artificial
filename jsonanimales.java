package jsonv2animals;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

public class jsonanimales {
		 
	 public static void main(String[] args) {
		 BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
		 
	        JSONParser parser = new JSONParser();
	        String animal="";
    		String tiene="";
    		String vive="";    		String pivote=animal;
    		String pertenece="";
	        
	        try {
	            
	            Object obj = parser.parse(new FileReader("prueba.json"));
	            JSONObject jsonObject = (JSONObject) obj;
	            System.out.println("JSON LEIDO: " + jsonObject);
	            
	            JSONArray array = (JSONArray) jsonObject.get("base");
	            System.out.println("");
	            int contnivel1 = 0;
	            int contnivel5 = 0;
	            
	            for(int i = 0 ; i < array.size() ; i++) {
	                JSONObject jsonObject1 = (JSONObject) array.get(i);
	                if (jsonObject1.get("nivel1") != null){
	                	contnivel1 ++;
	                }
	                if (jsonObject1.get("nivel5") != null){
	                	contnivel5 ++;
	                }	               
	            }
	            
	            String [][] base = new  String [contnivel1] [2];
	            String [][] base2 = new String [contnivel5][3];
	            
	            int contllenarb1 =0;
	            int contllenarb2 =0;
	            
	            for(int i = 0 ; i < array.size() ; i++) {
	                JSONObject jsonObject1 = (JSONObject) array.get(i);
	                if (jsonObject1.get("nivel1") != null){
	                	contllenarb1++;
	                	base[contllenarb1-1][0]=jsonObject1.get("nivel1")+"";
	                	base[contllenarb1-1][1]=jsonObject1.get("nivel2")+"";
	                }
	                if (jsonObject1.get("nivel5") != null){
	                	contllenarb2++;
	                	base2[contllenarb2-1][0]=jsonObject1.get("nivel3")+"";
	                	base2[contllenarb2-1][1]=jsonObject1.get("nivel4")+"";
	                	base2[contllenarb2-1][2]=jsonObject1.get("nivel5")+"";
	                }

	            }
	            
	            int repetir = 0;
	            do{	
		    		System.out.println("Ingresa animal");
		    		animal=entrada.readLine();
		    		System.out.println("Ingresa que tiene");
		    		tiene=entrada.readLine();
		    		System.out.println("Ingresa donde vive");
		    		vive=entrada.readLine();
		    		System.out.println("Ingresa a donde pertenece");
		    		pertenece=entrada.readLine();

		    		int cont3=0;
		    		pivote=animal;

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
	    				
	    				System.out.println("¿Quiere ingresar otro animal?");
	    				System.out.println("0 = SI \n 1 = NO");
	    				
			    		repetir=Integer.parseInt(entrada.readLine());
	    				
	            } while (repetir == 0);
	            
	        } catch(FileNotFoundException e) { }
	        catch(IOException e) { }
	        catch(ParseException e) { }
	        
	    }
}