from datetime import datetime
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    name = request.args.get('name', 'World')
    return jsonify({
        'message': f'Hello, {name}!',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({
        'message': 'Echo response',
        'received': data,
        'timestamp': datetime.utcnow().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True)