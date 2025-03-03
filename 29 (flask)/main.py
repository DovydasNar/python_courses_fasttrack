
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vardai')
def vardai():
    names = ['Dovydas', 'Petras', 'Paulius', 'Antanas', 'Lebronas', 'Kobe']
    return render_template('vardai.html', names_for_template= names)

if __name__ == '__main__':
    app.run()

