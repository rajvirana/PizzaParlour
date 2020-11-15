# Assignment 2: Pizza Parlour

Welcome to Rajvi and Yichen's Pizza Parlour, featuring a fully customized CLI for your ease of use, as well as a server that runs on Flask.

## Installation

This application was coded in Python 3.9.0.

Please use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies:

```bash
py -m pip install requests
py -m pip install pytest
py -m pip install pytest-cov
py -m pip install pyinquirer
py -m pip install 'prompt_toolkit==1.0.14'
py -m pip install Pygments
py -m pip install pytest-html
py -m pip install pytest-xdist
py -m pip install pylint
py -m pip install ptyprocess
py -m pip install regex
```

If the code does not run, there is potentially an issue with PyInquirer not installing its dependencies properly. The above listed are all the dependencies, but refer to the [PyInquirer](https://github.com/CITGuru/PyInquirer) readme, requirements.txt, requirements_dev.txt to check what is missing.

## Usage

To run the server:

```bash
py PizzaParlour.py
```

To run the CLI (must have server running to create / send orders):

```bash
py cli.py
```

Run unit tests with coverage:

```bash
pytest --cov-report term --cov=. tests/unit_tests.py
```

OR

```bash
py -m pytest --cov-report term --cov=. tests/unit_tests.py
```

### Testing (Please Read)

Due to the fact that we are saving client orders into a database, this means that during **unit testing**, we will be "cancelling" a "premade" order in `orders.json`.

Furthermore, because we generate order ids based on the **time** that they order their pizza, this means that all order ids will be different when the unittests are run. Thus, we decided to include a premade *order* with the order id ("20201112165232710") that we will be "cancelling" during unit testing.

**Before running the unit tests for a *second* time, please "reset" the contents in `orders.json` by copying the entirety of `orders_backup.json` into `orders.json`.**

Otherwise, unit tests **will fail**.

There is also a rare issue where after installing all of the dependencies, there will be a ModuleNotFoundError that is caused by an unknown issue in the PYTHON PATH that causes pytest to be unable to find PyInquirer. The only known method is deleting the entire repository and reinstalling dependencies. If it still does not run, here is a screenshot of the test coverage:

![image](https://64.media.tumblr.com/fec6ecb7de72ac69e40b1107dd775dfa/2ff54bf954af97cd-4b/s1280x1920/eade76effcb9c4084b542c796b53aa87df927c34.png)

## Pair Programming

A large portion of our program was done through pair programming.

**Feature 1:** CLI Command: Display Menu

>Driver: Rajvi

>Navigator: Yichen

**Feature 2:** Order Class

>Driver: Yichen

>Navigator: Rajvi

**Feature 3:** Serialization to JSON file

>Driver: Yichen

>Navigator: Rajvi

**Feature 4: (Discarded)** Serialization to CSV file

>Driver: Yichen

>Navigator: Rajvi

**Feature 5:** Delete OR update pre-existing order in JSON / CSV files:

>Driver: Rajvi

>Navigator: Yichen

### Pros and Cons

We enjoyed pair programming a lot, because while the driver was coding, the navigator was able to keep a sharp eye out on bad syntax, suggest better ideas for implementation, offer insight during moments of confusion, and generally keep the code aligned to the initial goal. The driver did not have to remember all the details that they needed to implement, and would work on it module-by-module as directed by the navigator.

Furthermore, we found that our efficiency during pair programming increased a lot, because we were able to talk out our thoughts and have two people searching up solutions to bugs, which saved us a lot of time. In fact, we opted to complete a large majority of our Flask API because of how efficient this method worked, and how it can minimize errors in the code. In addition, because we implemented almost our entire application together, it was much easier to split off after pair programming to finish up the application, because we both knew how exactly the application works.

One thing that was slightly frustrating was the lack of access to the other's code, such as if the driver was confused on what types of input a method would receive from the POST request from the client, the navigator had to test it out on their own local copy of the code or send the sample "input" through a text-chat. Furthermore, the navigator's eyes are faster than the driver's eyes, so during the implementation of a feature, the navigator would be voicing issues in the code during the ongoing coding of the driver. This can sometimes cause the driver to lose focus on their current work, which sometimes slowed us down.

## Code Design

We wanted our API to be able to interact with both the CLI and a database, so we decided to implement an extra step of writing order information to a JSON file. 

We employed the Builder design pattern with our Orders class, because originally, it required several different input values to its init method, which was a less-than-ideal way to go about creating an Order object. Thus, we decided to switch over to OrderBuilder class, which calls methods that will set the required instance variables in the Order class. 

- Single Responsibility Rule
    - All of our code are separated into modules depending on what they deal with. For example, reader.py deals with anything that requires output from our menu.csv file, and order_builder.py is the Builder pattern that builds all the instance variables in the Order class.
    - We made sure that jsonwrite.py would handle anything related to writing to the JSON, and PizzaParlour.py would only call these methods as to stick with single responsibility rule.

### RESTful API Design

- Client-Server
    - Our client and server are separate from each other, our client being the CLI, and our server being the Flask API, which takes information from our backend (`menu.csv`, `orders.json`).
    - The client will dynamically render menu.csv every time it is started up, as it receives the data from menu.csv from the server.
    - The server handles any processing (creating Order objects, formatting JSON objects, etc) and interacts with the database (`orders.json`).
    - The CLI and the Flask API can be updated independently of the other, and the only link required is to create new methods to handle CLI requests to the server.
- Stateless
    - Our API is stateless, because after it creates an Order object, we only send that information into the backend (`orders.json`) to be stored and does not store any record of the user sending it information. We always grab information the user requests directly from the database, and store any info the user inserts directly into the database through our API.

### Other
- Status Codes
    - Our API always sends status codes after any request
- JSON Response
    - Our API always returns a JSON response with any data required to the client.

## Tools

[PyInquirer](https://github.com/CITGuru/PyInquirer)

PyInquirer was chosen for it's interactive command line interface. From its docs, PyInquirer is an easily embeddable and beautiful command line interface for Python.

[Pylint](https://pypi.org/project/pylint/)

Pylint allowed us to keep our code clean and pointed us to any errors.

## License
[MIT](https://choosealicense.com/licenses/mit/)
