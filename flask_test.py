from flask import Flask

import json

f = open('data.json')
data = json.load(f)

app = Flask(__name__)

@app.route("/<user_id>")
def home(user_id):
    output = "user_id: " + user_id + ', segment: ' + str(data[user_id])
    return output


if __name__ == "__main__":
    app.run(debug=True)