from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    blog_request = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blog_request.json()
    return render_template("index.html", all_posts=all_posts)


@app.route("/blog/<num>")
def blog_post(num):
    blog_request = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = blog_request.json()

    my_post = all_posts[int(num) - 1]
    return render_template("post.html", post=my_post)


if __name__ == "__main__":
    app.run(debug=True)
