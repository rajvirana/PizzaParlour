from prompt_toolkit.validation import Validator, ValidationError
import requests

CREATE_PIZZA_ACTION = 1
UPDATE_PIZZA_ACTION = 2
CANCEL_ORDER_ACTION = 3
VIEW_MENU_SEL_ACTION = 4
VIEW_MENU_FULL_ACTION = 5
REQ_DELIVERY_ACTION = 6

URL = "http://127.0.0.1:5000"


class InputValidator(Validator):
    def validate(self, document):
        response = requests.get(url=URL + "/price")
        dictFromServer = response.json()

        if document.text.lower() not in dictFromServer:
            raise ValidationError(
                message='Please enter a valid item',
                cursor_position=len(document.text))  # Move cursor to end


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
                    'name': '4. View price of item',
                    'value': VIEW_MENU_SEL_ACTION
                },
            {
                    'name': '5. View Menu',
                    'value': VIEW_MENU_FULL_ACTION
                },
            {
                    'name': '6. Request for Delivery',
                    'value': REQ_DELIVERY_ACTION
                }

        ]
    }
]


cancel_questions = [
    {
        'type': 'input',
                'name': '_order_id',
                'message': 'Please enter your Order ID: '
    }
]

select_questions = [
    {
        'type': 'input',
                'name': '_item',
                'message': 'What item do you want the price of?',
                'validate': InputValidator
    }
]

deliver_questions = [
    {
        'type': 'list',
                'name': '_delivery',
                'message': "Select your delivery preference:",
                'choices': ['in-house delivery', 'uber eats', 'foodora']
    },
    {
        'type': 'input',
                'name': '_address',
                'message': "What is your address? "
    },
    {
        'type': 'input',
                'name': '_order_id',
                'message': 'What is your Order ID? '
    }
]
