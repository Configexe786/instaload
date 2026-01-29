from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Isse browser error khatam ho jayega

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['GET'])
def fetch_insta():
    insta_url = request.args.get('url')
    api_key = "YDAIoYzubTQCsxlG"
    
    if not insta_url:
        return jsonify({"status": "error", "message": "No URL provided"}), 400

    # Aapki original API call
    target_api = f"https://teamexe-api-insta-loader.vercel.app/insta?url={insta_url}&key={api_key}"
    
    try:
        response = requests.get(target_api)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
