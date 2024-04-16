import os

os.system("cls")
#ciclo repeticion for -> para
#for x in range(3): #-> siempre hay que ingresar un entero Siempre es for in
 #    print ("se portaron bien el sabado") #toma desde el 0 hasta el penultimo nro
     

try: #controlo la cantidad de notas a promediar
    contadorNota = 0
    cantidad = int(input("ingrese cantidad de notas a promediar\n"))
    for x in range (cantidad):
        nota = float(input(f"ingrese nota {X+1}\n"))
        contadorNota = contadorNota + nota     
    promedio = round(contadorNota/cantidad )
    promedioRedondeado = round(promedio, 1)
    print(f"el resultado de las {cantidad} notas es:  {promedioRedondeado}")
except:
    print("tipo de dato no es compatible")