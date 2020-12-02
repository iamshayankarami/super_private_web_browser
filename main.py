import requests
from flask import Flask, request
import sys

url = sys.argv[1]

r = requests.get(url).text

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        input_p = {}
        Request = request.form
        print({I:Request[I] for I in Request if I != "submit"})
    return r

if __name__ == '__main__':
    app.run('0.0.0.0', port='7000')
