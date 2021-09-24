from mock_data import mock_data
import json
from flask import Flask, render_template
app = Flask(__name__)

# put the dict here.
me = {
    "name" :"Andrew",
    "last" : "Singo",
    "email" : "test@email.com",
    "age" : 32,
    "hobbies" : [],
    "address" : {
        "street" : "main st",
        "number" : "100"
    }

}

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    # return full name.
    return f"{me['name']} {me['last']}"

@app.route("/about/email")
def email_info():
    return f"{me['email']}"

@app.route("/about/address")
def address_info():
    address = me ['address']
    return f"{address['number']} {address['street']}"


#### API Methods

@app.route("/api/catalog")
def get_catalog():
    return json.dumps(mock_data)

@app.route("/api/categories")
def get_categories():
    
    categories = []
    for product in mock_data:
        cat = product["category"]

        if cat not in categories:
            categories.append(cat)
    
    return json.dumps(categories)
    

app.run(debug = True)
