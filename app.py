from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory user storage (no backend)
users = [
    {"id": 1, "name": "John Doe", "email": "john@gmail.com"},
    {"id": 2, "name": "Alice", "email": "alice@gmail.com"}
]

# Home page
@app.route("/")
def index():
    return render_template("index.html", users=users)


# Add user
@app.route("/add-user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        return jsonify(status="error", message="Name and Email required")

    new_id = users[-1]["id"] + 1 if users else 1

    users.append({
        "id": new_id,
        "name": name,
        "email": email
    })

    return jsonify(status="success")


# Delete user
@app.route("/delete-user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify(status="success")


# Update user
@app.route("/update-user/<int:user_id>", methods=["POST"])
def update_user(user_id):
    name = request.form.get("name")
    email = request.form.get("email")

    for user in users:
        if user["id"] == user_id:
            user["name"] = name
            user["email"] = email

    return jsonify(status="success")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
