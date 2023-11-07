from flask import render_template, redirect, url_for

from dictsite import app
from dictsite.forms import SearchWord
from dictsite.fetch import get_definition


@app.route("/", methods=["POST", "GET"])
def home():
    form = SearchWord()

    if form.validate_on_submit():
        word = form.word.data
        definition = get_definition(word)
        return render_template("home.html", word=word, definition=definition, form=form)

    return render_template("home.html", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
