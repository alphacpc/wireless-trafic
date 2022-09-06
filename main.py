from flask import Flask, jsonify
from elasticsearch6 import Elasticsearch
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

elastic = Elasticsearch()



### GET ALL HITS FROM APIs ###
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




### GET TOP 10 DOMAINE NAME APIs ###
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



### GET PROTOCOL COUNT DAILY  ###
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
                    "protocol_agg": {
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