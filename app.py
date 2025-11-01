from flask import Flask , request ,redirect,url_for,session,Response,render_template ,flash

app = Flask(__name__)
app.secret_key = "supersecret"

app.route("/" , methods = ["GET","POSt"])
def form():
    if request.form == "POST":
        name = request.form.get("name")
        if not name:
            flash("name can not be empty")
            return redirect("form")
        flash(f"Thanks {name} , your feedback was saved")
        return render_template("thankyou.html")    
    return render_template("form.html") 

app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == '__main__':
    app.run(debug=True)
