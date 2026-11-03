from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "project": "The-Creators",
        "status": "scaffolded",
        "message": "Backend is ready for route and database integration."
    })


if __name__ == "__main__":
    app.run(debug=True)
