from app import app
from flask import render_template


@app.route("/", methods=["GET"])
def index():
    return render_template("/public/index.html")


@app.route("/jinja")
def jinja():
    my_name = "Tawanda"
    surname = "Muzanenhamo"
    age = 23
    langs = ['Python', 'JavaScript', 'Java', 'React', 'R', 'Assembly', 'Julia']
    friends = {"Shamiso": 22, "Takunda": 12, "Kimberly": 3}
    occupation = {"University", "Primary", "Baby"}
    loved = True

    class demo():
        def __init__(self, desc, year, location):
            self.desc = desc
            self.year = year
            self.location = location

        def where(self):

            return f"At {self.location}"

        def year(self):

            return f"In the year{self.year}"

        def desc(self):

            return f"Conditions: {self.desc}"

    def factorial(x):

        if x == 1 or x == 0:
            return 1
        else:
            return x * factorial(x-1)

    the_demo = demo(desc="Teenagers", year=1996, location="Rusape")
    return render_template("/public/jinja.html", my_name=my_name, surname=surname, age=age, langs=langs,
                           friends=friends, occupation=occupation, loved=loved, factorial=factorial, demo=demo,
                           the_demo=the_demo
                           )


@app.route("/about")
def about():
    return render_template("/public/profile.html")
    #Learnt cool stuff
