from flask import Flask, render_template, request, redirect, url_for, flash

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restoranas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

db = SQLAlchemy(app)


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    num_of_seats = db.Column(db.Integer, nullable=False)
    orders = db.relationship('Order', backref='table', cascade='all, delete-orphan')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=False)



@app.route('/')
def home():
    tables = Table.query.all()
    return render_template('index.html', tables=tables)


@app.route('/table/<int:id>')
def view_tables(id):
    table = Table.query.get_or_404(id)
    return render_template('staliukas.html', table=table)

@app.route('/add-table', methods=['POST'])
def add_table():
    number = request.form['number']
    num_of_seats = request.form['num_of_seats']
    new_table = Table(number=number, num_of_seats=num_of_seats)
    db.session.add(new_table)
    db.session.commit()
    flash('Staliukas pridetas!', 'success')
    return redirect('/')

@app.route('/add-order/<int:table_id>', methods=['POST'])
def add_order(table_id):
    description = request.form['order_description']
    price = request.form['price']
    try:
        price = float(price)
    except ValueError:
        flash('Netinkama kaina!', 'danger')
        return redirect(f'/staliukas/{table_id}')
    new_order = Order(order_description=description, price=price, table_id=table_id)
    db.session.add(new_order)
    db.session.commit()
    flash('Uzsakymas atliktas!', 'success')
    return redirect(f'/table/{table_id}')

@app.route('/delete-table/<int:id>', methods=['POST'])
def delete_table(id):
    table = Table.query.get_or_404(id)
    if table.orders:
        flash('Negalite istrinti staliuko su uzsakymais!', 'danger')
    else:
        db.session.delete(table)
        db.session.commit()
        flash('Staliukas istrintas!', 'success')
    return redirect('/')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
