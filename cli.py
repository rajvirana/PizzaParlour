from __future__ import print_function, unicode_literals
from PyInquirer import Separator, Token, print_json, prompt, style_from_dict
from pprint import pprint

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

starting_actions = [
    {
        'type': 'list',
        'name': 'action',
        'message': 'What would you like to do?',
        'choices': [
            {
                'name': '1. Order a Pizza',
                'value': 1
            },
            {
                'name': '2. Update an Existing Order',
                'value': 2
            },
            {
                'name': '3. Cancel an Order',
                'value': 3
            }

        ]
    }
]


def main():
    """
    User selects their starting actions: Order a Pizza, Update an Existing Order, Cancel an Order
    """
    print("Welcome to Rajvi and Yichen's Pizza Parlour!")
    answer = prompt(starting_actions)
    pprint(answer)


if __name__ == "__main__":
    main()
