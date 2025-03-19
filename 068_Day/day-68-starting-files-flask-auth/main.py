from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

# CREATE TABLE IN DB


class User(UserMixin,db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register',methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #Check if user already exists
        user = db.session.execute(db.select(User).where(User.email==request.form["email"])).scalar()
        if user:
            flash("Already registered - please login instead!")
            return redirect(url_for('login'))
        else:
            pass_hash = generate_password_hash(request.form["password"],method='scrypt', salt_length=16)
            print(pass_hash)
            new_entry = User(
                name = request.form["name"],
                password = pass_hash,
                email = request.form['email']
            )
            db.session.add(new_entry)
            db.session.commit()

            login_user(new_entry)
            return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login',methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.session.execute(db.select(User).where(User.email==request.form["email"])).scalar()
        if user:
            right_pass = check_password_hash(user.password,request.form["password"])
            if right_pass:
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash("Incorrect username/password")
        else:
            flash("Email is not registered, double check spelling & try again")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory("static","files/Cheat_Sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
