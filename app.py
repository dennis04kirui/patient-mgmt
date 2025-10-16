from flask import Flask, render_template, request, jsonify

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
    patients.append({
        "id": len(patients) + 1,
        "name": data['name'],
        "age": data['age'],
        "condition": data['condition']
    })
    return jsonify({"message": "Patient added successfully!"}), 201

@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    global patients
    patients = [p for p in patients if p['id'] != id]
    return jsonify({"message": "Patient deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
