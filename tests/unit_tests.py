from PizzaParlour import app

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Parlour!'

def test_create_pizza():

    data = {"_type": "cheese", "_size": "small", "_extra_toppings": ["feta cheese"], "_drink": "coke"}
    response = app.test_client().post('/create', json=data)

    assert response.json["_status"] == 201
    assert response.status_code == 201

def test_update_order():

    data = {"_order_id": "20201112165232710", "_type": "cheese", "_size": "small", "_extra_toppings": [], "_drink": "coke"}
    response = app.test_client().post('/update', json=data)

    assert response.status_code == 201

def test_update_order_fail():

    data = {"_order_id": "11111111111111111", "_type": "cheese", "_size": "small", "_extra_toppings": ["feta cheese"], "_drink": "coke"}
    response = app.test_client().post('/update', json=data)

    assert response.status_code == 404

def test_deliver_ubereats():
    data = {"_order_id": "20201112165232710", "_delivery":"ubereats", "_address": "123 depresso st"}
    response = app.test_client().get('/deliver', json=data)

    assert response.status_code == 200
    assert type(response.json["_order"]) == dict
    assert response.json["_address"] == "123 depresso st"
    assert response.json["_delivery"] == "ubereats"
    assert response.json["_order"]["_type"] == "cheese"

def test_deliver_ubereats_foodora():
    data = {"_order_id": "20201112165232710", "_delivery":"foodora", "_address": "123 meric st"}
    response = app.test_client().get('/deliver', json=data)

    assert response.status_code == 200
    assert type(response.json["_order"]) == str
    assert response.json["_address"] == "123 meric st"
    assert response.json["_delivery"] == "foodora"

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

