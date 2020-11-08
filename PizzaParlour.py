from flask import Flask

app = Flask("Assignment 2")


@app.route('/pizza')
def welcome_pizza():
    return "Welcome to Pizza Parlour!"


if __name__ == "__main__":
    app.run()
