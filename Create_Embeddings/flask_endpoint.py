from flask import Flask, jsonify, request, render_template
from query import *
app = Flask(__name__)


@app.route('/get_answer/<query>', methods= ['GET', 'POST'])
def answer(query):
    if(request.method == 'GET'):
        data = get_answer(query)
        return jsonify(data)
    
    if(request.method == 'POST'):
        data = get_answer(query)
        return jsonify(data)
 

@app.route('/',methods=['GET'])
def homepage():
    return jsonify({'data': "Hello World"})


# driver function
if __name__ == '__main__':
    app.run(debug = True)