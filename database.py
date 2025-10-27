import sqlite3

def init_db():
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            condition TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
