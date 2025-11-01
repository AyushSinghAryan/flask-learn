from flask import Flask , request ,redirect,url_for,session,Response,render_template 

app = Flask(__name__)
# app.secret_key = "supersecret"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit", methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "ayush123" and password == "12345":
    #     return render_template("welcome.html" , name = username)
    # else:
    #     return "Invalid Credentials "

    valid_credentials={
        "ayush":"12345",
        "aryan":"alexa",
        "singh":"asa"
    } 

    if username in valid_credentials and password == valid_credentials[username]:
        return render_template("welcome.html",name=username)
    else:
        return "invalid credentials"





if __name__ == '__main__':
    app.run(debug=True)
