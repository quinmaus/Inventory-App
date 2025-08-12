from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample inventory items
items = [
    {"name": "Apples", "count": 0},
    {"name": "Bananas", "count": 0},
    {"name": "Oranges", "count": 0},
    {"name": "Grapes", "count": 0}
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        idx = int(request.form["idx"])
        action = request.form["action"]
        if action == "up":
            items[idx]["count"] += 1
        elif action == "down" and items[idx]["count"] > 0:
            items[idx]["count"] -= 1
        return redirect(url_for("index"))
    return render_template("index.html", items=items)

if __name__ == "__main__":
    app.run(debug=True)