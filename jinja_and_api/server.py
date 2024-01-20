from flask import Flask, render_template
import random
import requests

AGE_API = "https://api.agify.io"
GENDER_API = "https://api.genderize.io"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", random_num=random.randint(25, 75))


@app.route('/guess/<user_name>')
def using_api(user_name):

    name_input = user_name.title()

    parameter = {"name": user_name}

    response1 = requests.get(url=AGE_API, params=parameter)
    data1 = response1.json()
    user_age = data1["age"]

    response2 = requests.get(url=GENDER_API, params=parameter)
    data2 = response2.json()
    user_gender = data2["gender"]

    return render_template("guess.html", name_of_user=name_input, age=user_age, gender=user_gender)


if __name__ == '__main__':
    app.run(debug=True)
