from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dummy_login", methods=["POST"])
def dummy_login():
    # Simulate capture of credentials (for demo only)
    username = request.form.get("user")
    password = request.form.get("pass")
    print(f"Simulated capture: {username} / {password}")
    return "✅ This was a phishing simulation. Do not enter real credentials."

if __name__ == "__main__":
    app.run(debug=True)
