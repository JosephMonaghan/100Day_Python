from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

load_dotenv()
api_token = os.getenv("movie_API_token")

class RatingForm(FlaskForm):
    rating = FloatField(label='Rating',validators=[DataRequired()],description="Your rating out of 10 (e.g. 7.5)")
    review = StringField(label='Review')
    submit = SubmitField()



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class = Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

class Movies(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float] = mapped_column(Float,nullable=True)
    ranking: Mapped[int] = mapped_column(Integer,nullable=True)
    review: Mapped[str] = mapped_column(String(1000),nullable=True)
    img_url: Mapped[str] = mapped_column(String,nullable=False)

    def __repr__(self):
        return f"<Movie {self.id}: {self.title}>"
    

with app.app_context():
    db.create_all()


# with app.app_context():
#     entry = Movies(
#         title="Avatar the Way of Water",
#         year = 2022,
#         description = "Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating = 7.3,
#         ranking = 9,
#         review = "I liked the water.",
#         img_url = "https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
#     db.session.add(entry)
#     db.session.commit()

# CREATE TABLE


@app.route("/")
def home():
    all_db = db.session.execute(db.select(Movies).order_by(Movies.rating.desc()))
    my_movies = all_db.scalars().all()
    for idx, movie in enumerate(my_movies):
        movie.ranking = idx + 1
    db.session.commit()


    return render_template("index.html",movies = my_movies)

@app.route("/edit/<int:idx>", methods=["GET", "POST"])
def edit(idx):
    entry = db.get_or_404(Movies,idx)
    rating_form = RatingForm()

    if rating_form.validate_on_submit():
        entry = db.get_or_404(Movies,idx)
        entry.rating = rating_form.rating.data
        entry.review = rating_form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html',movie = entry,form = rating_form)

@app.route("/delete/<int:idx>")
def delete(idx):
    entry = db.get_or_404(Movies,idx)
    db.session.delete(entry)
    db.session.commit()

    return redirect(url_for('home'))

class AddMovie(FlaskForm):
    movie = StringField(label='Movie',validators=[DataRequired()],description="Enter your favourite movie here!")
    submit = SubmitField("Add Movie")



movie_matches = []

@app.route("/selected/<int:idx>")
def selected(idx):
    selected_movie = movie_matches[idx]
    
    new_DB_entry = Movies(
        title = selected_movie["title"],
        year = selected_movie["year"],
        description = selected_movie["description"],
        img_url = selected_movie["img_url"],
    )
    db.session.add(new_DB_entry)
    db.session.commit()

    db.session.refresh(new_DB_entry)


    return redirect(url_for('edit',idx=new_DB_entry.id))

@app.route("/select")
def select():
    return render_template("select.html", matches = movie_matches)


@app.route("/add",methods=["GET","POST"])
def add():
    form = AddMovie()

    if form.validate_on_submit():
        url = "https://api.themoviedb.org/3/search/movie"
        
        headers = {"accept": "application/json",
                   "Authorization": f"Bearer {api_token}"}
        
        params = {
            "query": form.movie.data,
            "include_adult": "true",
            "language":"en-US",
            "page":"1"
        }

        response = requests.get(url, headers=headers,params=params)
        all_hits = response.json()['results']
        global movie_matches
        movie_matches = []

        for idx, movie in enumerate(all_hits):
            new_entry = {
                "loop_id": idx,
                "title": movie['title'],
                'year': movie['release_date'],
                'description': movie['overview'],
                'rating': movie['vote_average'],
                'img_url': f"https://image.tmdb.org/t/p/original/{movie['poster_path']}"
            }
            movie_matches.append(new_entry)
        
        return redirect(url_for('select'))
        
        # new_entry = Movies(
        # title = top_hit['title'],
        # description = top_hit['overview'],
        # year = int(top_hit['release_date'].split("-")[0]),
        # rating = top_hit['vote_average'],
        # img_url = f"https://image.tmdb.org/t/p/original/{top_hit['poster_path']}")

        # db.session.add(new_entry)
        # db.session.commit()

        # return redirect(url_for('home'))

    return render_template('add.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
