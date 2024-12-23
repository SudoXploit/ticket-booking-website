from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/book")
def book():
    ticket_type = request.args.get("ticket_type")
    quantity = request.args.get("quantity")
    return render_template("book.html", ticket_type=ticket_type, quantity=quantity)

@app.route("/confirmation", methods=["POST"])
def confirmation():
    data = request.form
    name = data.get("name")
    email = data.get("email")
    ticket_type = data.get("ticket_type")
    quantity = data.get("quantity")
    return render_template("confirmation.html", name=name, email=email, ticket_type=ticket_type, quantity=quantity)

if __name__ == "__main__":
    app.run(debug=True)
