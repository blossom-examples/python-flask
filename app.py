from datetime import datetime
import os
from flask import Flask, request, jsonify, render_template

# Disable ANSI colors in output
os.environ['FLASK_NO_COLOR'] = '1'
os.environ['PYTHONUNBUFFERED'] = '1'

# Set Flask's own env vars
if 'PORT' in os.environ:
    os.environ['FLASK_RUN_PORT'] = os.environ['PORT']
os.environ['FLASK_RUN_HOST'] = '0.0.0.0'

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)