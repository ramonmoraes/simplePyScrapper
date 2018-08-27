from flask import Flask, render_template, request
from snippet.__init__ import get_db
app = Flask(__name__)

@app.route("/")
def simple_view():
    collection_name = 'snippets'
    query_colletion = user = request.args.get('collection')
    if query_colletion != None:
        collection_name = query_colletion

    collection = get_db()[collection_name]
    cursor = collection.find({})
    arr_sni = list(map(lambda x: x, cursor))
    return render_template('index.html', snippets=arr_sni)