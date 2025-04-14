def leap_year():

    año = int(input("Ingrese un año:"))

    if(año % 4 == 0) and (año % 100 != 0): 
        respuesta = "es bisiesto"
    elif(año % 4 == 0) and (año % 400 == 0):
        respuesta = "es bisiesto"
    else:
        respuesta = "no es bisiesto"

    print (f"El año {año} {respuesta}")

