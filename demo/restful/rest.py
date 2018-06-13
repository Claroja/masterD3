from flask import json
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('rest.html')


@app.route('/index', methods=['GET','POST'])
def get_current_user():
    print(request.json)
    data=eval(request.json['data'])
    # return jsonify(username=data)
    return json.dumps({"username":data})


if __name__ == '__main__':
    app.run(debug=True)