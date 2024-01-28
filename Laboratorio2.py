print("\n\t  Menu Principal.\n")

print(" 1. ¡Hola Mundo!.\n 2. Almacenar Cadena.\n 3. Nombre de Usuario.\n 4. Operacion Aritmetica.\n 5. Pago por Horas.\n 6. Salir. ")

try:
    opc = int(input("\nIngrese una opcion (1-6): "))
    if opc == 1:
        print("\n¡Hola mundo!")

    if opc == 2:
        cadena = "hola mundo."
        result = cadena.capitalize()
        print(result)

    if opc == 3:
        print("\nNombre de Usuario.\n")
        nombre = input("Ingrese su nombre: ")
        nombre = nombre.lower()
        nombre = nombre.capitalize()
        respuesta = "HOLA"
        respuesta = respuesta.lower()

        result = print(f"¡{respuesta.capitalize()} {nombre}!")

    if opc == 4:
        print("\nOperacion Aritmetica: (3+2/2*5)^2\n")
        operacion = ((3+2)/(2*5))**2
        respuesta = str(operacion)
        digitos = len(respuesta)

        result = print(f"El resultado de la operacion es: {respuesta} y tiene {digitos-1} digitos.")

    if opc == 5:
        print("\nPago por Horas.\n")
        horas_trabajadas = int(input("ingrese la horas trabajadas: "))
        coste_por_hora = float(input("ingrese su coste por horta: "))
        salario = horas_trabajadas * coste_por_hora

        result = print(f"Su pago correspondiente es de: Q.{salario}")

    if opc == 6:
        print("Saliendo del programa...")

except:
    print("Opcion incorrecta...")