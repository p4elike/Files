# библиотека для получения пути к файлу
import os
# команда библиотеки для вывода пути на консоли
#print('====>' , os.getcwd())
# команда библиотеки для вывода полного пути к определённому файлу на консоли
#print(f'{os.getcwd()}/допустим.txt')

#полный путь для люой платформы
#path = os.path.join(os.getcwd(),'допустим.txt')
from pprint import pprint

with open('допустим.txt') as recipe_list:
    result = {}

    for name in recipe_list:
        dish_name = name.strip()
        counter = int(recipe_list.readline().strip())
        temp_data = []
        for food in range(counter):
            ingredient, quantity, unit = recipe_list.readline().split('|')
            food_list = {'ingredient_name' : ingredient.strip(), 'quantity': int(quantity.strip()), 'measure' : unit.strip()}
            temp_data.append(food_list)
        result[dish_name] = temp_data
        recipe_list.readline().strip()

    #pprint(result)

def get_shop_list_by_dishes(dishes_list, person_count):
    list_by_dishes = []
    for dishes in result and dishes_list:
        list_by_dishes.append(result[dishes])
        print(list_by_dishes)

            # for ingredient_list in list_by_dishes:
            #     for ingredient_quantity in ingredient_list:
            #         ingredient_quantity['quantity'] = ingredient_quantity['quantity'] * person_count
            #         get_shop_list_by_dishes = {ingredient_quantity['ingredient_name'] : {ingredient_quantity['quantity'],ingredient_quantity['measure']}}
            #         #print(ingredient_quantity['ingredient_name'], ingredient_quantity['quantity'], ingredient_quantity['measure'],)
            #
            #
            #
            #         print(get_shop_list_by_dishes)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
#get_shop_list_by_dishes( 'Омлет', 3 )