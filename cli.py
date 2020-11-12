from __future__ import print_function, unicode_literals
from PyInquirer import Separator, Token, print_json, prompt, style_from_dict
from pprint import pprint
from listconvert import list_to_dict, list_to_objects
from typing import Dict, List
import csv
import requests

URL = "http://127.0.0.1:5000"

CREATE_PIZZA_ACTION = 1
UPDATE_PIZZA_ACTION = 2
CANCEL_ORDER_ACTION = 3
VIEW_MENU_ACTION = 4

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

menu_options = {}


def _get_choices(key: str, options: Dict[str, List[str]]) -> List[str]:
    '''
    Returns the choices in menu options
    '''
    if key in options:
        return menu_options[key]
    else:
        return ["key error"]


# User's initial action choices
starting_actions = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What would you like to do?',
        'choices': [
            {
                'name': '1. Order a Pizza',
                'value': CREATE_PIZZA_ACTION
            },
            {
                'name': '2. Update an Existing Order',
                'value': UPDATE_PIZZA_ACTION
            },
            {
                'name': '3. Cancel an Order',
                'value': CANCEL_ORDER_ACTION
            },
            {
                'name': '4. View Menu',
                'value': VIEW_MENU_ACTION
            }

        ]
    }
]


# Asks user if they wish to be redirected to home selection/"start_actions"
return_action = [
    {
        'type': 'confirm',
        'message': 'Do you want to return to home selection?',
        'name': 'return',
        'default': True,
    },
]


def main():
    """
    User selects their starting actions: Order a Pizza, Update an Existing Order, Cancel an Order
    """
    print("Welcome to Rajvi and Yichen's Pizza Parlour!")
    action = prompt(starting_actions, style=style)
    pprint(action)

    if action['action'] == CREATE_PIZZA_ACTION:
        create_order()
    elif action['action'] == UPDATE_PIZZA_ACTION:
        pass
    elif action['action'] == CANCEL_ORDER_ACTION:
        pass
    else:
        display_menu()


def create_order():
    '''
    Places an order specific to user's choices and outputs their order ID.
    '''
    r = requests.get(url=URL + "/menu")
    data = r.json()

    menu_options = list_to_dict(data)
    toppings_objects = list_to_objects(menu_options["toppings"])
    menu_options["toppings"] = toppings_objects

    # pprint(menu_options)

    order_options = [
        {
            'type': 'list',
            'name': '_size',
            'message': 'What size of pizza would you like?',
            'choices': menu_options['sizes']
        },
        {
            'type': 'list',
            'name': '_type',
            'message': "What type of pizza would you like?",
            'choices': menu_options['pizzas']
        },
        {
            'type': 'checkbox',
            'name': '_toppings',
            'message': "Which toppings would you like?",
            'choices': menu_options['toppings']
        },
        {
            'type': 'list',
            'name': '_drinks',
            'message': "Choose a Drink",
            'choices': menu_options['drinks']
        }
    ]

    answer = prompt(order_options)
    pprint(answer)

    r = requests.post(url=URL + "/create", data=answer)


def display_menu() -> None:
    """
    Diplay the menu from menu.csv
    """
    r = requests.get(url=URL + "/menu")
    menu = r.json()

    print("="*15 + " MENU " + "="*15)

    for row in menu:
        if row[0] != '':
            print("{0:30} {1:10}".format(row[0], row[1]))
        else:
            print(" ")

    answer = prompt(return_action, style=style)
    pprint(answer)

    if (answer['return']):
        main()


if __name__ == "__main__":
    main()
