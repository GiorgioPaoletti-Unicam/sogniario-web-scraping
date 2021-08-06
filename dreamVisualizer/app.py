from bson.objectid import ObjectId
from flask import Flask, render_template
from flask import redirect, url_for
from pymongo import MongoClient
from spacy import displacy

app = Flask(__name__)

client = MongoClient()
db = client['Dreams']


@app.route('/')
def index():
    return redirect(url_for('dreams_list'))


@app.route('/dreams')
def dreams_list():
    collections = [
        "internationalarchiveofdreamsDreams",
        "thedreamarchiveDreams",
        # "cepeiDreams"
    ]

    headings = ["ID", "Title", "Date", "Text"]
    data = []
    for collection_name in collections:
        for dream in db[collection_name].find({}):
            data.append([dream["_id"],
                         dream["title"] if dream["title"] is not None else "",
                         dream["date"] if dream["date"] is not None else "",
                         dream["text"] if dream["text"] is not None else ""
                         ])

    return render_template("table.html", headings=headings, data=data)


@app.route('/dreams/<dream_id>')
def visualize_a_dream(dream_id):
    dream = db["tokenizedDreams"].find_one({"_id": ObjectId(dream_id)})

    doc = [
        {
            "words": dream["words"],
            "arcs": dream["arcs"]
        }
    ]
    return displacy.render(doc, style="dep", manual=True)


if __name__ == '__main__':
    app.run()
