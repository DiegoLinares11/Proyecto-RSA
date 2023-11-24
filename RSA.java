import java.util.Scanner;

public class RSA {
    public static boolean esPrimo(int numero) {
        if (numero == 0 || numero == 1 || numero == 4) {
            return false;
        }
        for (int x = 2; x <= numero / 2; x++) {
            if (numero % x == 0) {
                return false;
            }
        }
        return true;
    }

    public static int findMCD(int a, int b) {
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

    public static void cifrarPalabra(String palabra, int numeroE, int productoPQ) {
        StringBuilder numerosStr = new StringBuilder();
        String diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        for (int i = 0; i < palabra.length(); i += 2) {
            char letra1 = palabra.charAt(i);
            char letra2 = (i + 1 < palabra.length()) ? palabra.charAt(i + 1) : 'A';

            int numero1 = diccionario.indexOf(letra1);
            int numero2 = (diccionario.indexOf(letra2) != -1) ? diccionario.indexOf(letra2) : -1;

            String nn1 = "", nn2 = "", sfinal;
            int nfinal;

            if (numero1 <= 9 && numero2 > 9) {
                nn1 = "0" + numero1;
                sfinal = nn1 + numero2;
            } else if (numero1 > 9 && numero2 <= 9) {
                nn2 = "0" + numero2;
                sfinal = numero1 + nn2;
            } else if (numero1 <= 9 && numero2 <= 9) {
                nn1 = "0" + numero1;
                nn2 = "0" + numero2;
                sfinal = nn1 + nn2;
            } else {
                sfinal = "" + numero1 + numero2;
            }

            nfinal = (int) Math.pow(Integer.parseInt(sfinal), numeroE) % productoPQ;
            String formattedNum = String.format("%04d", nfinal);
            numerosStr.append(formattedNum).append(" ");
        }

        System.out.println("Mensaje cifrado");
        System.out.println(numerosStr.toString().trim());
    }

    public static void opcionDescifrar() {
        System.out.println("Descifrar");
        // Implementa la lógica de descifrado si es necesario
    }

    public static void opcionCifrar() {
        int numeroP = 0;
        boolean primo = false;
        Scanner scanner = new Scanner(System.in);

        while (!primo) {
            System.out.print("Ingresa el primer numero primo: ");
            numeroP = scanner.nextInt();
            primo = esPrimo(numeroP);
            if (!primo) {
                System.out.println("El numero no es primo. Intentalo de nuevo.");
            }
        }

        System.out.println("Numero primo valido: " + numeroP);

        int numeroQ = 0;
        primo = false;

        while (!primo) {
            System.out.print("Ingresa el segundo numero primo: ");
            numeroQ = scanner.nextInt();
            primo = esPrimo(numeroQ);
            if (!primo) {
                System.out.println("El numero no es primo. Intentalo de nuevo.");
            }
        }

        System.out.println("Numero primo valido: " + numeroQ);

        int productoPQ = (numeroP - 1) * (numeroQ - 1);
        int multiplicacionPQ = numeroP * numeroQ;
        int MCD = 0;
        int numeroE = 0;

        while (MCD != 1) {
            System.out.print("Ingresa tu numero e tal que MCD (" + productoPQ + ", e) sea 1: ");
            numeroE = scanner.nextInt();
            MCD = findMCD(productoPQ, numeroE);
            if (MCD != 1) {
                System.out.println("El MCD no es 1, intentalo de nuevo.");
            }
        }

        System.out.println("Numero e valido: " + numeroE);
        System.out.println("La llave publica es: (" + numeroE + ", " + productoPQ + ")");

        System.out.print("Ingresa una palabra: ");
        String palabra = scanner.next().toUpperCase();
        cifrarPalabra(palabra, numeroE, multiplicacionPQ);
    }

    public static void mostrarMenu() {
        System.out.println("Opciones disponibles:");
        System.out.println("1. Cifrar palabra");
        System.out.println("2. Descifrar palabra");
        System.out.println("0. Salir");
    }

    public static int elegirOpcion() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                System.out.print("Elige una opción (0-2): ");
                int opcion = scanner.nextInt();
                if (opcion < 0 || opcion > 2) {
                    System.out.println("Por favor, ingresa una opción válida (0-2).");
                } else {
                    return opcion;
                }
            } catch (java.util.InputMismatchException e) {
                System.out.println("Por favor, ingresa un número.");
                scanner.next(); // Limpiar el búfer de entrada
            }
        }
    }

    public static void main(String[] args) {
        while (true) {
            mostrarMenu();
            int opcionElegida = elegirOpcion();

            if (opcionElegida == 1) {
                System.out.println("Seleccionaste la Opción 1.");
                opcionCifrar();
            } else if (opcionElegida == 2) {
                System.out.println("Seleccionaste la Opción 2.");
                opcionDescifrar();
            } else if (opcionElegida == 0) {
                System.out.println("Saliendo del programa...");
                break;
            }
        }
    }
}