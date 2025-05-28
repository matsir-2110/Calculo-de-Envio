# Calculo-de-Envio

Una tienda en línea necesita calcular el costo de envío de sus productos. El costo 
depende del peso del paquete y la distancia de envío.

1_ Definir una función 'calcular_costo_envio(peso_kg, distancia_km)' que reciba el peso del paquete en kg (float) y la distancia de envío
en km (int).

Tarifas:

    - Costo base por peso:
        .Hasta 1 kg: $5
        .Más de 1 kg hasta 5 kg: $10
        .Más de 5 kg: $20

    - Costo adicional por distancia: 
        .$0.50 por cada kilómetro.

2_ Definir otra función 'calcular_costo_envio_con_descuento(peso_kg,
distancia_km, cantidad_paquetes)' que:

    _ Esta función debe llamar a calcular_costo_envio para obtener el
       costo base de un solo paquete.
       
    _ Si cantidad_paquetes es 5 o más, aplicar un 10% de descuento sobre
       el costo total (costo base * cantidad_paquetes).
       
    _ Si cantidad_paquetes es 10 o más, aplicar un 15% de descuento sobre
       el costo total.
       
    _ Retornar el costo total con el descuento aplicado
