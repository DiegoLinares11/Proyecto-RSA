def es_primo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, numero // 2):
        if numero % x == 0:
            return False
    return True

def find_MCD(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        cociente = a // b
        residuo = a % b

        print(f"{a} ÷ {b} = {cociente} con un residuo de {residuo}.")
        
        a, b = b, residuo

    return a

def cifrar_palabra(palabra, numero_e, producto_pq):
    numeros = []
    numeros_str = []
    diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(0, len(palabra), 2):
        letra1 = palabra[i]
        letra2 = palabra[i + 1] if i + 1 < len(palabra) else 'A'

        numero1 = diccionario.index(letra1)
        numero2 = diccionario.index(letra2) if letra2 in diccionario else -1

        nn1 = nn2 = sfinal = ''
        nfinal = 0

        if numero1 <= 9 and numero2 > 9:
            nn1 = f"0{numero1}"
            sfinal = f"{nn1}{numero2}"
        elif numero1 > 9 and numero2 <= 9:
            nn2 = f"0{numero2}"
            sfinal = f"{numero1}{nn2}"
        elif numero1 <= 9 and numero2 <= 9:
            nn1 = f"0{numero1}"
            nn2 = f"0{numero2}"
            sfinal = f"{nn1}{nn2}"
        else:
            sfinal = f"{numero1}{numero2}"

        nfinal = pow(int(sfinal), numero_e, producto_pq)
        numeros.append(nfinal)

    for num in numeros:
        if num <= 99:
            numeros_str.append("00" + str(num))
        elif num <= 999:
            numeros_str.append("0" + str(num))
        else: 
            numeros_str.append(str(num))
    
    cadena_cifrada = ' '.join(numeros_str)
    print("Mensaje cifrado")
    print(cadena_cifrada)

def opcion_descifrar():
    print
    

def opcion_cifrar():
    numero_p = 0
    primo = False

    while not primo:
        numero_p = int(input("Ingresa el primer numero primo: "))
        primo = es_primo(numero_p)
        if not primo:
            print("El numero no es primo. Intentalo de nuevo.")

    print("Numero primo valido:", numero_p)

    numero_q = 0
    primo = False

    while not primo:
        numero_q = int(input("Ingresa el segundo numero primo: "))
        primo = es_primo(numero_q)
        if not primo:
            print("El numero no es primo. Intentalo de nuevo.")

    print("Numero primo valido:", numero_q)

    producto_pq  = (numero_p - 1) * (numero_q - 1)
    multiplicacion_pq  = numero_p * numero_q
    MCD = 0
    numero_e = 0

    while MCD != 1:
        numero_e = int(input(f"Ingresa tu numero e tal que MCD ({producto_pq}, e) sea 1: "))
        MCD = find_MCD(producto_pq, numero_e)
        if MCD != 1:
            print("El MCD no es 1, intentalo de nuevo.")

    print("Numero e valido:", numero_e)
    print("La llave publica es: (", numero_e, ",", producto_pq, ")")

    palabra = input("Ingresa una palabra: ").upper()
    cifrar_palabra(palabra, numero_e, multiplicacion_pq)

def mostrar_menu():
    print("Opciones disponibles:")
    print("1. Cifrar palabra")
    print("2. Descifrar palabra")
    print("0. Salir")

def elegir_opcion():
    while True:
        try:
            opcion = int(input("Elige una opción (0-2): "))
            if opcion < 0 or opcion > 2:
                print("Por favor, ingresa una opción válida (0-2).")
            else:
                return opcion
        except ValueError:
            print("Por favor, ingresa un número.")

def main():
    while True:
        mostrar_menu()
        opcion_elegida = elegir_opcion()

        if opcion_elegida == 1:
            print("Seleccionaste la Opción 1.")
            opcion_cifrar()
        elif opcion_elegida == 2:
            print("Seleccionaste la Opción 2.")
            opcion_descifrar()
        elif opcion_elegida == 0:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()


    