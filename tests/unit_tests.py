from PizzaParlour import app
import unittest
from unittest.mock import patch
from cli import main, create_order, update_order, cancel_order, input_menu, display_menu, response_message, InputValidator
from prompt_toolkit.document import Document
from jsonwrite import get_order_ids
from listconvert import list_to_dict, list_to_objects


def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Parlour!'


def test_create_pizza():

    data = {"_type": "cheese", "_size": "small",
            "_extra_toppings": ["feta cheese"], "_drink": "coke"}
    response = app.test_client().post('/create', json=data)

    assert response.json["_status"] == 201
    assert response.status_code == 201


def test_update_order():

    data = {"_order_id": "20201112165232710", "_type": "cheese",
            "_size": "small", "_extra_toppings": [], "_drink": "coke"}
    response = app.test_client().post('/update', json=data)

    assert response.status_code == 201


def test_update_order_fail():

    data = {"_order_id": "11111111111111111", "_type": "cheese",
            "_size": "small", "_extra_toppings": ["feta cheese"], "_drink": "coke"}
    response = app.test_client().post('/update', json=data)

    assert response.status_code == 404


def test_deliver_fail():
    data = {"_order_id": "111111", "_delivery": "ubereats",
            "_address": "123 depresso st"}
    response = app.test_client().get('/deliver', json=data)

    assert response.status_code == 404


def test_deliver_ubereats():
    data = {"_order_id": "20201112165232710",
            "_delivery": "ubereats", "_address": "123 depresso st"}
    response = app.test_client().get('/deliver', json=data)

    assert response.status_code == 200
    assert type(response.json["_order"]) == dict
    assert response.json["_address"] == "123 depresso st"
    assert response.json["_delivery"] == "ubereats"
    assert response.json["_order"]["_type"] == "cheese"


def test_deliver_foodora():
    data = {"_order_id": "20201112165232710",
            "_delivery": "foodora", "_address": "123 meric st"}
    response = app.test_client().get('/deliver', json=data)

    assert response.status_code == 200
    assert type(response.json["_order"]) == str
    assert response.json["_address"] == "123 meric st"
    assert response.json["_delivery"] == "foodora"


def test_deliver_inhouse():
    data = {"_order_id": "20201112165232710",
            "_delivery": "in-house", "_address": "123 mertler st"}
    response = app.test_client().get('/deliver', json=data)

    assert response.status_code == 200
    assert type(response.json["_order"]) == dict
    assert response.json["_address"] == "123 mertler st"
    assert response.json["_delivery"] == "in-house"
    assert response.json["_order"]["_type"] == "cheese"


def test_cancel_order_fail():
    data = {"_order_id": "11111111111111111"}
    response = app.test_client().post('/cancel', json=data)

    assert response.status_code == 404


def test_cancel_order():
    data = {"_order_id": "20201112165232710"}
    response = app.test_client().post('/cancel', json=data)

    assert response.status_code == 200


def test_menu():

    response = app.test_client().get('/menu')

    assert response.json[0][0] == "Sizes"


def test_prices():

    response = app.test_client().get('/price')

    assert response.json["uoftears"] == "5.81"

# listconver TESTS


data = [["Sizes", ""], ["Small", "6.99"], ["Medium", "8.99"], ["Large", "10.99"], ["", ""], ["Pizzas", ""], ["Cheese", "1.01"], ["Mediterranean", "2.00"], ["UofTears (extra Salty)", "5.81"], ["Custom", " 10.99"], ["", ""], ["Toppings", ""], [
        "Salt", "9.99"], ["Broccoli", "4.50"], ["Sundried Tomatoes", "4.50"], ["Black Olives", "1.10"], ["Tears", "0.01"], ["Cheddar Cheese", "3.02"], ["Pepperoni", "2.89"], ["Feta Cheese", "5.55"], ["", ""], ["Drinks", ""], ["Coke", " 3.00"]]


def test_list_to_dict():

    output = {'sizes': ['small', 'medium', 'large'], 'pizzas': ['cheese', 'mediterranean', 'uoftears (extra salty)', 'custom'], 'toppings': [{'name': 'salt'}, {'name': 'broccoli'}, {
        'name': 'sundried tomatoes'}, {'name': 'black olives'}, {'name': 'tears'}, {'name': 'cheddar cheese'}, {'name': 'pepperoni'}, {'name': 'feta cheese'}], 'drinks': ['coke']}

    result = list_to_dict(data)

    assert result.keys() == output.keys()


def test_list_to_objects():
    options = list_to_dict(data)
    result = list_to_objects(options["toppings"])

    items = [{'name': 'salt'}, {'name': 'broccoli'}, {'name': 'sundried tomatoes'}, {'name': 'black olives'}, {
        'name': 'tears'}, {'name': 'cheddar cheese'}, {'name': 'pepperoni'}, {'name': 'feta cheese'}]

    assert result == items


def test_response_message_update():
    method_type = "update"
    wrong_code = 404
    good_code = 200
    order_id = "20201114013747739"

    wrong_value = response_message(method_type, order_id, wrong_code)
    good_value = response_message(method_type, order_id, good_code)

    assert wrong_value == False
    assert good_value == True


def test_response_message_cancel():
    method_type = "cancel"
    wrong_code = 404
    good_code = 200
    order_id = "20201114013747739"

    wrong_value = response_message(method_type, order_id, wrong_code)
    good_value = response_message(method_type, order_id, good_code)

    assert wrong_value == False
    assert good_value == True


def test_response_message_delivery():
    method_type = "deliver"
    wrong_code = 404
    good_code = 200
    order_id = "20201114013747739"

    wrong_value = response_message(method_type, order_id, wrong_code)
    good_value = response_message(method_type, order_id, good_code)

    assert wrong_value == False
    assert good_value == True


def test_input_validator():
    txt = "cheese"
    doc = Document(txt, None, None)
    validator = InputValidator()

    raised = False
    try:
        validator.validate(doc)
    except:
        raised = True

    assert raised == False
