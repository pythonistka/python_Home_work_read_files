from pprint import pprint

file_name = "recipes.txt"


def file_worker(file_name: str) -> dict:
    data = ""
    with open(file_name, encoding="utf-8") as file:
        data = file.readlines()

    total_str = "".join(data)
    recipes = total_str.split("\n\n")

    cook_book = {}
    for x in recipes:
        recipe = x.split("\n")
        dish_name = recipe[0]
        list_recipes = []
        for i in range(2, len(recipe)):
            ingridient = recipe[i].split(" | ")
            ingridient_name = ingridient[0]
            quantity = ingridient[1]
            measure = ingridient[2]
            dict_ingridient = {'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure}
            list_recipes.append(dict_ingridient)
        cook_book[dish_name] = list_recipes

    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int) -> dict:
    # проверка персон на ноль
    if person_count == 0 or person_count is None:
        print("Количество людей не может быть ноль")
        return {}

    # достаём ингридиенты, кол-во умножаем на кол-во персон
    shopping_bag = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        # Проверяем, есть ли такое блюдо
        if ingredients is None:
            print(f"[-] Блюдо {dish} не в списке")
            continue
        # Из блюда вытаскиваем ингридиенты из блюда и записываем в список ингридентов для покупок
        for ingridient in ingredients:
            # вычисляем кол-во ингридиента, учитывая, что ингридиенты могут повторяться в разных блюдах
            ingridient['quantity'] = int(ingridient['quantity']) * person_count
            quantity = ingridient['quantity']
            # Если такой ингридиент уже был в списке, то суммируем
            ingridient_name = ingridient['ingridient_name']
            if ingridient_name in shopping_bag:
                quantity = quantity + shopping_bag[ingridient_name]['quantity']
            # записываем в словарь игридиент
            shopping_bag[ingridient_name] = {
                'measure': ingridient['measure'],
                'quantity': quantity
            }
    # Возвращаем список(словарь) для покупок
    return shopping_bag






print("[1] Читаем словарь с рецептами из файла")
cook_book = file_worker(file_name)
pprint(cook_book)

print("\n[2] Выводим список покупок")
shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
pprint(shop_list)
