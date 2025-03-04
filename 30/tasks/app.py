from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/paieska', methods=['GET'])
def paieska():
    query = request.args.get('query', '')
    return render_template('forma_get.html', query=query)


@app.route('/prisijungti', methods=['GET', 'POST'])
def prisijungti():
    if request.method == 'POST':
        username = request.form.get('username')
        return f'Prisijungete kaip {username}'
    return render_template('forma_post.html')


@app.route('/registracija', methods=['GET', 'POST'])
def registracija():
    error = None
    success = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        if not username or not password or not password2:
            error = 'Klaida, visi laukai turi buti uzpildyti!'
        elif password != password2:
            error = 'Klaida, slaptazodziai nesutampa!'
        elif len(password) < 6:
            error = 'Klaida, slaptazdis turi buti is bent 6 simboliu.'
        else:
            success = 'Uzsiregistravote sekmingai!'

    return render_template('forma_registracija.html', error=error, success=success)


app.run()