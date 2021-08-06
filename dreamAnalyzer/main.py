import spacy
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient()
    db = client['Dreams']

    collections = [
        "internationalarchiveofdreamsDreams",
        "thedreamarchiveDreams",
        # "cepeiDreams"
    ]
    collection_to = db["tokenizedDreams"]

    nlp = None

    for collection_name in collections:
        for dream in db[collection_name].find({}):

            try:
                nlp = spacy.load(dream["language"] + "_core_web_sm")
            except Exception:
                print("The dream with the following Id: %s has a non-existent language" % dream["_id"])
                continue

            doc = nlp(dream["text"])

            doc_map = {}
            words = []
            arcs = []
            for token in doc:

                token_text = token.text

                if token.pos_ == "VERB":
                    token_text = token.lemma_

                if token.pos_ == "AUX":
                    continue

                if token.pos_ == "PART" and token.dep_ == "neg":
                    token_text = "not"

                words.append({
                    "text": token_text,
                    "tag": token.tag_
                })

                arcs.append({
                    "start": token.head.i,
                    "end": token.i,
                    "label": token.dep_,
                    "dir": "right" if token.head.i > token.i else "left"
                })

            doc_map["words"] = words
            doc_map["arcs"] = arcs

            collection_to.insert_one(doc_map)
