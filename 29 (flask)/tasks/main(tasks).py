from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sveiki atvykte i Flask aplikacija!'

@app.route('/apie')
def apie():
    return 'Tai yra apie mus puslapis'

@app.route('/vartotojas/<vardas>')
def greeting(vardas):
    return f'Sveiki, {vardas}!'

@app.route('/skaicius/<int:nr>')
def number(nr):
    return f'Jus ivedete skaiciu: {nr}'

@app.route('/kelione/<start>/<end>')
def trip_route(start, end):
    return f'Keliones marsrutas is {start} i {end}'



if __name__ == '__main__':
    app.run()




