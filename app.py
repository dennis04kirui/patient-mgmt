from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database import init_db

app = Flask(__name__)
init_db()

# Home Page
@app.route('/')
def home():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patients")
    patients = c.fetchall()
    conn.close()
    return render_template('index.html', patients=patients)

# Add Patient
@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form['name']
    age = request.form['age']
    condition = request.form['condition']

    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("INSERT INTO patients (name, age, condition) VALUES (?, ?, ?)", (name, age, condition))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

# Delete Patient
@app.route('/delete/<int:id>')
def delete_patient(id):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("DELETE FROM patients WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))
# Edit Patient
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        condition = request.form['condition']
        c.execute("UPDATE patients SET name=?, age=?, condition=? WHERE id=?", (name, age, condition, id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))

    else:
        c.execute("SELECT * FROM patients WHERE id=?", (id,))
        patient = c.fetchone()
        conn.close()
        return render_template('edit.html', patient=patient)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
