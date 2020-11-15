from __future__ import print_function, unicode_literals
import requests
import csv
import json
from typing import Dict, List
from PyInquirer import prompt, Token, style_from_dict
from pprint import pprint
from listconvert import list_to_dict, list_to_objects
from questions import InputValidator, starting_actions, cancel_questions, select_questions, deliver_questions, CREATE_PIZZA_ACTION, UPDATE_PIZZA_ACTION, CANCEL_ORDER_ACTION, VIEW_MENU_FULL_ACTION, VIEW_MENU_SEL_ACTION, REQ_DELIVERY_ACTION, URL

STATUS_OK = [200, 201]

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


def response_message(method_type: str, order_id: str, status_code: int) -> bool:
    if method_type == "update":
        if status_code in STATUS_OK:
            print(
                "Order updated successfully. Your Order ID is still {}.".format(order_id))
            return True
        else:
            print("Could not update order. Please enter a valid Order ID.")
            return False
    elif method_type == "cancel":
        if status_code in STATUS_OK:
            print("Order cancelled successfully.")
            return True
        else:
            print("Could not cancel order. Please enter a valid Order ID.")
            return False
    elif method_type == "deliver":
        if status_code in STATUS_OK:
            print("Order has been delivered successfully!")
            return True
        else:
            print("Could not deliver your order. Please enter a valid Order ID.")
            return False


def main() -> bool:
    """
    User selects their starting actions: Order a Pizza, Update an Existing Order, Cancel an Order
    """
    print("Welcome to Rajvi and Yichen's Pizza Parlour!")
    action = prompt(starting_actions, style=style)
    pprint(action)

    if action['action'] == CREATE_PIZZA_ACTION:
        create_order()
    elif action['action'] == UPDATE_PIZZA_ACTION:
        update_order()
    elif action['action'] == CANCEL_ORDER_ACTION:
        answer = prompt(cancel_questions, style=style)
        response = requests.post(url=URL + "/cancel", json=answer)
        dictFromServer = response.json()
        cancel_order(dictFromServer, response.status_code)
    elif action['action'] == VIEW_MENU_SEL_ACTION:
        answer = prompt(select_questions, style=style)
        response = requests.get(url=URL + "/price")
        dictFromServer = response.json()
        input_menu(dictFromServer, answer["_item"])
    elif action['action'] == VIEW_MENU_FULL_ACTION:
        r = requests.get(url=URL + "/menu")
        menu = r.json()
        display_menu(menu)
    else:
        answer = prompt(deliver_questions, style=style)
        response = requests.get(url=URL + "/deliver", json=answer)
        dictFromServer = response.json()
        request_delivery(dictFromServer, response.status_code)


def create_order() -> None:
    '''
    Places an order specific to user's choices and outputs their order ID.
    '''
    response = requests.get(url=URL + "/menu")
    data = response.json()

    menu_options = list_to_dict(data)
    toppings_objects = list_to_objects(menu_options["toppings"])
    menu_options["toppings"] = toppings_objects

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
            'name': '_extra_toppings',
            'message': "Which toppings would you like?",
            'choices': menu_options['toppings']
        },
        {
            'type': 'list',
            'name': '_drink',
            'message': "Choose a Drink",
            'choices': menu_options['drinks']
        }
    ]

    answer = prompt(order_options, style=style)
    response = requests.post(url=URL + "/create", json=answer)
    dictFromServer = response.json()

    print("Thank you for your order! Your Order ID is " +
          dictFromServer["_order_id"])


def update_order() -> None:
    '''
    Prompts the user to enter an order ID, and updates their order options
    '''
    response = requests.get(url=URL + "/menu")
    data = response.json()

    menu_options = list_to_dict(data)
    toppings_objects = list_to_objects(menu_options["toppings"])
    menu_options["toppings"] = toppings_objects

    order_options = [
        {
            'type': 'input',
            'name': '_order_id',
            'message': 'Please enter your Order ID: '

        },
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
            'name': '_extra_toppings',
            'message': "Which toppings would you like?",
            'choices': menu_options['toppings']
        },
        {
            'type': 'list',
            'name': '_drink',
            'message': "Choose a Drink",
            'choices': menu_options['drinks']
        }
    ]

    answer = prompt(order_options, style=style)
    response = requests.post(url=URL + "/update", json=answer)
    dictFromServer = response.json()

    value = response_message(
        "update", dictFromServer["_order_id"], response.status_code)


def cancel_order(dictFromServer: Dict[str, str], status_code: int) -> bool:
    '''
    Prompts user for their Order ID and cancels the order.
    '''
    return response_message(
        "cancel", dictFromServer["_order_id"], status_code)


def input_menu(dictFromServer: [str, str], item: str) -> bool:
    '''
    User enters an item name and then obtains the price.
    '''
    print("The cost of {} is {}.".format(
        item, dictFromServer[item.lower()]))

    return True


def display_menu(menu: List[str]) -> bool:
    """
    Diplay the menu from menu.csv
    """

    print("="*15 + " MENU " + "="*15)

    for row in menu:
        if row[0] != '':
            print("{0:30} {1:10}".format(row[0], row[1]))
        else:
            print(" ")

    return True


def request_delivery(dictFromServer: Dict[str, str], status_code: int) -> bool:
    '''
    Prompts user to select delivery type, enter their Order ID, and Address.
    '''
    value = response_message(
        "deliver", dictFromServer["_order_id"], status_code)

    if value:
        print(dictFromServer["_order"])

    return value


if __name__ == "__main__":
    main()
