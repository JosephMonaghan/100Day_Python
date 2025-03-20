from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, g
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import *


'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# TODO: Configure Flask-Login


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)

# CONFIGURE TABLES

# TODO: Create a User table for all your registered users. 
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String,nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    posts: Mapped[list["BlogPost"]] = relationship(back_populates="author")
    comments: Mapped[list["Comment"]] = relationship(back_populates="author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = relationship("User", back_populates="posts")
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("user.id"))
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    comments: Mapped[list["Comment"]] = relationship(back_populates="parent_post")


class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] =mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(String,nullable=False)


    author: Mapped[str] = relationship("User", back_populates="comments")
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("user.id"))


    parent_post = relationship("BlogPost",back_populates="comments")
    post_id: Mapped[int] = mapped_column(Integer,db.ForeignKey("blog_posts.id"))



with app.app_context():
    db.create_all()
    # new_user = User(name = "Joseph Monaghan",
    #                 email = "Joseph_Monaghan@outlook.com",
    #                 password=generate_password_hash("MyPass12345", method='scrypt', salt_length=16))
    # db.session.add(new_user)
    # db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)

# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register',methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        #Check if user already exists
        user = db.session.execute(db.select(User).where(User.email==form.email.data)).scalar()
        if user:
            flash("Already registered - please login instead!")
            return redirect(url_for('login'))
        else:
            pass_hash = generate_password_hash(form.password.data,method='scrypt', salt_length=16)
            print(pass_hash)
            new_entry = User(
                name = form.name.data,
                password = pass_hash,
                email = form.email.data
            )
            db.session.add(new_entry)
            db.session.commit()

            login_user(new_entry)
            return redirect(url_for('get_all_posts'))

    return render_template("register.html", form = form)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login',methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email==login_form.email.data)).scalar()
        if user:
            right_pass = check_password_hash(user.password,login_form.password.data)
            if right_pass:
                login_user(user)
                return redirect(url_for('get_all_posts'))
            else:
                flash("Invalid username/password combination")
        else:
            flash("Email not registered - double check spelling & try again")
        
    return render_template("login.html", form=login_form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=["GET","POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)

    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(
            text = form.body.data,
            post_id = post_id,
            author_id = current_user.get_id()
        )
        db.session.add(new_comment)
        db.session.commit()
    
    comments = db.session.execute(db.select(Comment).where(Comment.post_id == post_id).order_by(Comment.id.desc())).scalars()

    return render_template("post.html", post=requested_post, comment_form=form, comments = comments)


# TODO: Use a decorator so only an admin user can create a new post

def adminonly(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        print(current_user.get_id())
        if current_user.get_id() == "1":
            return func(*args, **kwargs)
        else:
            return abort(403)
    return decorated


@app.route("/new-post", methods=["GET", "POST"])
@adminonly
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@adminonly
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@adminonly
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
