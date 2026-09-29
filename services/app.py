from flask import Flask, render_template
import os
from db import db, connect_db
import models

app=Flask(
    __name__,
    template_folder="../frontend/pages",
    static_folder="../frontend",
    static_url_path="/static"

    )


app.config["SQLALCHEMY_DATABASE_URI"]=connect_db()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<page>.html")
def html_page(page):
    return render_template(f"{page}.html")

if __name__=="__main__":
    app.run(debug=True,port=5000)