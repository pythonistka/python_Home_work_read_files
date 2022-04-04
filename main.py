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



result = file_worker(file_name)
pprint(result)
