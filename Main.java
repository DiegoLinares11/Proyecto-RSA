import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int numeroP;
        boolean primo;
        do {
            System.out.println("Ingresa el primer numero primo: ");
            numeroP = scan.nextInt();
            primo = esPrimo(numeroP);

            if (!primo) {
                System.out.println("El numero no es primo. Intentalo de nuevo.");
            }

        } while (!primo);

        System.out.println("Numero primo valido: " + numeroP);

        int numeroQ;
        primo = false;

        do {
            System.out.println("Ingresa el segundo numero primo: ");
            numeroQ = scan.nextInt();
            scan.nextLine();
            primo = esPrimo(numeroQ);

            if (!primo) {
                System.out.println("El numero no es primo. Intentalo de nuevo.");
            }

        } while (!primo);

        System.out.println("Numero primo valido: " + numeroQ);

        int productoPQ = (numeroP - 1) * (numeroQ - 1);

        int MCD;
        int numeroE;
        do {
            System.out.println("Ingresa tu numero e tal que MCD (" + productoPQ + ", e) sea 1");
            numeroE = scan.nextInt();
            scan.nextLine();
            MCD = findMCD(productoPQ, numeroE);

            if (MCD != 1) {
                System.out.println("El MCD no es 1, intentalo de nuevo.");
            }

        } while (MCD != 1);

        System.out.println("Numero e valido: " + numeroQ);

        System.out.println("La llave publica es: (" + numeroE + "," + productoPQ + ")");
        //////////////////////////////////////////////////////////////////////////////////////////////////////
        // Pedir al usuario que ingrese una palabra

        System.out.println("Ingresa una palabra: ");
        String palabra = scan.nextLine().toUpperCase(); // Convertir la palabra a mayusculas
        
        separarPalabra(palabra, numeroE, productoPQ);
    }

    public static boolean esPrimo(int numero) {
        // El 0, 1 y 4 no son primos
        if (numero == 0 || numero == 1 || numero == 4) {
            return false;
        }
        for (int x = 2; x < numero / 2; x++) {
            // Si es divisible por cualquiera de estos numeros, noes primo
            if (numero % x == 0)
                return false;
        }
        // Si no se pudo dividir por ninguno de los de arriba, si es primo
        return true;

    }

    public static int findMCD(int a, int b) {
        // Asegurarse de que a sea mayor o igual que b
        if (b > a) {
            int temp = a;
            a = b;
            b = temp;
        }

        while (b != 0) {
            int cociente = a / b;
            int residuo = a % b;

            System.out.println(a + " ÷ " + b + " = " + cociente + " con un residuo de " + residuo + ".");

            a = b;
            b = residuo;
        }

        return a;
    }

    public static void separarPalabra(String palabra, int numeroE, int productoPQ) {
        String nn1;
        String nn2;
        String sfinal;
        double nfinal;

        ArrayList<Double> numeros = new ArrayList<>();
        String diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // Recorrer la palabra en bloques de dos letras
        for (int i = 0; i < palabra.length(); i += 2) {
            char letra1 = palabra.charAt(i);
            char letra2 = (i + 1 < palabra.length()) ? palabra.charAt(i + 1) : 'A';

            // Obtener el número correspondiente a cada letra
            int numero1 = diccionario.indexOf(letra1);
            int numero2 = diccionario.indexOf(letra2);

            // Imprimir el resultado
            System.out.printf("%c%c = %02d%02d%n", letra1, letra2, numero1, numero2);
            System.out.println(numero1);

            if (numero2 != -1) {
                System.out.println(numero2);
            }
            
            if (numero1 <= 9 && numero2 > 9) {
                nn1 = "0" + numero1;
                sfinal = nn1 + numero2;
            } else if (numero1 > 9 && numero2 <= 9) {
                
                nn2 = "0" + numero2;
                sfinal = numero1 + nn2;

            }else if (numero1 <= 9 && numero2 <= 9){
                nn1 = "0" + numero1;
                nn2 = "0" + numero2;
                sfinal = nn1 + nn2;

            } else {
                sfinal = Integer.toString(numero1) + Integer.toString(numero2);
            }

            nfinal = (Math.pow(Integer.parseInt(sfinal), productoPQ)) % productoPQ;
            numeros.add(nfinal);
        }
        
        System.out.println(numeros);
    }


}