from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mokiniai.db'
# app.config['SQLALCHEMY_TRACK_MODIFIACTIONS'] = False

db = SQLAlchemy(app)

class Mokiniai(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(50), nullable=False)
    pavarde = db.Column(db.String(50), nullable=False)
    klase = db.Column(db.Integer, nullable=False)
    sukurimo_data = db.Column(db.DateTime, default=datetime.utcnow())

    @property
    def sekanti_klase(self):
        return self.klase + 1

    def __repr__(self):
        return f'ID: {self.id}. Mokinys: {self.vardas} {self.pavarde}. Klase: {self.klase}'


@app.route('/', methods=['GET', 'POST'])
def rodyti_mokinius():
    search_query = request.args.get('search', '')
    if search_query:
        mokiniai = Mokiniai.query.filter(Mokiniai.vardas.like(f'%{search_query}%')).all()
    else:
        mokiniai = Mokiniai.query.all()
    return render_template('mokiniai.html', mokiniai=mokiniai, search_query=search_query)


@app.route('/prideti-mokini', methods=['GET', 'POST'])
def prideti_mokini():
    if request.method == 'POST':
        vardas = request.form['vardas']
        pavarde = request.form['pavarde']
        klase = request.form['klase']

        naujas_mokinys = Mokiniai(vardas=vardas, pavarde=pavarde,klase=klase)
        db.session.add(naujas_mokinys)
        db.session.commit()

        return redirect('/')
    return render_template('prideti-mokini.html')






if __name__ == '__main__':
    app.run(port=5001)


