from flask import Flask, render_template, request, jsonify, Response
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['GET'])
def fetch_insta():
    insta_url = request.args.get('url')
    api_key = "YDAIoYzubTQCsxlG"
    if not insta_url:
        return jsonify({"status": "error", "message": "No URL"}), 400
    
    target_api = f"https://teamexe-api-insta-loader.vercel.app/insta?url={insta_url}&key={api_key}"
    try:
        response = requests.get(target_api, timeout=10)
        return jsonify(response.json())
    except:
        return jsonify({"status": "error"}), 500

# Force Download Logic
@app.route('/download_proxy')
def download_proxy():
    file_url = request.args.get('url')
    file_name = request.args.get('name', 'file')
    
    r = requests.get(file_url, stream=True)
    headers = dict(r.headers)
    headers['Content-Disposition'] = f'attachment; filename={file_name}'
    
    return Response(r.content, headers=headers)

app = app
