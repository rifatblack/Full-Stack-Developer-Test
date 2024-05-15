from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
db = SQLAlchemy(app)


class Client(db.Model):
    __tablename__ = 'clients'
    client_email = db.Column(db.String(120), primary_key=True)
    referral_email = db.Column(db.String(120))


def insert_clients_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            client_email, referral_email = row
            existing_client = Client.query.filter_by(client_email=client_email).first()
            if not existing_client:
                client = Client(client_email=client_email, referral_email=referral_email)
                db.session.add(client)
    db.session.commit()


def get_referral_relationship(email):
    relationship = []

    def traverse(email):
        clients = Client.query.filter_by(referral_email=email).all()
        for client in clients:
            relationship.append(client.client_email)
            traverse(client.client_email)

    traverse(email)
    return relationship


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        referral_relationship = get_referral_relationship(email)
        return render_template('index.html', email=email, referral_relationship=referral_relationship)
    return render_template('index.html', email=None, referral_relationship=None)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        insert_clients_from_csv('client.csv')
    app.run(debug=True)
