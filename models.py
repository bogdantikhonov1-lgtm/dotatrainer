import sqlite3
from flask import g
from config import DATABASE

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS stats (
            user_id INTEGER PRIMARY KEY,
            total_attempts INTEGER DEFAULT 0,
            correct_attempts INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
    ''')
    db.commit()

def get_user_stats(user_id):
    db = get_db()
    stats = db.execute('SELECT * FROM stats WHERE user_id = ?', (user_id,)).fetchone()
    if stats is None:
        db.execute('INSERT INTO stats (user_id) VALUES (?)', (user_id,))
        db.commit()
        stats = db.execute('SELECT * FROM stats WHERE user_id = ?', (user_id,)).fetchone()
    return stats
