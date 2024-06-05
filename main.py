from flask import Flask,render_template,redirect

import requests
blog_url="https://api.npoint.io/674f5423f73deab1e9a7"
response=requests.get(blog_url)
all_data=response.json()

app=Flask(__name__)

@app.route("/")

def start():
    return render_template("index.html",blog=all_data)

@app.route("/about")

def about():
    return render_template("about.html")

@app.route("/post/<int:id>")

def post(id):
    req_blog=[blog for blog in all_data if blog["id"]==id]
    return render_template("post.html",blog=req_blog[0])

@app.route("/contact")

def contact():
    return render_template("contact.html")




if __name__=="__main__":
    app.run(debug=True)