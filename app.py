from flask import Flask ,render_template
import json


app = Flask(__name__)

def load_posts():
    """Opens the json file and loads blog posts"""
    with open("blog_posts.json", "r") as fileobj:
        blog_posts = json.load(fileobj)
    return blog_posts

@app.route('/greeting')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999, debug=True)