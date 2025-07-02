from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

def load_posts():
    """Opens the json file and loads blog posts"""
    with open("blog_posts.json", "r") as fileobj:
        blog_posts = json.load(fileobj)
    return blog_posts

def save_blog_posts(posts):
    """Updates the json file"""
    with open('blog_posts.json', 'w') as fileobj:
        json.dump(posts, fileobj)


def fetch_post_by_id(post_id):
    """Fetch blog posts per ID"""
    blog_posts = load_posts()
    for post in blog_posts:
        if post['id'] == post_id:
            return post
    return None



@app.route('/greeting')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def index():
    blog_posts = load_posts()
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
       author=request.form.get('author')
       title=request.form.get('title')
       content=request.form.get('content')

       blog_posts=load_posts()
       new_post={
       'id' : len(blog_posts)+1,
       'author': author,
       'title': title,
       'content': content,
       }
       blog_posts.append(new_post)
       save_blog_posts(blog_posts)

       return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):

    blog_posts = load_posts()
    updated_posts = [post for post in blog_posts if post['id'] != post_id]

    save_blog_posts(updated_posts)
    return redirect(url_for('index'))

@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    # Fetch the blog posts from the JSON file
    post = fetch_post_by_id(post_id)

    if post is None:
        # Post not found
        return "Post not found", 404

    if request.method == 'POST':
        # Update the post in the JSON file
        post['author'] = request.form.get('author')
        post['title'] = request.form.get('title')
        post['content'] = request.form.get('content')

        # Fetch all posts
        blog_posts = load_posts()

        # Update the post in the list
        for idx, p in enumerate(blog_posts):
            if p['id'] == post_id:
                blog_posts[idx] = post
                break

        # Save updated list to JSON file
        save_blog_posts(blog_posts)

        # Redirect back to the home page
        return redirect(url_for('index'))

    # Display the update.html page
    return render_template('update.html', post=post)

@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    blog_posts = load_posts()

    for post in blog_posts:
        if post['id'] == post_id:
            post['likes'] = post.get('likes', 0) + 1
            break

    save_blog_posts(blog_posts)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4999, debug=True)