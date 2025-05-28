#Funciones para Cálculo de Costos de Envío

#Funcion 1
def calcular_costo_envio(peso_kg, distancia_km):
    if peso_kg <= 1:
        plata = 5
    elif peso_kg > 1 and peso_kg <= 5:
        plata = 10
    elif peso_kg > 5:
        plata = 20
        
    plata += distancia_km * 0.5
    return plata


plata_fin = 0
#Funcion 2
def calcular_costo_envio_con_descuento(peso_kg, distancia_km, cantidad_paquetes):
    if cantidad_paquetes >= 5 and cantidad_paquetes < 10:
        plata_fin = (calcular_costo_envio(peso_kg, distancia_km) * cantidad_paquetes) -  (calcular_costo_envio(peso_kg, distancia_km) * cantidad_paquetes) * 0.1
    elif cantidad_paquetes >= 10:
        plata_fin = (calcular_costo_envio(peso_kg, distancia_km) * cantidad_paquetes) - (calcular_costo_envio(peso_kg, distancia_km) * cantidad_paquetes) * 0.15
    return plata_fin

#Input de Valores
while True:
    peso_kg = float(input("Peso del alimento (kg): "))
    distancia_km = int(input("Distancia de envío del paquete (km): "))
    cantidad_paquetes = int(input("Cantidad de paquetes: "))

    if peso_kg < 0 or distancia_km < 0 or cantidad_paquetes < 0:
        print("Uno de los valores ingresados es negativo. Vuelva a ingresar")
    else:
        break

#Imprimir resultados
if cantidad_paquetes < 5:
    print("El precio final a pagar es: ", calcular_costo_envio(peso_kg, distancia_km) * cantidad_paquetes)
else:
        print("El precio final a pagar con descuento incluido es: ", calcular_costo_envio_con_descuento(peso_kg, distancia_km, cantidad_paquetes))