import sqlite3

from flask import Flask
import os


application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev')

if ENV == 'dev':
    pass
    # ustawienia dla wersji developerskiej
else:
    pass
    # ustawienia dla wersji produkcyjnej


def init_db():
    conn = sqlite3.connect('tasks.sqlite')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )
    ''')
    conn.commit()
    conn.close()

init_db()




@application.route('/')
def hello_world():
    return ('<h1>Witaj, BigData z Pythonem!</h1><p>Przykład CI/CD - automatyczne wdrożenie!</p><p>Bartosz Bryniarski</p>'
            f'<p>Środowisko: <b>{ENV}</b></p>')


if __name__ == '__main__':
    application.run(debug=True)