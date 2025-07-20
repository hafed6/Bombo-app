from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)
DATA_FILE = "data.json"

# إنشاء الملف إذا لم يكن موجودًا
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def home():
    return "Le serveur Flask fonctionne correctement !"

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    with open(DATA_FILE, 'r') as f:
        content = json.load(f)
    content.append(data)
    with open(DATA_FILE, 'w') as f:
        json.dump(content, f, indent=4)
    return jsonify({"message": "Données enregistrées avec succès", "data": data})

@app.route('/get', methods=['GET'])
def get_data():
    with open(DATA_FILE, 'r') as f:
        content = json.load(f)
    return jsonify(content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
