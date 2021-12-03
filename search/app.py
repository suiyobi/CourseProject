import sys
import json

from flask import Flask, request, jsonify
from flask import request

from search import JobSearch

app = Flask(__name__)

@app.route("/")
def hello_world():
    urls = app.job_search.search('android')
    return json.dumps(urls)


@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query')

    urls = app.job_search.search(query)
    # response = json.dumps(urls)
    response = jsonify(urls)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def server(config):
    app.job_search = JobSearch(config)
    return app


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} config.toml".format(sys.argv[0]))
        sys.exit(1)

    server(sys.argv[1]).run(debug=False, threaded=False)
