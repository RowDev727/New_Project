from flask import Blueprint, render_template, url_for

main = Blueprint("main", __name__)

posts = [
    {
        "author": "chris",
        "title": "Post number 1",
        "content": "This is just some dummy text",
        "date_posted": "November 26, 2023"
    },
    {
        "author": "Josh",
        "title": "Post number 2",
        "content": "This is more dummy text",
        "date_posted": "November 27, 2023"
    }
]



@main.route("/")
def home():
    return render_template("index.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html")
