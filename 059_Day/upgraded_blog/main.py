from flask import Flask, render_template
import requests

app = Flask(__name__)


api_endpoint = 'https://api.npoint.io/cd5be0119dd1cb4c5ded'
posts = requests.get(api_endpoint).json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog/<num>")
def blog_post(num):
    post = posts[int(num)-1]
    return render_template("post.html",post=post)



if __name__ == "__main__":
    app.run(debug=True)