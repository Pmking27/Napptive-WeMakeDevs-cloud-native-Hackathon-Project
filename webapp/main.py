from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/ff4783055aa65fc65d27").json()

email = requests.get("https://api.npoint.io/39c00547fec65def5034").json()
my_email=str(email['email'])
my_password=str(email['key'])

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True,)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=email_message
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=int("3000"),debug=True)
