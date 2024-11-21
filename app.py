from flask import Flask, render_template
import key

app = Flask(__name__)
@app.route("/")
def index():
    def cool_things():
        print("I print the API key here, without having it in this file: ", key.MY_SECRET_API_KEY_1)






    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]
    new = []

            #new = {fruit['name']: fruit['quantity']}

    new =  {fruit["name"]: fruit["quantity"] for fruit in fruits if fruit["name"].lower().startswith('o')}
    new = {fruit["name"]: fruit["quantity"] for fruit in fruits if fruit['quantity'] < 3}

    return render_template("index.html", fruits=new, key_1 = key.MY_SECRET_API_KEY_1, key_2 = key.MY_SECRET_API_KEY_2)
