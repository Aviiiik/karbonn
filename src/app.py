from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from model import probe_model_5l_profit

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React


@app.route('/upload', methods=['POST'])
def upload_file():
    
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        data = json.load(file)
        raw_result = probe_model_5l_profit(data["data"])

        # Format the result to "rule_name: value" style
        formatted_result = "\n".join([f"{key}: {value}" for key, value in raw_result["flags"].items()])

        return jsonify({"result": formatted_result}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
