from flask import Flask, jsonify, request

app = Flask(__name__)


# ログ設定
@app.route('/api/secrets', methods=['POST'])
def secrets():
    data = request.json
    if not data or 'key' not in data:
        return jsonify({"error": "Invalid request"}), 400
    if data['key'] == 'my-secret-key':
        return jsonify({"secret": "my-secret-value"})
    return jsonify({"error": "Secret not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
