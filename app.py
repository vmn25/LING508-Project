from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
from logging.config import dictConfig

from app.services import Services
from model.generators import Noun

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

services = Services()


@app.before_request
def basic_authentication():
    if request.method.lower() == 'options':
        return Response()


@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("web/viet.html", "r") as f:
        return f.read()


@app.route("/noun_data/<noun>", methods=["GET"])
def noun_data(noun: str):
    res = services.noun_classifier(noun)
    app.logger.info("/noun_data - Got noun data: " + noun)
    return jsonify(english=res.eng, classifier=res.classifier.value if res.classifier else "N/A", vietnamese=res.viet)


@app.route("/noun_storage", methods=["POST"])
def noun_storage():
    data = request.get_json()
    app.logger.info(f"/noun_storage - Got noun storage data: {data}")
    # data.headers.add('Access-Control-Allow-Origin', '*')
    res = services.parse_noun(data)
    if services.add_noun(res):
        return jsonify({"msg": "Noun has been added successfully"})
    else:
        return jsonify({"msg": "Noun is already added"})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
