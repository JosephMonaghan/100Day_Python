from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, URL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
    pass


class BookForm(FlaskForm):
    rating_choices = [x+1 for x in range(10)]
    bookname = StringField(label='bookname', validators=[DataRequired()])
    author = StringField(label='author',validators=[DataRequired()])
    rating = SelectField(label='rating',choices=rating_choices,validators=[DataRequired()])
    submit = SubmitField(label="submit")

class RatingForm(FlaskForm):
    rating_choices = [x+1 for x in range(10)]
    rating = SelectField(label='rating',choices=rating_choices, validators=[DataRequired()])
    submit = SubmitField(label="submit")


db = SQLAlchemy(model_class = Base)

app = Flask(__name__)
app.secret_key="mysecretkeyissupersecret"
bootstrap = Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    
    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()

def render_home():
    res = db.session.execute(db.select(Book).order_by(Book.title))
    my_books = res.scalars().all()
    return render_template("index.html",books=my_books)



@app.route('/')
def home():
    return render_home()


@app.route("/edit/<int:idx>", methods=["GET", "POST"])
def edit(idx:int):
    form = RatingForm()
    result = db.session.execute(db.select(Book).where(Book.id==idx)).scalar()

    if form.validate_on_submit():
        book_to_update = db.get_or_404(Book, idx)
        book_to_update.rating = form.rating.data
        db.session.commit()
        return redirect(url_for("home"))


    return render_template('edit.html',book=result,rating_form = form)


@app.route("/add",methods=["GET","POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_entry = Book(title=form.bookname.data,author=form.author.data,rating=form.rating.data)
        db.session.add(new_entry)
        db.session.commit()


        return redirect(url_for("home"))

    
    return render_template("add.html",myform=form)

@app.route("/delete/<int:idx>")
def delete(idx):
    book_to_delete = db.get_or_404(Book,idx)
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

