from flask import Flask, render_template, send_from_directory
import os

BLOG = './templates/blogposts/'
app = Flask(__name__)

def escape_double_quotes(text):
    new = text.replace('"', r"\"")
    return new

def getlatestpost(posts):
  latest = posts[0]
  latesttime = os.stat(BLOG+posts[0]).st_ctime
  for post in posts:
    time = os.stat(BLOG+post).st_mtime
    if time > latesttime:
      latest = post
      latesttime = time
  return latest

@app.route('/')
def home():
    archive = os.listdir(BLOG)
    recent_post = 'blogposts/' + getlatestpost(archive)
    return render_template("home.html", post=recent_post, active="Home")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/archive')
def projects():
    archive = os.listdir(BLOG)

    return render_template("archive.html", archive=archive)

@app.route('/archive/<post>')
def post(post):
    postpath = 'blogposts/' + post
    return render_template("home.html", post=postpath, active="Archive")

if __name__ == "__main__":
    app.run()
