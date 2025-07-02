from flask import Flask ,render_template
# In-memory list of blog posts


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'
from flask import

@app.route('/')
def index():
    blog_post = random.choice(blog_posts)
    return render_template('index.html', posts=blog_posts)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999, debug=True)