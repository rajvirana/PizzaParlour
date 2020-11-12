from flask import Flask, request, jsonify

from order import Order
from jsonwrite import get_order_ids, write_to_json, remove_from_json, convert_to_csv, get_order
from csvwrite import get_reader, write_to_csv, update_order_csv, remove_from_csv
import jsonwrite
import json
import csv

app = Flask("Assignment 2")


@app.route('/pizza')
def welcome_pizza():
    return "Welcome to Pizza Parlour!"

# s =  {"_order_id": "20201109200700761", "_type": "cheese", "_size": "large", "_extra_toppings": ["feta cheese"], "_address": "123 depression street", "_drink": "coke", "_delivery": "ubereats", "_price": 16.55}


@app.route('/create', methods=['POST'])
def create_order() -> str:
    '''
    Uploads the new order into the respective data files. If delivery method is foodora, will upload it to orders.csv,
    if delivery method is ubereats or in-house, uploads the order to orders.csv
    '''
    new_order = Order(request.json['_type'], request.json['_size'], request.json['_extra_toppings'],
                      request.json['_drink'])

    write_to_json(new_order)

    order_id = {"_order_id": new_order.get_order_id()}

    response = app.response_class(response=json.dumps(order_id), status=201, mimetype='application/json')

    return response


@app.route("/update", methods=['POST'])
def update_order() -> str:
    '''
    Updates a prexisting order in orders.csv or orders.json depending on the delivery type: foodora or, ubereats/in-house respectively.

    Precondition: user inputs their previous order_id, and all other fields that may or may not be changed
    '''

    keys = get_order_ids()

    order_id = {"_order_id": request.json["_order_id"]}

    if request.json['_order_id'] not in keys:

        order_id["status"] = 404

        response = app.response_class(response=json.dumps(order_id), status=404, mimetype='application/json')
    else:
        new_order = Order(request.json['_type'], request.json['_size'], request.json['_extra_toppings'],
                        request.json['_drink'])

        new_order.set_order_id(request.json['_order_id'])

        write_to_json(new_order)

        order_id["status"] = 201

        response = app.response_class(response=json.dumps(order_id), status=201, mimetype='application/json')

    return response


@app.route("/cancel", methods=['POST'])
def cancel_order() -> str:
    '''
    Cancels a prexisting order in orders.csv or orders.json depending on the delivery type: foodora or, ubereats/in-house respectively.

    Precondition: order_id is prexisting in the appropriate delivery type
    '''
    keys = get_order_ids()
    order_id = {"_order_id": request.json["_order_id"]}

    if request.json['_order_id'] not in keys:
        order_id["status"] = 404
        
        response = app.response_class(response=json.dumps(order_id), status=404, mimetype='application/json')
    else:
        remove_from_json(request.json["_order_id"])

        order_id["status"] = 200
        
        response = app.response_class(response=json.dumps(order_id), status=200, mimetype='application/json')

    return response

@app.route("/deliver", methods=['GET'])
def request_delivery():
    '''
    Requests delivery of the pizza.

    Precondition: Input should look like:

    {
        "_delivery_method": "foodora",
        "_order_id": "34324217871822",
        "_address": "123 depression street",
    } 
    '''
    keys = get_order_ids()
    order_info = {"_order_id": request.json["_order_id"]}
    order_id = request.json['_order_id']

    if order_id not in keys:
        order_info["status"] = 404

        response = app.response_class(response=json.dumps(order_info), status=404, mimetype='application/json')
    else:
        if request.json["_delivery_method"] == "foodora":
            order = convert_to_csv(order_id)    
        else:
            order = get_order(order_id)
        
        order_info["status"] = 200
        order_info["order"] = order
        order_info["address"] = request.json["_address"]
        order_info["delivery"] = request.json["_delivery_method"]

        response = app.response_class(response=json.dumps(order_info), status=200, mimetype='application/json')

    return response

@app.route("/menu", methods=['GET'])
def get_menu():
    '''
    Returns the list of lines from the menu
    '''
    return jsonify(get_reader())


if __name__ == "__main__":
    app.run()
