from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")  # NEW landing page


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # ✅ You can add email sending here later
        print(f"Message received from {name} ({email}): {message}")
        return render_template("contact.html", success=True)
    return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)
