from typing import List, Dict

# data = [["Sizes", ""], ["Small", "6.99"], ["Medium", "8.99"], ["Large", "10.99"], ["", ""], ["Pizzas", ""], ["Cheese", "1.01"], ["Mediterranean", "2.00"], ["UofTears (extra Salty)", "5.81"], ["Custom", " 10.99"], ["", ""], ["Toppings", ""], [
#     "Salt", "9.99"], ["Broccoli", "4.50"], ["Sundried Tomatoes", "4.50"], ["Black Olives", "1.10"], ["Tears", "0.01"], ["Cheddar Cheese", "3.02"], ["Pepperoni", "2.89"], ["Feta Cheese", "5.55"], ["", ""], ["Drinks", ""], ["Coke", " 3.00"]]

# output = {'sizes': ['small', 'medium', 'large'], 'pizzas': ['cheese', 'mediterranean', 'uoftears (extra salty)', 'custom'], 'toppings': [{'name': 'salt'}, {'name': 'broccoli'}, {
#     'name': 'sundried tomatoes'}, {'name': 'black olives'}, {'name': 'tears'}, {'name': 'cheddar cheese'}, {'name': 'pepperoni'}, {'name': 'feta cheese'}], 'drinks': ['coke']}

# items = [{'name': 'salt'}, {'name': 'broccoli'}, {'name': 'sundried tomatoes'}, {'name': 'black olives'}, {
#     'name': 'tears'}, {'name': 'cheddar cheese'}, {'name': 'pepperoni'}, {'name': 'feta cheese'}]


def list_to_dict(data: List[List[str]]) -> Dict[str, List[str]]:
    '''
    Converts the list of rows form the menu into a dictionary where each category in the menu is a key in menu_options,
    and its value is a list of the options for each category.
    '''
    key = ''
    options = {}

    for row in data:
        if row[0] != "" and row[1] == "":
            key = row[0].lower()
        elif row[0] != "" and row[1] != "":
            if key not in options:
                options[key] = [row[0].lower()]
            else:
                options[key].append(row[0].lower())

    return options


def list_to_objects(items: List[str]) -> List[object]:
    objects = []
    for item in items:
        objects.append({"name": item.lower()})

    return objects


# if __name__ == "__main__":
#     options = list_to_dict(data)
#     items_result = list_to_objects(options["toppings"])
#     options["toppings"] = items

#     print(items)
#     print(items_result == items)
