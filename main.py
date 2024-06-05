from flask import Flask,render_template,redirect,request

import requests
blog_url="https://api.npoint.io/674f5423f73deab1e9a7"
response=requests.get(blog_url)
all_data=response.json()
import smtplib

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

@app.route("/contact",methods=["GET","POST"])

def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        message=f"Name : {data["name"]} \n Email : {data["email"]} \n Phone Number : {data["phone"]} \n Message : {data["message"]}"
        
        from email.mime.text import MIMEText
        msg=MIMEText(message)
        receipient="ap22csb0a10@student.nitw.ac.in"
        sender="anirudhpabbaraju1103@gmail.com"
        password='atnipcvnvvxvcghn'
        msg['Subject']="Happy Birthday!"
        msg['From']=sender
        msg['To']=receipient
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
            smtp_server.login(sender,password)
            smtp_server.sendmail(sender,receipient,msg.as_string())
            
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
        
       
        




if __name__=="__main__":
    app.run(debug=True)