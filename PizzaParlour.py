from flask import Flask, request
from order import Order
from jsonwrite import write_to_json, remove_from_json
from csvwrite import write_to_csv, update_order_csv
import json
import csv

app = Flask("Assignment 2")


@app.route('/pizza')
def welcome_pizza():
    return "Welcome to Pizza Parlour!"

# s =  {"_order_id": "20201109200700761", "_type": "cheese", "_size": "large", "_extra_toppings": [], "_address": "123 depression street", "_drink": "coke", "_delivery": "ubereats", "_price": 16.55}


@app.route('/create', methods=['POST'])
def create_order() -> str:
    '''
    Uploads the new order into the respective data files. If delivery method is foodora, will upload it to orders.csv,
    if delivery method is ubereats or in-house, uploads the order to orders.csv
    '''
    new_order = Order(request.json['_type'], request.json['_size'], request.json['_extra_toppings'],
                      request.json['_drink'], request.json['_delivery'], request.json['_address'])

    if request.json["_delivery"] == "foodora":
        write_to_csv(new_order)
    elif request.json["_delivery"] == "ubereats" or request.json["_delivery"] == "in-house":
        write_to_json(new_order)

    return "ok"


@app.route("/update", methods=['POST'])
def update_order() -> str:
    '''
    Updates a prexisting order in orders.csv or orders.json depending on the delivery type: foodora or, ubereats/in-house respectively.

    Precondition: user inputs their previous order_id, and all other fields that may or may not be changed
    '''
    new_order = Order(request.json['_type'], request.json['_size'], request.json['_extra_toppings'],
                      request.json['_drink'], request.json['_delivery'], request.json['_address'])

    new_order.set_order_id(request.json['_order_id'])

    if request.json["_delivery"] == "foodora":
        update_order_csv(new_order)
    elif request.json["_delivery"] == "ubereats" or request.json["_delivery"] == "in-house":
        write_to_json(new_order)

    return "ok"


@app.route("/cancel", methods=['POST'])
def cancel_order() -> str:
    '''
    Cancels a prexisting order in orders.csv or orders.json depending on the delivery type: foodora or, ubereats/in-house respectively.

    Precondition: order_id is prexisting in the appropriate delivery type
    '''
    if request.json["_delivery"] == "foodora":
        pass
    elif request.json["_delivery"] == "ubereats" or request.json["_delivery"] == "in-house":
        remove_from_json(request.json["_order_id"])

    return "ok"


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
