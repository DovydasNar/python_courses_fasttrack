from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///organizacija.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Darboviete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String(50), nullable=False)
    miestas = db.Column(db.String(50), nullable=False)
    darbuotojai = db.relationship('Darbuotojas', backref='darboviete', lazy=True)

    @property
    def darbuotoju_skaicius(self):
        return len(self.darbuotojai)


class Darbuotojas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(50), nullable=False)
    pavarde = db.Column(db.String(50), nullable=False)
    pareigos = db.Column(db.String(50), nullable=False)
    darboviete_id = db.Column(db.Integer, db.ForeignKey('darboviete.id'), nullable=False)

@app.route('/', methods=['GET'], endpoint='index')
def rodyti_darbovietes():
    darbovietes = Darboviete.query.all()
    klaida = request.args.get('klaida')
    return render_template('index.html', darbovietes=darbovietes, klaida=klaida)

@app.route('/darboviete/<int:id>', methods=['GET'])
def rodyti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)
    return render_template('darboviete.html', darboviete=darboviete)

@app.route('/prideti-darboviete', methods=['POST', 'GET'])
def prideti_darboviete():
    if request.method == 'POST':
        pavadinimas = request.form['pavadinimas']
        miestas = request.form['miestas']
        nauja_darboviete = Darboviete(pavadinimas=pavadinimas, miestas=miestas)
        db.session.add(nauja_darboviete)
        db.session.commit()
        return redirect('/')
    return render_template('prideti-darboviete.html')

@app.route('/redaguoti_darboviete/<int:id>', methods=['POST', 'GET'])
def redaguoti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)
    if request.method == 'POST':
        darboviete.pavadinimas = request.form['pavadinimas']
        darboviete.miestas = request.form['miestas']
        darboviete.darbuotoju_skaicius = request.form['darbuotoju_skaicius']
        db.session.commit()

        return redirect('/')
    return render_template('redaguoti-darboviete.html', darboviete=darboviete)

@app.route('/trinti_darboviete/<int:id>', methods=['POST', 'GET'])
def trinti_darboviete(id):
    darboviete = Darboviete.query.get_or_404(id)
    if darboviete.darbuotojai:
        return redirect(url_for('index', klaida='Negalite istrinti darbovietes, nes joje yra darbuotoju.'))
    db.session.delete(darboviete)
    db.session.commit()
    return redirect('/')

@app.route('/darbuotojai', methods=['GET'])
def darbuotojai():
    darbuotojai = Darbuotojas.query.all()
    return render_template('darbuotojai.html', darbuotojai=darbuotojai)



@app.route('/prideti-darbuotoja', methods=['POST', 'GET'])
def prideti_darbuotoja():
    if request.method == 'POST':
        darboviete_id = request.form['darboviete_id']
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        pareigos = request.form['pareigos']

        naujas_darbuotojas = Darbuotojas(darboviete_id=darboviete_id, vardas=vardas, pavarde=pavarde, pareigos=pareigos)

        db.session.add(naujas_darbuotojas)
        db.session.commit()

        return redirect('/prideti-darbuotoja')

    darbovietes = Darboviete.query.all()
    return render_template('prideti-darbuotoja.html', darbovietes=darbovietes)

@app.route('/redaguoti-darbuotoja/<int:id>', methods=['GET', 'POST'])
def redaguoti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)
    darbovietes = Darboviete.query.all()
    if request.method == 'POST':
        darbuotojas.darboviete_id = request.form['darboviete_id']
        darbuotojas.vardas = request.form['vardas']
        darbuotojas.pavarde = request.form['pavarde']
        darbuotojas.pareigos = request.form['pareigos']

        db.session.commit()
        return redirect('/darbuotojai')

    return render_template('redaguoti-darbuotoja.html', darbuotojas=darbuotojas, darbovietes=darbovietes)


@app.route('/trinti_darbuotoja/<int:id>', methods=['POST', 'GET'])
def trinti_darbuotoja(id):
    darbuotojas = Darbuotojas.query.get_or_404(id)
    db.session.delete(darbuotojas)
    db.session.commit()
    return redirect('/darbuotojai')








if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5002)

