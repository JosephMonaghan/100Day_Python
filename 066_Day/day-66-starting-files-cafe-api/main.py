from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random as rd

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random",methods=["GET"])
def random():
    all_db = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = all_db.scalars().all()
    random_cafe = rd.choice(all_cafes)
    # cafe_dict = random_cafe.__dict__
    
    # export_json = {}
    # for key in cafe_dict.keys():
    #     if not key.startswith("_"):
    #         export_json[key] = cafe_dict[key]

    return {"cafe":random_cafe.to_dict()}

@app.route("/all",methods=["GET"])
def all():
    all_db = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = all_db.scalars().all()


    return {"cafes":[cafe.to_dict() for cafe in all_cafes]}
    
@app.route("/search")
def search():  
    loc = request.args.get("loc")
    search_results = db.session.execute(select(Cafe).where(Cafe.location == loc)).scalars()

    if len(list(search_results)) == 0:
        return {"error": {"Not Found": "Sorry, we don't have a cafe at that location."}}
    else:
        search_results = db.session.execute(select(Cafe).where(Cafe.location == loc)).scalars()
        return {"cafes":[cafe.to_dict() for cafe in search_results]}
    

    

# HTTP POST - Create Record
@app.route("/add",methods=["POST"])
def add():
    try:
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("has_sockets")),
            has_toilet=bool(request.form.get("has_toilet")),
            has_wifi=bool(request.form.get("has_wifi")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )

        db.session.add(new_cafe)
        db.session.commit()
        return {"response":{"success":"Successfully added a new cafe"}}
    except Exception as e:
        print(e)
        return {"Failed":"Something went wrong"}


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def update_price(cafe_id:int):
    
    my_shop = db.get_or_404(Cafe,cafe_id)
    if my_shop:
        my_shop.coffee_price = request.form.get("price")

        db.session.commit()
        return jsonify(response = {"success": f"Successfully updated price for {my_shop.name}"}), 200
    else:
        return jsonify(response = {"Failed": "Something went wrong..."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>")
def report_closed(cafe_id:int):
    api_token = request.args.get("api-token")
    if api_token == "MySecretCode":
        my_shop = db.get_or_404(Cafe,cafe_id)
        if my_shop:
            db.session.delete(my_shop)
            db.session.commit()
            return jsonify(response = {"Success":f"{my_shop.name} was successfully removed"})
        else:
            return jsonify(error= {"Failed": "No cafe with that id was found"}), 404

    else:
        return jsonify(error = {"Failed": "No Authorization token"}), 403
    


if __name__ == '__main__':
    app.run(debug=True)
