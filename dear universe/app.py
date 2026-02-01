from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
app.secret_key = "dear_universe_secret_key"

from flask import session

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # OWNER CREDENTIALS (hardcoded for now)
        if username == "admin" and password == "dearuniverse":
            session["owner"] = True
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("owner"):
        return redirect(url_for("login"))

    return render_template("dashboard.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now we just print (later: email, database, WhatsApp, etc.)
        print(name, email, message)

        return redirect(url_for("contact"))

    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/collection")
def collection():
    return render_template("collection.html")

@app.route("/shop")
def shop():
    products = [
        {
            "id": 1,
            "name": "Universe Tee",
            "price": "₵150",
            "image": "images/tee.jpg",
            "description": "Minimal unisex tee designed for everyday gravity."
        },
        {
            "id": 2,
            "name": "Universe Hoodie",
            "price": "₵350",
            "image": "images/hoodie.jpg",
            "description": "Heavyweight hoodie with a relaxed cosmic fit."
        },
        {
            "id": 3,
            "name": "Universe Jacket",
            "price": "₵200",
            "image": "images/jacket.jpg",
            "description": "Bold outerwear for colder orbits."
        }
    ]
    return render_template("shop.html", products=products)

@app.route("/product/<int:product_id>")
def product(product_id):
    products = [
        {
            "id": 1,
            "name": "Universe Tee",
            "price": "₵150",
            "image": "images/tee.jpg",
            "description": "Minimal unisex tee designed for everyday gravity."
        },
        {
            "id": 2,
            "name": "Universe Hoodie",
            "price": "₵300",
            "image": "images/hoodie.jpg",
            "description": "Heavyweight hoodie with a relaxed cosmic fit."
        },
        {
            "id": 3,
            "name": "Universe Jacket",
            "price": "₵200",
            "image": "images/jacket.jpg",
            "description": "Bold outerwear for colder orbits."
        }
    ]

    selected_product = next(
        (p for p in products if p["id"] == product_id), None
    )

    return render_template("product.html", product=selected_product)



if __name__ == "__main__":
    app.run(debug=True)
