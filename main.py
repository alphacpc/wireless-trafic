from flask import Flask, jsonify, render_template, request
from elasticsearch6 import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

elastic = Elasticsearch()

@app.route('/api/all', methods=["GET"])
def home():
    body = {
        "size" : 10000,
        "query" : {
            "match_all":{}
        }
    }
    resp = elastic.search(index="captures", body = body)

    return jsonify({"data": resp['hits']['hits']})






@app.route('/protocol', methods=["GET"])
def protocole():
    body = {
        "aggs": {
            "keys": {
                "terms": {
                    "field": "dst_port.keyword"
                }
            }
        },
        "size": 0
    }
    
    resp = elastic.search(index="captures", body = body)

    return jsonify({"data": resp['aggregations']['keys']['buckets']})







@app.route('/length', methods=["GET"])
def length():
    body = {
        "aggs": {
            "keys": {
                "terms": {
                    "field": "information.keyword"
                }
            }
        },
        "size": 0
    }
    
    resp = elastic.search(index="captures", body = body)

    return jsonify({"data": resp['aggregations']['keys']['buckets']})





@app.route('/api/dns_name', methods=["GET"])
def domaine_name():
    body = {
        "query": {
            "match": {
                "isDNS": "True"
            }
        },
        "size": 0,
        "aggs": {
            "keys": {
            "terms": {
                "field": "information.keyword"
            }
            }
        }
    }
    
    resp = elastic.search(index="captures", body = body)

    return jsonify({"data": resp['aggregations']['keys']['buckets']})




@app.route('/api/protocol_daily', methods=["GET"])
def protocol_daily():
    body = {
        "size": 0, 
        "aggs": {
            "daily_agg": {
                "date_histogram": {
                    "field": "today",
                    "interval": "day"
                },
                "aggs": {
                    "country_agg": {
                        "terms": {
                            "field": "protocol.keyword",
                            "size": 2
                        }
                    }
                }
            }
        }
    }
    
    resp = elastic.search(index="captures", body = body)

    return jsonify({"data": resp['aggregations']['daily_agg']['buckets']})




if __name__=='__main__':

    app.run(debug = True, port = 5000)



# "illegal_argument_exception","reason" : "La fenêtre de résultat est trop grande, de + la taille doit être inférieure ou égale à : [10000] mais était [20000]. Voir l'api scroll pour un moyen plus efficace de demander de grands ensembles de données. Cette limite peut être fixée en modifiant le paramètre de niveau d'index [index.max_result_window]."