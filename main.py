from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

from models.outfit import Outfit
from utils.file_handler import load_outfits, save_outfits

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():

    return render_template("home.html")


@app.route("/add", methods=["GET", "POST"])
def add_outfit():

    if request.method == "POST":

        top = request.form["top"]
        bottom = request.form["bottom"]
        shoes = request.form["shoes"]
        style = request.form["style"]
        event = request.form["event"]
        weather = request.form["weather"]

        image_file = request.files["image"]

        image_name = ""

        if image_file.filename != "":
            image_name = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config["UPLOAD_FOLDER"], image_name))

        new_outfit = Outfit(
            top,
            bottom,
            shoes,
            style,
            event,
            weather,
            image_name
        )
        outfits = load_outfits()

        outfits.append(
            new_outfit.to_dict()
        )

        save_outfits(outfits)

        return redirect("/outfits")

    return render_template("add.html")


@app.route("/outfits")
def outfits():

    all_outfits = load_outfits()

    return render_template(
        "outfits.html",
        outfits=all_outfits
    )


@app.route("/delete/<int:index>")
def delete_outfit(index):

    outfits = load_outfits()

    if 0 <= index < len(outfits):
        outfits.pop(index)
        save_outfits(outfits)

    return redirect("/outfits")


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_outfit(index):

    outfits = load_outfits()

    if index < 0 or index >= len(outfits):
        return redirect("/outfits")

    if request.method == "POST":

        outfits[index]["top"] = request.form["top"]
        outfits[index]["bottom"] = request.form["bottom"]
        outfits[index]["shoes"] = request.form["shoes"]
        outfits[index]["style"] = request.form["style"]
        outfits[index]["event"] = request.form["event"]
        outfits[index]["weather"] = request.form["weather"]

        save_outfits(outfits)

        return redirect("/outfits")

    return render_template("edit.html", outfit=outfits[index], index=index)


@app.route("/filter", methods=["GET", "POST"])
def filter_outfits():

    outfits = load_outfits()
    filtered_outfits = []

    if request.method == "POST":

        style = request.form["style"]
        event = request.form["event"]
        weather = request.form["weather"]

        for outfit in outfits:

            matches = 0

            if outfit["style"] == style:
                matches += 1

            if outfit["event"] == event:
                matches += 1

            if outfit["weather"] == weather:
                matches += 1

            if matches >= 2:
                filtered_outfits.append(outfit)

    return render_template("filter.html", outfits=filtered_outfits)


@app.route("/recommend", methods=["GET", "POST"])
def recommend_outfit():

    outfits = load_outfits()
    recommended = None

    if request.method == "POST":

        event = request.form["event"]
        weather = request.form["weather"]

        best_match = 0

        for outfit in outfits:

            matches = 0

            if outfit["event"] == event:
                matches += 1

            if outfit["weather"] == weather:
                matches += 1

            if matches > best_match:
                best_match = matches
                recommended = outfit

    return render_template("recommend.html", outfit=recommended)

if __name__ == "__main__":

    app.run(debug=True)