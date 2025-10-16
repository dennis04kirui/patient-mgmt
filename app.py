from flask import Flask, request, jsonify, render_template
from flask import Flask, request, jsonify

app = Flask(__name__)

patients = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/patients', methods=['GET'])
def get_patients():
    return jsonify(patients)

@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    patients.append(data)
    return jsonify({"message": "Patient added successfully!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
