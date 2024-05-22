from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    resp = requests.get('https://api.npoint.io/19c4467e9b0030cad0fd')
    data = resp.json()
    return render_template('index.html', all_blogs=data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/blog/<id>')
def get_blog(id):
    resp = requests.get(f'https://api.npoint.io/19c4467e9b0030cad0fd/{id}')
    data = resp.json()
    return render_template("post.html", blog=data)


if __name__ == "__main__":
    app.run(debug=True)
