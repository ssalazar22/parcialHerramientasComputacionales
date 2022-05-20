## Estudiantes: Santiago Salazar Gil y Fabian David Trochez
## Codigos: 8970728 y 8970267

producto01 = "Huevos"
producto02 = "Leche"
producto03 = "Milo"
producto04 = "Ensalada"
producto05 = "Papitas"
producto06 = "Galletas"
producto07 = "Gaseosa"
producto08 = "Carne"
producto09 = "Cafe"
producto10 = "Pan"
producto11 = "Chocolate"

print("Bienvenido a la cafeteria de la Pontificia Universidad Javeriana, que desea comprar el dia de hoy?")
print("Codigo 01: ", producto01)
print("Codigo 02: ", producto02)
print("Codigo 03: ", producto03)
print("Codigo 04: ", producto04)
print("Codigo 05: ", producto05)
print("Codigo 06: ", producto06)
print("Codigo 07: ", producto07)
print("Codigo 08: ", producto08)
print("Codigo 09: ", producto09)
print("Codigo 10: ", producto10)
print("Codigo 11: ", producto11)

def cafeteriasUniversidad():
    cedula = input("Numero de cedula: ")
    rol = input("Profesor o estudiante: ")
    while rol != "profesor" and rol != "estudiante":   
        rol = input("Digite bien la informacion, profesor o estudiante: ")
    if rol == "estudiante": 
        becas = input("Pertenece usted al programa de becas?: ")  
        while becas != "si" and becas != "no":
            becas = input("Digite bien la informacion, pertenece usted al programas de becas?: ")
    compra = True
    precioAcumulado = 0
    masDeUnaCompra = False
    while compra == True:
        codigoProducto = input("Codigo del producto: ")
        while codigoProducto != "01" and codigoProducto != "02" and codigoProducto != "03" and codigoProducto != "04" and codigoProducto != "05" and codigoProducto != "06" and codigoProducto != "07" and codigoProducto != "08" and codigoProducto != "09" and codigoProducto != "10" and codigoProducto != "11":
            codigoProducto = input("El codigo solicitado no esta relacionado con ningun producto, por favor digite un codigo valido: ")
        cantidadUnidades = int(input("Catidad de unidades a comprar: "))
        precioProducto = int(input("Precio del producto: "))
        precioTotalAPagar = cantidadUnidades * precioProducto
        if rol == "estudiante": 
            if becas == "si": 
                precioTotalAPagar = (precioTotalAPagar * 50) / 100
            else: 
                precioTotalAPagar = (precioTotalAPagar * 70) / 100
        elif rol == "profesor": 
            precioTotalAPagar = (precioTotalAPagar * 80) / 100
        otraCompra = input("Desea comprar otro producto?: ")
        while otraCompra != "si" and otraCompra != "no":
            otraCompra = input("Digite bien la informacion, desea comprar otro producto?: ")
        if otraCompra == "no": 
            compra = False
        else: 
            compra = True
            masDeUnaCompra = True
        precioAcumulado = precioAcumulado + precioTotalAPagar
    if masDeUnaCompra == False:
        print("El", rol, "con cedula", cedula, "debe pagar", "$", int(precioAcumulado), "por el producto", codigoProducto)
    else: 
        print("El", rol, "con cedula", cedula, "debe pagar", "$", int(precioAcumulado), "por todos los productos seleccionados")

cafeteriasUniversidad()