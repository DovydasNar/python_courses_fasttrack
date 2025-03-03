from flask import Flask, render_template

app = Flask(__name__)

#                                                               1 task

# @app.route('/')
# def home():
#     return 'Sveiki atvykte i Flask aplikacija!' \
#             '<p> <a href=/pagrindinis> Pagrindinis </p>'
#
# @app.route('/apie')
# def apie():
#     return 'Tai yra apie mus puslapis' \
#            '<p><a href="/">Home</p>'
#
# @app.route('/vartotojas/<vardas>')
# def greeting(vardas):
#     return f'Sveiki, {vardas}!' \
#            '<p><a href="/">Home</p>'
#
# @app.route('/skaicius/<int:nr>')
# def number(nr):
#     return f'Jus ivedete skaiciu: {nr}' \
#            '<p><a href="/">Home</p>'
#
# @app.route('/kelione/<start>/<end>')
# def trip_route(start, end):
#     return f'Keliones marsrutas is {start} i {end}'
#
#
# # ===========================================================================================
#
# #                                               task 2
#
#
# @app.route('/pagrindinis')
# def main():
#     return '<h1>Mano Flask puslapis</h1>' \
#            '<p>Tai yra pagrindinis puslapis</p>' \
#            '<p><a href="/apie">Apie</p>' \
#            '<p><a href="/">Home</p>' \
#            '<p><a href="/vartotojas/Dovydas">Vartotojo puslapis</p>' \
#            '<p><a href="/skaicius/100">Skaiciaus puslapis</p>'

# # ===========================================================================================

#                                       task 3


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vartotojai')
def users():
    users_list = ['Dovydas', 'Paulius', 'Jonas', 'Petras', 'Antanas', 'Algirdas']
    return render_template('vartotojai.html', users_for_template=users_list)

# # ===========================================================================================


if __name__ == '__main__':
    app.run()




