from flask import Flask

app = Flask("Assignment 2")


@app.route('/pizza')
def welcome_pizza():
    return "Welcome to Pizza Parlour!"


def calculate_total(prices) -> float:
    """
    Calculate and returns the user's total cost

    prices: the list of costs of all items in the user's order
    """
    return sum(prices)


@app.route('/create')
def store_order():
    # note: "orders" is an Order type object
    return "hello"


if __name__ == "__main__":
    app.run()
