from __future__ import print_function, unicode_literals
import requests
import csv
import json
from typing import Dict, List
from PyInquirer import prompt, Token, style_from_dict
from pprint import pprint
from listconvert import list_to_dict, list_to_objects
from questions import InputValidator, starting_actions, cancel_questions, select_questions, deliver_questions, CREATE_PIZZA_ACTION, UPDATE_PIZZA_ACTION, CANCEL_ORDER_ACTION, VIEW_MENU_FULL_ACTION, VIEW_MENU_SEL_ACTION, REQ_DELIVERY_ACTION, URL
# from prompt_toolkit.validation import Validator, ValidationError


# URL = "http://127.0.0.1:5000"

# CREATE_PIZZA_ACTION = 1
# UPDATE_PIZZA_ACTION = 2
# CANCEL_ORDER_ACTION = 3
# VIEW_MENU_SEL_ACTION = 4
# VIEW_MENU_FULL_ACTION = 5
# REQ_DELIVERY_ACTION = 6

STATUS_OK = [200, 201]

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})


# class InputValidator(Validator):
#     def validate(self, document):
#         response = requests.get(url=URL + "/price")
#         dictFromServer = response.json()

#         if document.text.lower() not in dictFromServer:
#             raise ValidationError(
#                 message='Please enter a valid item',
#                 cursor_position=len(document.text))  # Move cursor to end


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

# def _prompt_return() -> None:
#     # Asks user if they wish to be redirected to home selection/"start_actions"
#     return_action = [
#         {
#             'type': 'confirm',
#             'message': 'Do you want to return to home selection?',
#             'name': 'return',
#             'default': True,
#         },
#     ]

#     answer = prompt(return_action)

#     if (answer['return']):
#         main()
#     else:
#         print("Thank you for shopping with us!")


def main():
    """
    User selects their starting actions: Order a Pizza, Update an Existing Order, Cancel an Order
    """
    # User's initial action choices
    # starting_actions = [
    #     {
    #         'type': 'list',
    #         'name': 'action',
    #         'message': 'What would you like to do?',
    #         'choices': [
    #             {
    #                 'name': '1. Order a Pizza',
    #                 'value': CREATE_PIZZA_ACTION
    #             },
    #             {
    #                 'name': '2. Update an Existing Order',
    #                 'value': UPDATE_PIZZA_ACTION
    #             },
    #             {
    #                 'name': '3. Cancel an Order',
    #                 'value': CANCEL_ORDER_ACTION
    #             },
    #             {
    #                 'name': '4. View price of item',
    #                 'value': VIEW_MENU_SEL_ACTION
    #             },
    #             {
    #                 'name': '5. View Menu',
    #                 'value': VIEW_MENU_FULL_ACTION
    #             },
    #             {
    #                 'name': '6. Request for Delivery',
    #                 'value': REQ_DELIVERY_ACTION
    #             }

    #         ]
    #     }
    # ]

    print("Welcome to Rajvi and Yichen's Pizza Parlour!")
    action = prompt(starting_actions, style=style)
    pprint(action)

    if action['action'] == CREATE_PIZZA_ACTION:
        create_order()
    elif action['action'] == UPDATE_PIZZA_ACTION:
        update_order()
    elif action['action'] == CANCEL_ORDER_ACTION:
        # cancel_questions = [
        #     {
        #         'type': 'input',
        #         'name': '_order_id',
        #         'message': 'Please enter your Order ID: '
        #     }
        # ]

        answer = prompt(cancel_questions, style=style)
        response = requests.post(url=URL + "/cancel", json=answer)
        dictFromServer = response.json()
        val = cancel_order(dictFromServer, response.status_code)
    elif action['action'] == VIEW_MENU_SEL_ACTION:
        # select_questions = [
        #     {
        #         'type': 'input',
        #         'name': '_item',
        #         'message': 'What item do you want the price of?',
        #         'validate': InputValidator
        #     }
        # ]

        answer = prompt(select_questions, style=style)
        response = requests.get(url=URL + "/price")
        dictFromServer = response.json()
        val = input_menu(dictFromServer, answer["_item"])
    elif action['action'] == VIEW_MENU_FULL_ACTION:
        r = requests.get(url=URL + "/menu")
        menu = r.json()
        val = display_menu(menu)
    else:
        # deliver_questions = [
        #     {
        #         'type': 'list',
        #         'name': '_delivery',
        #         'message': "Select your delivery preference:",
        #         'choices': ['in-house delivery', 'uber eats', 'foodora']
        #     },
        #     {
        #         'type': 'input',
        #         'name': '_address',
        #         'message': "What is your address? "
        #     },
        #     {
        #         'type': 'input',
        #         'name': '_order_id',
        #         'message': 'What is your Order ID? '
        #     }
        # ]

        answer = prompt(deliver_questions, style=style)
        response = requests.get(url=URL + "/deliver", json=answer)
        dictFromServer = response.json()
        val = request_delivery(dictFromServer, response.status_code)


def create_order():
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

    # _prompt_return()


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

    # _prompt_return()


def cancel_order(dictFromServer: Dict[str, str], status_code: int) -> bool:
    '''
    Prompts user for their Order ID and cancels the order.
    '''

    # question = [
    #     {
    #         'type': 'input',
    #         'name': '_order_id',
    #         'message': 'Please enter your Order ID: '
    #     }
    # ]

    # answer = prompt(question, style=style)
    # response = requests.post(url=URL + "/cancel", json=answer)
    # dictFromServer = response.json()

    return response_message(
        "cancel", dictFromServer["_order_id"], status_code)

    # _prompt_return()


def input_menu(dictFromServer: [str, str], item: str) -> bool:
    '''
    User enters an item name and then obtains the price.
    '''

    # question = [
    #     {
    #         'type': 'input',
    #         'name': '_item',
    #         'message': 'What item do you want the price of?',
    #         'validate': InputValidator
    #     }
    # ]

    # answer = prompt(question, style=style)
    # response = requests.get(url=URL + "/price")
    # dictFromServer = response.json()

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

    # _prompt_return()

    return True


def request_delivery(dictFromServer: Dict[str, str], status_code: int) -> bool:
    '''
    Prompts user to select delivery type, enter their Order ID, and Address.
    '''
    # questions = [
    #     {
    #         'type': 'list',
    #         'name': '_delivery',
    #         'message': "Select your delivery preference:",
    #         'choices': ['in-house delivery', 'uber eats', 'foodora']
    #     },
    #     {
    #         'type': 'input',
    #         'name': '_address',
    #         'message': "What is your address? "
    #     },
    #     {
    #         'type': 'input',
    #         'name': '_order_id',
    #         'message': 'What is your Order ID? '
    #     }
    # ]

    # answer = prompt(questions, style=style)
    # response = requests.get(url=URL + "/deliver", json=answer)
    # dictFromServer = response.json()

    value = response_message(
        "deliver", dictFromServer["_order_id"], status_code)

    if value:
        print(dictFromServer["_order"])

    # _prompt_return()

    return value


if __name__ == "__main__":
    main()
