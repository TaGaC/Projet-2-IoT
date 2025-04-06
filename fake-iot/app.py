from flask import Flask, request, render_template, redirect

app = Flask(__name__)
password = "SuperSecret123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("password") == password:
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
