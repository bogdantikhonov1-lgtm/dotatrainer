import random
from flask import render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import get_db, get_user_stats
from data import SCENARIOS

def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        if not username or not password:
            return render_template('register.html', error="Заполните все поля")
        db = get_db()
        existing = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
        if existing:
            return render_template('register.html', error="Пользователь уже существует")
        hashed = generate_password_hash(password)
        db.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', (username, hashed))
        db.commit()
        user = db.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
        session['user_id'] = user['id']
        session['username'] = username
        session['score'] = 0
        session['total'] = 0
        return redirect(url_for('index'))
    return render_template('register.html', error=None)

def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = username
            stats = get_user_stats(user['id'])
            session['score'] = stats['correct_attempts']
            session['total'] = stats['total_attempts']
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error="Неверное имя пользователя или пароль")
    return render_template('login.html', error=None)

def logout():
    session.clear()
    return redirect(url_for('index'))

def index():
    if 'user_id' not in session:
        return render_template('index.html', scenario=None, selected=None, stats=None, show_form=False)
    user_id = session['user_id']
    stats = get_user_stats(user_id)
    if 'scenario_id' not in session:
        return redirect(url_for('new_scenario'))
    scenario = SCENARIOS[session['scenario_id']]
    selected = session.get('selected_hero', None)
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice and not selected:
            session['selected_hero'] = choice
            session['total'] = session.get('total', 0) + 1
            if choice == scenario['correct']:
                session['score'] = session.get('score', 0) + 1
            db = get_db()
            db.execute('UPDATE stats SET total_attempts = ?, correct_attempts = ? WHERE user_id = ?',
                       (session['total'], session['score'], user_id))
            db.commit()
            return redirect(url_for('index'))
    return render_template('index.html', scenario=scenario, selected=selected, stats=stats, show_form=False)

def new_scenario():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    session['scenario_id'] = random.randrange(len(SCENARIOS))
    session.pop('selected_hero', None)
    return redirect(url_for('index'))

def reset_score():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    session['score'] = 0
    session['total'] = 0
    user_id = session['user_id']
    db = get_db()
    db.execute('UPDATE stats SET total_attempts = 0, correct_attempts = 0 WHERE user_id = ?', (user_id,))
    db.commit()
    session.pop('scenario_id', None)
    session.pop('selected_hero', None)
    return redirect(url_for('index'))
