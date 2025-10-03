from flask import Flask, jsonify, request

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
    data=request.get_json()
    message=data.get('message','')
    return jsonify(message=message.lower())

if __name__ == '__main__':
    app.run(debug=True)