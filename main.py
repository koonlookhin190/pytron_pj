from googleapiclient.discovery import build
from flask import Flask, request, jsonify
from flask_cors import CORS

my_api_key = "AIzaSyCmRvHOP1wJM5rUF9JMlpHgOA8yaaytae0"
# my_api_key = "AIzaSyCK2TB3yEzihRCiH9h17xUSbIZbR8nWbEk"
my_cse_id = "03082958736eb4b86"
# my_cse_id = "a454c0eb1bb48467b"

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


@app.route('/search', methods=['GET'])
def search_query():
    query = request.args.get("find", default="", type=str)
    results = google_search(query, my_api_key, my_cse_id)
    for result in results:
        print(result)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
