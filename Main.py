"""
-----------------------------------
Proyecto RSA-Matematica Discreta
-----------------------------------
Autores: 
- Diego Linares -> 221256
- Christian Echeverria -> 221441
"""
import os

def limpiar_pantalla():
    if os.name == 'posix':  # Comprueba si es un sistema tipo UNIX
        input("Presiona Enter para limpiar la pantalla...")
        os.system('clear')
    elif os.name == 'nt':  # Comprueba si es un sistema Windows
        input("Presiona Enter para limpiar la pantalla...")
        os.system('cls')
    else:
        # Si no es un sistema compatible, simplemente espera a que el usuario presione Enter
        input("Presiona Enter para continuar...")
        
def es_primo(numero):
    if numero == '' or numero == '0' or numero == ' ' or numero == '1' or numero == '4':
        return False
    for x in range(2, int(numero) // 2 + 1):
        if int(numero) % x == 0:
            return False
    return True

def obtener_primo():
    while True:
        entrada = input(": ")
        if entrada.strip() == '':
            print("No has ingresado nada. Por favor, ingresa un número.")
            continue 

        if not es_primo(entrada):
            print("El número ingresado no es primo. Inténtalo de nuevo.")
            continue  

        return int(entrada)

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

def find_bezout_identity(a, b):
    # Asegurarse de que a sea mayor o igual que b
    if b > a:
        a, b = b, a

    # Inicializar variables para la identidad de Bezout
    x1, y1 = 1, 0
    x2, y2 = 0, 1

    while b != 0:
        cociente = a // b
        residuo = a % b

        # Actualizar la identidad de Bezout
        temp_x, temp_y = x2, y2
        x2 = x1 - cociente * x2
        y2 = y1 - cociente * y2
        x1, y1 = temp_x, temp_y

        print(f"{a} ÷ {b} = {cociente} con un residuo de {residuo}.")

        a, b = b, residuo

    # El MCD es a, la identidad de Bezout es (x1, y1)
    bezout_identity = (x1, y1, a)
    return bezout_identity

def exp_modular(base, exponente, modulo):
    resultado = 1
    base = base % modulo

    while exponente > 0:
        # Si el exponente es impar, multiplicar el resultado con la base
        if exponente % 2 == 1:
            resultado = (resultado * base) % modulo

        # Ahora exponente es par, dividirlo por 2
        exponente = exponente // 2
        base = (base * base) % modulo
    #Esto es necesario ya que si no podria estar un 12 en lugar de un 0012 lo que haria que no estuviera la ´A´ en la primera.
    resultado_formateado = str(resultado).zfill(4)

    return resultado_formateado

def numero_a_letras(numero):
    # Convertir el numero a una cadena
    numero_str = str(numero)

    # Asegurarse de que la longitud de la cadena sea par agregando un '0' al principio si es necesario
    if len(numero_str) % 2 != 0:
        numero_str = '0' + numero_str
    # Dividir la cadena en bloques de dos caracteres
    bloques = [numero_str[i:i+2] for i in range(0, len(numero_str), 2)]

    # Convertir cada bloque a un numero entero y luego a su representación de letra segun el diccionario
    diccionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras = [diccionario[int(bloque)] for bloque in bloques]

    # Unir las letras en una cadena
    mensaje = ''.join(letras)

    return mensaje


def opcion_descifrar():
    print("Descifrar")
    print("Ingresa el primer numero primo: ")
    numero_p = obtener_primo()
        
    print("Numero primo valido:", numero_p)

    print("Ingresa el segundo numero primo: ")
    numero_q = obtener_primo()

    print("Numero primo valido:", numero_q)
    multiplicacion_pq  = numero_p * numero_q
    producto_pq  = (numero_p - 1) * (numero_q - 1)
    MCD = 0
    numero_e = 0

    while MCD != 1:
        numero_e = int(input(f"Ingresa tu numero e tal que MCD ({producto_pq}, e) sea 1: "))
        MCD = find_MCD(producto_pq, numero_e)
        if MCD != 1:
            print("El MCD no es 1, intentalo de nuevo.")
        
    print("Numero e valido:", numero_e)
    print("La llave publica es: (", numero_e, ",", producto_pq, ")")
    bezout_identity = find_bezout_identity(producto_pq, numero_e)
    print(f"Identidad de Bézout: {bezout_identity[0]} * {producto_pq} + {bezout_identity[1]} * {numero_e} = {bezout_identity[2]}")
    resultado = bezout_identity[1] % producto_pq
    if resultado < 0:
        resultado += producto_pq
    print("d = ",resultado)


    numeros = []

    while True:
        try:
            mensaje = input("Ingresa el mensaje cifrado en bloques de 4 numeros\nEjemplo: 0194 0312 0196\n")
            
            # Dividir la cadena en bloques de 4 caracteres
            bloques = mensaje.split()

            # Iterar sobre cada bloque y convertirlo a un numero
            for bloque in bloques:
                numero = int(bloque)
                numeros.append(numero)

            # Si no hay excepciones (es decir, si todas las conversiones a int fueron exitosas), salir del bucle
            break

        except ValueError:
            print("Error: Ingresa solo números. Intenta de nuevo.")
    # Aplicar la función exp_modular a cada valor en la lista numeros
    resultados_exp_modular = [exp_modular(num, resultado, multiplicacion_pq) for num in numeros]

    # Imprimir los resultados
    for i, resultado_exp_modular in enumerate(resultados_exp_modular):
        print(f"Resultado para numeros[{i}]: {resultado_exp_modular}")

    # Inicializar una cadena para almacenar los mensajes resultantes
    mensaje_resultante = ""

    # Aplicar la funcion numero_a_letras a cada resultado en la lista resultados_exp_modular
    for resultado_exp_modular in resultados_exp_modular:
        letra_resultante = numero_a_letras(resultado_exp_modular)
        mensaje_resultante += letra_resultante

    # Imprimir el mensaje resultante
    print("Mensaje resultante:", mensaje_resultante)
     

def opcion_cifrar():
    print("cifrar")
    print("Ingresa el primer numero primo: ")
    numero_p = obtener_primo()
    print("Numero primo valido:", numero_p)
    
    print("Ingresa el segundo numero primo: ")
    numero_q = obtener_primo()
    print("Numero primo valido:", numero_q)

    producto_pq  = (numero_p - 1) * (numero_q - 1)
    multiplicacion_pq  = 2537
    MCD = 0
    numero_e = 0

    while MCD != 1:
        numero_e = int(input(f"Ingresa tu numero e tal que MCD (e, {producto_pq}) sea 1: "))
        MCD = find_MCD(producto_pq, numero_e)
        if MCD != 1:
            print("El MCD no es 1, intentalo de nuevo.")

    print("Numero valido:", numero_e)
    print("La llave publica es: (", numero_e, ",", multiplicacion_pq, ")")

    palabra = input("Ingresa una palabra: ").upper()
    cifrar_palabra(palabra, numero_e, multiplicacion_pq)


def mostrar_menu():
    texto_ascii = '''
______       # ______      # ________      #
/_____/\      #/_____/\     #/_______/\     #
\:::_ \ \     #\::::_\/_    #\::: _  \ \    #
 \:(_) ) )_   # \:\/___/\   # \::(_)  \ \   #
  \: __ `\ \  #  \_::._\:\  #  \:: __  \ \  #
   \ \ `\ \ \ #    /____\:\ #   \:.\ \  \ \ #
    \_\/ \_\/ #    \_____\/ #    \__\/\__\/ #
              ##             ##               ##    
    '''

    print(texto_ascii)
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
            limpiar_pantalla()
        elif opcion_elegida == 2:
            print("Seleccionaste la Opción 2.")
            opcion_descifrar()
            limpiar_pantalla()
        elif opcion_elegida == 0:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()


    