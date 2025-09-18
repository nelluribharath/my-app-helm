from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kubernetes! 🚀 Your app is running."

if __name__ == "__main__":
    # Run on 0.0.0.0 so it's accessible inside Docker/K8s
    app.run(host="0.0.0.0", port=5000)
