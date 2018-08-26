from flask import Flask, render_template
from snippet.__init__ import get_db
app = Flask(__name__)

@app.route("/")
def simple_view():
    collection = get_db()['snippets']
    cursor = collection.find({})
    arr_sni = list(map(lambda x: x, cursor))
    return render_template('index.html', snippets=arr_sni)