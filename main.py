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

    # достаём ингредиенты, кол-во умножаем на кол-во персон
    shopping_bag = {}
    for dish in dishes:
        ingredients = cook_book[dish]
        # Проверяем, есть ли такое блюдо
        if ingredients is None:
            print(f"[-] Блюдо {dish} не в списке")
            continue
        # Из блюда вытаскиваем ингредиенты и записываем в список ингредиентов для покупок
        for ingridient in ingredients:
            # вычисляем кол-во ингредиента, учитывая, что ингредиенты могут повторяться в разных блюдах
            ingridient['quantity'] = int(ingridient['quantity']) * person_count
            quantity = ingridient['quantity']
            # Если такой ингредиент уже был в списке, то суммируем
            ingridient_name = ingridient['ingridient_name']
            if ingridient_name in shopping_bag:
                quantity = quantity + shopping_bag[ingridient_name]['quantity']
            # записываем в словарь игредиент
            shopping_bag[ingridient_name] = {
                'measure': ingridient['measure'],
                'quantity': quantity
            }
    # Возвращаем список(словарь) для покупок
    return shopping_bag




def concat_two_files():
    file_name1 = "1.txt"
    with open(file_name1, encoding="utf-8") as file:
        file1 = file.readlines()
    file_len1 = len(file1)

    file_name2 = "2.txt"
    with open(file_name2, encoding="utf-8") as file:
        file2 = file.readlines()
    file_len2 = len(file2)

    file_content = []
    if len(file1) > len(file2):
        file_content.append(file_name2)
        file_content.append(file_len2)
        file_content = file_content + file2

        file_content.append(file_name1)
        file_content.append(file_len1)
        file_content = file_content + file1
    else:
        file_content.append(file_name1)
        file_content.append(file_len1)
        file_content = file_content + file1

        file_content.append(file_name2)
        file_content.append(file_len2)
        file_content = file_content + file2

    result_file_name = "result.txt"
    file = open(result_file_name, encoding="utf-8", mode="w")
    for line in file_content:
        line = str(line).strip() + "\n"
        file.write(line)
        print(line)
    file.close()


print("[1] Читаем словарь с рецептами из файла")
cook_book = file_worker(file_name)
pprint(cook_book)

print("\n[2] Выводим список покупок")
shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
pprint(shop_list)

print("\n[3] Записываем файл")
result = concat_two_files()
