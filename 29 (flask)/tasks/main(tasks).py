from flask import Flask

app = Flask(__name__)

#                                                               1 task

@app.route('/')
def home():
    return 'Sveiki atvykte i Flask aplikacija!' \
            '<p> <a href=/pagrindinis> Pagrindinis </p>'

@app.route('/apie')
def apie():
    return 'Tai yra apie mus puslapis' \
           '<p><a href="/">Home</p>'

@app.route('/vartotojas/<vardas>')
def greeting(vardas):
    return f'Sveiki, {vardas}!' \
           '<p><a href="/">Home</p>'

@app.route('/skaicius/<int:nr>')
def number(nr):
    return f'Jus ivedete skaiciu: {nr}' \
           '<p><a href="/">Home</p>'

@app.route('/kelione/<start>/<end>')
def trip_route(start, end):
    return f'Keliones marsrutas is {start} i {end}'


# ===========================================================================================

#                                               task 2


@app.route('/pagrindinis')
def main():
    return '<h1>Mano Flask puslapis</h1>' \
           '<p>Tai yra pagrindinis puslapis</p>' \
           '<p><a href="/apie">Apie</p>' \
           '<p><a href="/">Home</p>'


if __name__ == '__main__':
    app.run()




