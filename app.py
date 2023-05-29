from flask import *
from engines.google import google_search
from engines.wiki import getWikiSummary
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/search/", methods=["GET"])
def search():
    query = request.args.get('query')
    selectedLang = request.args.get('lang')
    if query:
        wiki = getWikiSummary(query, lang=selectedLang)
        results = google_search(query, lang=selectedLang)
        return render_template("index.html", results = results, query = query)

    else:
        return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
