menu = {
    "Comida china": {
        "Arroz frito": 8,
        "Pollo Kung Pao": 10,
        "Rollos Spring": 6,
    },
    "Comida Italiana": {
        "Spaghetti a la Bolognesa": 12,
        "Pizza": 14,
        "Tiramisu": 9,
    },
    "Pasteleria": {
        "Croissant": 4,
        "Eclair": 5,
        "Macarron": 3,
    },
    "Especialidad del chef": {
        "Pasta Especial": 18,
        "Corte Especial": 20,
    }
}

def display_menu():
    print(" Bienvenido al organizador de experiencias de cena!\n")
    print("MENÚ:")
    for category, meals in menu.items():
        print(f"\n{category}:\n")
        for meal, price in meals.items():
            print(f"{meal} - ${price}")

def get_user_selection():
    selected_meals = {}
    while True:
        meal_choice = input("\nIngrese el nombre del plato que desea ordenar (o ingrese 'listo' para terminar): ")
        if meal_choice.lower() == "listo":
            break

        if meal_choice not in [meal for meals in menu.values() for meal in meals]:
            print("Error: Plato no disponible en el menú. Por favor, seleccione un plato válido.")
            continue

        try:
            quantity = int(input(f"Cuantos {meal_choice} desea ordenar? "))
            if quantity <= 0:
                print("Error: La cantidad debe ser positiva, entera y mayor a 0.")
            elif quantity > 100:
                print("Error: La máxima cantidad de ordenes son 100 platos.")
            else:
                selected_meals[meal_choice] = quantity
        except ValueError:
            print("Error: Entrada invalida. Por favor, ingrese un entero positivo valido.")

    return selected_meals

def calculate_total_cost(selected_meals):
    base_cost = 5
    total_cost = sum(menu[meal_category][meal] * quantity for meal, quantity in selected_meals.items()
                     for meal_category in menu.keys())
    total_quantity = sum(selected_meals.values())

    if total_quantity > 10:
        total_cost *= 0.8
    elif total_quantity > 5:
        total_cost *= 0.9

    if total_cost > 100:
        total_cost -= 25
    elif total_cost > 50:
        total_cost -= 10

    special_meals = [meal for meal in selected_meals.keys() if meal in menu["Especialidad del chef"].keys()]
    if special_meals:
        total_cost *= 1.05

    return total_cost

def confirm_order(selected_meals, total_cost):
    print("\nPlatos seleccionados:")
    for meal, quantity in selected_meals.items():
        print(f"{meal} x{quantity}")

    print(f"\nCosto Total: ${total_cost}")

    confirmation = input("\nquieres confirmar tu orden? (si/no): ")
    if confirmation.lower() == "si":
        return total_cost
    else:
        return -1

def dining_experience_manager():
    display_menu()
    selected_meals = get_user_selection()
    total_cost = calculate_total_cost(selected_meals)
    confirmed_total_cost = confirm_order(selected_meals, total_cost)

    if confirmed_total_cost != -1:
        print("\nGracias por ordenar! Disfrute su comida!")
        return confirmed_total_cost
    else:
        print("\nOrden cancelada. Por favor, haga cambios en su selección.")
        return -1

if __name__ == "__main__":
    dining_experience_manager()
