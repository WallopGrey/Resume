import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Разрешаем кросс-доменные запросы

DB_PATH = 'views.db'

def init_db():
    """Создает таблицу для хранения счетчика, если ее нет"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            views_count INTEGER DEFAULT 0
        )
    ''')
    # Инициализируем начальную запись
    cursor.execute('INSERT OR IGNORE INTO stats (id, views_count) VALUES (1, 0)')
    conn.commit()
    conn.close()

@app.route('/views', methods=['GET'])
def get_views():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Увеличиваем счетчик просмотров на 1
    cursor.execute('UPDATE stats SET views_count = views_count + 1 WHERE id = 1')
    conn.commit()

    # Получаем актуальное значение
    cursor.execute('SELECT views_count FROM stats WHERE id = 1')
    views = cursor.fetchone()[0]

    conn.close()
    return jsonify({"views": views})

if __name__ == '__main__':
    init_db()
    # Запуск только локально на порту 8000
    app.run(host='0.0.0.0', port=8000)
