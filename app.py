from flask import Flask, request, render_template, redirect, session, url_for, send_from_directory

app = Flask(__name__)
app.secret_key = "UneSuperCleSecrete"  # Nécessaire pour les sessions

# Identifiants d'accès
USERNAME = "SuperTK79"
PASSWORD = "SuperSecret123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USERNAME and password == PASSWORD:
            session["user"] = username
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", username=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route('/ad_free')
def index():
    return render_template('index.html')

@app.route('/AdFree.apk')
def download_apk():
    return send_from_directory('.', 'ad_free.apk', as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

