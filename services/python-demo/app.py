from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Python Demo Service</h1>
    <p>This is running on a persistent backend!</p>
    """

@app.route('/api/status')
def status():
    return jsonify({"status": "running", "service": "python-demo"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
