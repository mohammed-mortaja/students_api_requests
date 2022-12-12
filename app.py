import json

import requests
from flask import Flask, render_template

def get_all_students():
    res = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    res_json = res.json()
    res_code = res_json['code']
    res_data = res_json['data']

    print(res.json())

    if res_code == 200:
        print('Get ALL Students Successfully ')
        return res_data
    else:
        print('ERROR Getting All Students')
        return False



app = Flask(__name__)
@app.route("/")
def home():
    all_data = get_all_students()
    print(all_data)
    context = {
        "title": "Students",
        'students': all_data
    }
    return render_template("temp.html", **context)


if __name__ == "__main__":
    app.run(debug=True)