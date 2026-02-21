from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "super secret key"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method=="POST":
		session.permanent=True
		user=request.form["username"]
		session["username"]=user
		session["first_login"]=True
		return redirect(url_for("user",name=user))
	
	return render_template('login.html')

@app.route("/user/")
def user():
    if "username" in session: 
        name=session["username"]
        if session.get("first_login"):
            flash(f"Log in successful for {name}",category="info")
            session["first_login"]=False
        else:
            flash(f"Welcome back {name}!",category="info")
        return render_template('user.html',name=name)
    else:
        flash("You are not logged in!",category="error")
        return redirect(url_for("login")) 

@app.route("/logout")
def logout():
    username = session.get("username")
    session.pop("username",None)
    flash(f"You have been logged out, {username}!",category="info")
    return redirect(url_for("home"))
    

if __name__ == "__main__":
	app.run(debug=True)