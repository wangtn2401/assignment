from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Address of API Express
API_EXPRESS_URL = "http://api-express:3000"

@app.route("/<path:path>", methods=["GET"])
def get_users(path):
    url = f"{API_EXPRESS_URL}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        data=request.data,
        headers=request.headers,
        params=request.args
    )
    return (response.text, response.status_code, response.headers.items())

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    # Search ID
    user_url = f"{API_EXPRESS_URL}/users/{user_id}"
    response = requests.get(user_url)
    return (response.text, response.status_code, response.headers.items())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
