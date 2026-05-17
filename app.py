from flask import Flask
from config import SECRET_KEY
from models import close_connection, init_db
from views import (
    register, login, logout, index, new_scenario, reset_score
)

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Регистрируем маршруты через add_url_rule для наглядности
app.add_url_rule('/register', 'register', register, methods=['GET', 'POST'])
app.add_url_rule('/login', 'login', login, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout)
app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
app.add_url_rule('/new', 'new_scenario', new_scenario)
app.add_url_rule('/reset', 'reset_score', reset_score)

app.teardown_appcontext(close_connection)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    print("⚙️ Запуск Dota 2 Draft Trainer с регистрацией на http://127.0.0.1:5000")
    app.run(debug=True)
