from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Address of API Express
API_EXPRESS_URL = "http://api-express:3000"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    url = f"{API_EXPRESS_URL}/{path}"
    response = requests.request(
        method=request.method,
        url=url,
        data=request.data,
        headers=request.headers
    )
    return (response.text, response.status_code, response.headers.items())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
