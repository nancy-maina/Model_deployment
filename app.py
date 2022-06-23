from re import template
from flask import Flask, render_template, request
import music

app = Flask(__name__)

@app.route("/, methods = ['POST]")
def hello():
    if request.methid == "POST":
        name = request.form["genre"]
        music_pred = music.music.prediction(genre)

        print(music_pred)
    return render_template("index.html")


#@app.route("/sub", methods = ["POST"])
#def submit():
    #HTML => .py
  #  if request.method == "POST":
   #     name = request.form["username"]
    
    #.py => HTML

    #return render_template("sub.html", n = name)


if __name__ == "__main__":
    app.run()