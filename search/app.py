import sys
import json

from flask import Flask
from flask import request

from search import JobSearch

app = Flask(__name__)

@app.route("/")
def hello_world():
    urls = app.job_search.search('android')
    return json.dumps(urls)


@app.route("/search", methods=['POST'])
def search():
    query = request.form['query']

    urls = app.job_search.search(query)
    return json.dumps(urls)

def server(config):
    app.job_search = JobSearch(config)
    return app


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} config.toml".format(sys.argv[0]))
        sys.exit(1)

    server(sys.argv[1]).run(debug=False, threaded=False)
