from codigo import calPre
from codigo import menu

diccionarioComidas, nombresComidas, nombresEspeciales, nombrePrecios = menu()

def test_calPre():
    pedido1 = [["pollo frito", 2], ["sopa de pollo",3], ["Bolon",2]]
    pedido2 = [["Chancho",2], ["Huevo frito",4], ["Encebollado",3], ["fideo",2]]
    pedido3 = [["Bollo", 50], ["pie",20], ["Batido",20], ["croissant",20]]
    pedido4 = [["croissant",1],["sopa de pollo",3], ["Encebollado",3],["Bollo",2]]

    #mas de 5 comidas
    assert calPre(pedido1, nombrePrecios, nombresEspeciales) == 35.80
    #mas de 10 comidas
    assert calPre(pedido2, nombrePrecios, nombresEspeciales) == 47.40
    #mas de 100 comidas
    assert calPre(pedido3, nombrePrecios, nombresEspeciales) == -1
    #sin especiales
    assert calPre(pedido4, nombrePrecios, nombresEspeciales) == 40.50
