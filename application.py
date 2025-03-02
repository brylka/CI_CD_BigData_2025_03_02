from flask import Flask
import os


application = Flask(__name__)

ENV = os.environ.get('FLASK_ENV', 'dev')

@application.route('/')
def hello_world():
    if ENV == 'dev':
        return ('tadam')
    else:
        return ('<h1>Witaj, BigData z Pythonem!</h1><p>Przykład CI/CD - automatyczne wdrożenie!</p><p>Bartosz Bryniarski</p>'
                f'<p>Środowisko: <b>{ENV}</b></p>')


if __name__ == '__main__':
    application.run(debug=True)