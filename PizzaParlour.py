from flask import Flask, request
from order import Order
from jsonwrite import write_to_json
from csvwrite import write_to_csv, update_order_csv
import json
import csv

app = Flask("Assignment 2")


@app.route('/pizza')
def welcome_pizza():
    return "Welcome to Pizza Parlour!"

# s =  {"_order_id": "20201109200700761", "_type": "cheese", "_size": "large", "_extra_toppings": [], "_address": "123 depression street", "_drink": "coke", "_delivery": "ubereats", "_price": 16.55}


@app.route('/create', methods=['POST'])
def create_order() -> bool:
    '''
    Uploads the new order into the respective data files. If delivery method is foodora, will upload it to orders.csv,
    if delivery method is ubereats or in-house, uploads the order to orders.csv
    '''
    write_to_json(request.json)
    return request.json


# @app.route('/update')
# def update_order(new_order: Order) -> None:

# def calculate_total(prices) -> float:
#     """
#     Calculate and returns the user's total cost

#     prices: the list of costs of all items in the user's order
#     """
#     return sum(prices)


# @app.route('/create')
# def store_order():
#     # note: "orders" is an Order type object
#     return "hello"
if __name__ == "__main__":
    app.run()
