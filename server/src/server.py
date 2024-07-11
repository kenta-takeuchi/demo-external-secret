from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# ログ設定
logging.basicConfig(level=logging.DEBUG)

@app.route('/api/secrets', methods=['POST'])
def secrets():
    data = request.json
    app.logger.debug('Received data test: %s', data)
    if not data or 'key' not in data:
        return jsonify({"error": "Invalid request"}), 400
    if data['key'] == 'my-secret-key':
        app.logger.debug(f"return value by key: {data['key']}")
        return jsonify({"secret": "my-secret-value"})
    return jsonify({"error": "Secret not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
