from flask import Flask, jsonify, render_template, request
from elasticsearch6 import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


elastic = Elasticsearch()

@app.route('/', methods=["GET"])
def home():
    body = {
        "size" : 1000,
        "query" : {
            "match_all":{}
        }
    }
    resp = elastic.search(index="captures", body = body)

    return jsonify({"data": resp['hits']['hits']})


if __name__=='__main__':

    app.run(debug = True, port = 5000)