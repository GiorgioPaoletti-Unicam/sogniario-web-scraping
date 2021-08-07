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


""" 
API to view the dream list
"""


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
    if len(data) == 0:
        return "The dream list is empty"

    return render_template("table.html", headings=headings, data=data)


"""
API to visualize dream dependencies graphically
"""


@app.route('/dreams/<dream_id>')
def visualize_a_dream(dream_id):
    try:
        dream = db["tokenizedDreams"].find_one({"_id": ObjectId(dream_id)})

        doc = [
            {
                "words": dream["words"],
                "arcs": dream["arcs"]
            }
        ]
        return displacy.render(doc, style="dep", manual=True)

    except Exception:
        return "The dream with the following Id: %s not exist" % dream_id


if __name__ == '__main__':
    app.run()
