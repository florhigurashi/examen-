#Realizar un programa en Python que conste de la conversión de °C a °F, °K.
#El mismo debe permitirle al usuario el ingreso del número a convertir en el tipo
# de dato que se considere correspondiente y con un mensaje que justifique cada conversión 
# mostrándolo por pantalla.

def conversion_grados():
    
    grados_centigrados=float(input("Ingrese los grados centigrados que desea convertir: "))
    
    grados_farenheit= grados_centigrados/33.8
    grados_kelvin= grados_centigrados/ 274.15

    print(f"La cantidad de {grados_centigrados}grados farenheit es igual a: {grados_farenheit}")
    print(f"La cantidad de {grados_centigrados} grados kelvin es igual a: {grados_kelvin}")

conversion_grados()