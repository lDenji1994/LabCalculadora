print(" 1- Suma. \n 2- Resta. \n 3- Multiplicacion. \n 4 - Divicion.")
entrada = int(input("Bienvenido porfavor seleccione una opcion "))

while entrada != 0:
    entrada = int(input("Bienvenido porfavor seleccione una opcion "))

    if entrada == 1:
        entrada2 = int(input("Desea seguir sumando (si 1 : no 0): "))
        while entrada2 !=0: 
            a = int(input("ingrese el primer numero: "))
            b = int(input("ingrese el segundo numero: "))

            suma = a + b
            print("Resultado de la suma: " , suma)
            entrada2 = int(input("Desea seguir sumando (si 1 : no 0): "))

    if entrada == 2:
        entrada2 = int(input("Desea seguir restando (si 1 : no 0): "))
        while entrada2 !=0: 
            a = int(input("ingrese el numero mayor: "))
            b = int(input("ingrese el numero menor: "))

            resta = a - b
            print("Resultado de la resta: " , resta)
            entrada2 = int(input("Desea seguir restando (si 1 : no 0): "))

    if entrada == 3:
        entrada2 = int(input("Desea seguir multiplicando (si 1 : no 0): "))
        while entrada2 !=0: 
            a = int(input("ingrese el primer numero : "))
            b = int(input("ingrese el segundo numero : "))

            multiplicacion = a * b
            print("Resultado de la multiplicacion: " , multiplicacion)
            entrada2 = int(input("Desea seguir multiplicando (si 1 : no 0): "))

    if entrada == 4:
        entrada2 = int(input("Desea seguir dividiendo (si 1 : no 0): "))
        while entrada2 !=0: 
            a = int(input("ingrese el primer numero : "))
            b = int(input("ingrese el segundo numero : "))

            divicion = a / b
            print("Resultado de la divicion: " , divicion)
            entrada2 = int(input("Desea seguir dividiendo (si 1 : no 0): "))