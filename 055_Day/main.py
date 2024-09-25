from flask import Flask
import random

tgt_number = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def homepage():
    site_txt = "<h1>Guess a number between 1 and 9</h1>"
    site_txt += "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=400px>"
    return site_txt

@app.route("/<int:num>")
def is_num(num):
    global tgt_number
    if num == tgt_number:
        response_txt = "<h1>You got it!</h1>"
        response_txt+= "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzVieGJ5c25rc3M5MTJ3NjRjMGF2c3NhMjhxbWdpMXg4dDRhYm9oOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XkGXBa01dxNIvjAJHl/giphy.gif' width=400px>"
    elif num > tgt_number:
        response_txt = "<h1>Too high!</h1>"
        response_txt += "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3RhaGYxaTlncDEzaDdoc2ZlODY4b3RoNzJ2NXZxODlta3Z5dmNkYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2YWy9pD8sZEUMF0s/giphy.gif' width=400px>"
    elif num < tgt_number:
        response_txt = "<h1>too low!</h1>"
        response_txt += "<img src='https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHc5OXBueThzN3g2NnVzbWNwd3dubGk2bDM1aWNybjFiMW1nc3BseiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TgmiJ4AZ3HSiIqpOj6/giphy.gif' width=400px>"
    
    return response_txt

if __name__=="__main__":
    app.run(debug=True)
