from flask import Flask, jsonify, request
from Services.operations_service import reduce_operation

app = Flask(__name__, instance_relative_config=True)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello world!")

@app.route('/toupper', methods=['POST'])
def to_upper():
    data = request.get_json()
    message = data.get('message', '')
    return jsonify(message=message.upper())

@app.route('/tolower', methods=['POST'])
def to_lower():
    data = request.get_json()
    message = data.get('message','')
    return jsonify(message=message.lower())

@app.route("/concat", methods=['POST'])
def concat():
    data = request.get_json()
    message1 = data.get('message1','')
    message2 = data.get('message2','')
    return jsonify(message=message1+message2)

@app.route("/reduce", methods=['POST'])
def reduce():
    data = request.get_json()

    print(f"Data: {data}")
    operator = data.get('operator')
    listString = data.get('list')
    result, message = reduce_operation(listString, operator)
    if result is None:
        return jsonify(error=message), 400
    
    return jsonify(result=result)

def get_app():
    return app