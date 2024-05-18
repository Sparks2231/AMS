"""elabora un programa en python que calcule el area de un rectángulo, considera lo siguiente:
1. La función recibira 2 parametros, la base y la altura, y devolvera el area.
2. En el programa principal la base tendra un valor de 5 y la altura un valor de 10.
3. En el programa principal se imprimira el resultado correspondiente"""

def calcular_area(a,b):
    area=a*b
    return area
a=5
b=10

AreaR=calcular_area(a,b)
print ("El area del rectángulo es: ", AreaR)
