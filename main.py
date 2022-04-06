from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOG_DATA = {}

@app.route('/')
def home():
    global BLOG_DATA
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    all_blogs = requests.get(blog_url).json()
    BLOG_DATA = all_blogs
    return render_template("index.html", posts=all_blogs)

@app.route('/blog/<blogid>')
def get_blog_post(blogid):
    global BLOG_DATA
    title = ''
    subtitle = ''
    body = ''
    for blog_post in BLOG_DATA:
        if blog_post['id'] == int(blogid):
            title = blog_post['title']
            subtitle = blog_post['subtitle']
            body = blog_post['body']
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
