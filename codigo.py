def recPed(nombresTodasComidas):
    
    comida = ""
    cantidad = 0
    while(True):
        comida = input("Ingrese plato: ")
        if(comida.lower() in nombresTodasComidas):
            break
        else:
            print("Error: Ingresar de nuevo")
    
    while(True):
        try:
            cantidad = int(input(">>Cantidad de platos: "))
            if(int(cantidad) >= 1):
                break
            else:
                print("debe ingresar un valor mayor o igual a 1")
        except:
            print("ingrese valor entero")
    
    return [comida.capitalize(), cantidad]

class Comida:

    def __init__(self, nombreComida, precio):
        self.nombreComida = nombreComida
        self.precio = precio
    
    def getNombre(self):
        return self.nombreComida

    def getPrecio(self):
        return self.precio     
    
    def __str__(self):
        return f"{self.nombreComida.capitalize()}, ${self.precio}"
    
    def __repr__(self):
        return str(self.__dict__)
    

def diccionarioTotal(dicc1, dicc2):
    mezcla = {**dicc1, **dicc2}
    return mezcla

    
def menu():
    diccionarioComidas = {"Segundo":[], "Sopas":[], "Entradas":[]}
    diccionarioEspeciales = {"Especialidad del chef":[]}

    arregloCriollo = diccionarioComidas.get("Segundo")
    arregloCriollo.append(Comida("pollo frito", 5))
    arregloCriollo.append(Comida("Encebollado", 5))
    arregloCriollo.append(Comida("Bollo", 5))
    arregloSopas = diccionarioComidas.get("Sopas")
    arregloSopas.append(Comida("sopa crema", 5))
    arregloSopas.append(Comida("fideo", 5))
    arregloSopas.append(Comida("sopa de pollo", 5))
    arregloPostres = diccionarioComidas.get("Entradas")
    arregloPostres.append(Comida("croissant", 5))
    arregloPostres.append(Comida("pie", 5))
    arregloPostres.append(Comida("Batido", 5))
    arregloChef = diccionarioEspeciales.get("Especialidad del chef")
    arregloChef.append(Comida("Huevo frito",7 ))
    arregloChef.append(Comida("Chancho", 8))
    arregloChef.append(Comida("Bolon", 7))

    diccionarioFinal = diccionarioTotal(diccionarioComidas, diccionarioEspeciales)

    resultado = []
    for valor1 in diccionarioFinal.values():
        for valor2 in valor1:
            resultado.append(valor2.getNombre().lower())
    todasComidas = resultado

    resultado = []
    for valor1 in diccionarioEspeciales.values():
        for valor2 in valor1:
            resultado.append(valor2.getNombre().lower())
    todasEspeciales = resultado

    diccionarioNuevo = {}

    for valor1 in diccionarioFinal.values():
        for valor2 in valor1:
            diccionarioNuevo[valor2.getNombre().lower()] = valor2.getPrecio()

    todosPrecios = diccionarioNuevo

    return diccionarioFinal, todasComidas, todasEspeciales, todosPrecios

diccionarioFinal, todasComidas, todasEspeciales, todosPrecios = menu()


def calPre(misPedidos, todosPrecios, comidasEspeciales):

    tamanioPedido = 0
    precioInicial = 0
    cantidadDeEspeciales = 0
    recargoPorEspeciales = 0
    
    for pedido in misPedidos:
        nombre = pedido[0]
        cantidad = pedido[1]
        precioUnitario = todosPrecios.get(nombre.lower())

        print(f"Platos: {nombre}, cantidad: {cantidad}, precio por unidad: ${todosPrecios.get(nombre.lower())}")
        precioInicial = precioInicial + (precioUnitario*cantidad)
        tamanioPedido = tamanioPedido + cantidad

        if(nombre.lower() in comidasEspeciales):
            cantidadDeEspeciales = cantidadDeEspeciales + cantidad
            recargoPorEspeciales = recargoPorEspeciales + 0.05*(cantidad*precioUnitario)

    print(f"\nNumero de platos: {tamanioPedido}.  Precio standard: ${'{:.2f}'.format(precioInicial)}.")

    if(tamanioPedido <= 100):
        
        if((tamanioPedido > 5) and ( tamanioPedido <= 10)):
            precioInicial = precioInicial*0.9
            print(f"\nSe pidieron entre 5 y 10 comidas (-10%): ${'{:.2f}'.format(precioInicial)}")
        
        if((tamanioPedido > 10)):
            precioInicial = precioInicial*0.8
            print(f"\nSe pidieron mas de 10 comidas (-20%): ${'{:.2f}'.format(precioInicial)}")
        
        if((precioInicial > 50) and (precioInicial <= 100)):
            precioInicial = precioInicial-10
            print(f"\nCosto entre $50 y $100 (-10$): ${'{:.2f}'.format(precioInicial)}")

        if(precioInicial > 100):
            precioInicial = precioInicial-25
            print(f"\nCosto mayor a $100 (-25$): ${'{:.2f}'.format(precioInicial)}")

        if(cantidadDeEspeciales>0):
            precioInicial = precioInicial+recargoPorEspeciales
            print(f"\nSe pidio {cantidadDeEspeciales} platos especiales (+5% del valor de cada plato especial -> +{'{:.2f}'.format(recargoPorEspeciales)}): ${'{:.2f}'.format(precioInicial)}")

        return round(precioInicial, 2)

    else:
        return -1


def inicio():
    
    diccionarioComidasporTipo, nombresTodasComidas, nombresEspeciales, NombreyPrecioTodos = menu()
    
    print("Bienvenido , este es nuestro menu: \n")

    for valor1 in diccionarioComidasporTipo.keys():
        print(f"***********{valor1.upper()}***********")
        for valor2 in diccionarioComidasporTipo.get(valor1):
            print(valor2.getNombre() + " -> " + str(valor2.getPrecio()) + "$")
        print("\n")

    print("¿Desea hacer un pedido?, Si/No")
  
    pedido = "No"

    while(True):
        pedir = input("Ingrese opción: ")
        try:
            if( str(pedir).upper() == "SI"):
                pedido = "SI"
                break
            elif( str(pedir).upper() == "NO" ):
                pedido = "NO"
                break
            else:
                print("Opcion no valida, intente nuevamente")
        except:
            print("Ingrese solo (Si o No)")
    
    hacePed = pedido

    

    if(hacePed == "SI"):
        print("\n")

        pedidos = []
        pedido = recPed(nombresTodasComidas)
        pedidos.append(pedido)
        
        print("\nGustaria seguir pidiendo?, Si/No")

        while(True):
            sigue = input("     >>Ingrese opcion: ")
            
            if( str(sigue).upper() == "SI"):
                print("\n")
                pedido = recPed(nombresTodasComidas)
                pedidos.append(pedido)
                print("\n       Quiere pedir mas?, Si/No")
            elif( str(sigue).upper() == "NO" ):
                break
            else:
                print("     Error: intente de nuevo")

        misPedidos = pedidos

        print("\n****precio de pedido*******")
        totalPagar = calPre(misPedidos, NombreyPrecioTodos, nombresEspeciales)
        if(totalPagar > 0):
            print(f"\nTotal= ${'{:.2f}'.format(totalPagar)}")
            
            while(True):
                comprar = input("\n>>¿Confirmar?: si/no ")
                try:
                    if( str(comprar).upper() == "SI" ):
                        print(f"\nCompra de ${'{:.2f}'.format(totalPagar)} registrada, pronto podra retirarla")
                        print("\n")
                        print("Gracias, vuelva pronto")
                        break
                    elif( str(comprar).upper() == "NO" ):
                        print("Cancelado.")
                        print("\n")
                        print("Gracias, vuelva pronto")
                        break
                    else:
                        print("\nError: por favor escoja una opcion valida")
                except:
                    print("\nIngrese Si o No")
            
        else:
            print("\nEl maximo permitido es 100.")
    else:
        print("\n")
        print("Gracias, vuelva pronto")


#inicio()