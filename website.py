from flask import Flask, render_template
from flask import request, jsonify, redirect, session, url_for
from werkzeug import secure_filename
from storage import get_archive, get_file_text
import pymysql.cursors

app = Flask(__name__)

def escape_double_quotes(text):
    new = text.replace('"', r"\"")
    return new

@app.route('/')
def home():
    archive = get_archive()
    recent_post = get_file_text(archive[sorted(archive.keys(), reverse=True)[0]])
    recent_post = escape_double_quotes(repr(recent_post))
    return render_template("home.html", post=recent_post, active="Home")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/archive')
def projects():
    archive = get_archive()
    return render_template("archive.html", archive=archive)

@app.route('/archive/<post>')
def post(post):
    post_text = escape_double_quotes(repr(get_file_text(post)))
    return render_template("home.html", post=post_text, active="Archive")

if __name__ == "__main__":
    app.run()
