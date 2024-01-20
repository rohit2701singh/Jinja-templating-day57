from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the website. Please write your name in url"


@app.route('/<name>')
def num_generate(name):
    random_num = random.randint(1, 100)
    current_year = datetime.now().year
    return render_template("index.html", user_name=name, a_num=random_num, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)


