# import csv

# def load_referral_data():
#     referral_data = {}
#     with open('C:/Users/S M Rifat/Desktop/TestDev/alphaonlineclass/question_01/client.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader :
#             email = row['email'].strip()
#             referral_email = row['referral_email'].strip()
#             referral_data.setdefault(referral_email, []).append(email)
#     return referral_data

# def display_referral_relationships(main_referrer, referral_data, depth=0):
#     prefix = "    " * depth
#     print(f"{prefix}>>>> {main_referrer}")
#     referrals = referral_data.get(main_referrer, [])
#     for referral in referrals:
#         display_referral_relationships(referral, referral_data, depth + 1)

# def main():
#     referral_data = load_referral_data()
#     main_referrers = [email for email, referrals in referral_data.items() if not email in referral_data.values()]
#     for main_referrer in main_referrers:
#         display_referral_relationships(main_referrer, referral_data)

# if __name__ == "__main__":
#     main()
# import csv

# def load_referral_data():
#     referral_data = {}
#     with open('C:/Users/S M Rifat/Desktop/TestDev/alphaonlineclass/question_01/client.csv', newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             email = row['email'].strip().lower()
#             referral_email = row['referral_email'].strip().lower()
#             referral_data.setdefault(referral_email, []).append(email)
#     return referral_data

# def display_referral_chain(email, referral_data, depth=0):
#     prefix = "    " * depth
#     print(f"{prefix}>>>> {email}")
#     referrals = referral_data.get(email, [])
#     for referral in referrals:
#         display_referral_chain(referral, referral_data, depth + 1)

# def main():
#     referral_data = load_referral_data()
#     search_email = input("Enter the email address to search for: ").strip().lower()
#     if search_email in referral_data:
#         print("Referral Chain:")
#         display_referral_chain(search_email, referral_data)
#     else:
#         print("Email not found in referral data.")

# if __name__ == "__main__":
#     main()



import csv

def load_referral_data():
    referral_data = {}
    with open('C:/Users/S M Rifat/Desktop/TestDev/alphaonlineclass/question_01/client.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row['email'].strip()
            referral_email = row['referral_email'].strip()
            if referral_email:  # Check if referral email is not empty
                referral_data.setdefault(referral_email, []).append(email)
    return referral_data

def find_referral_chain(search_email, referral_data):
    if search_email in referral_data:
        print("Referral Chain:")
        display_referral_chain(search_email, referral_data)
        return True
    else:
        for referral_email, referrals in referral_data.items():
            if search_email in referrals:
                print("Referral Chain:")
                display_referral_chain(search_email, referral_data)
                return True
    return False

def display_referral_chain(email, referral_data, depth=0):
    prefix = "    " * depth
    print(f"{prefix}>>>> {email}")
    referrals = referral_data.get(email, [])
    for referral in referrals:
        display_referral_chain(referral, referral_data, depth + 1)

def main():
    referral_data = load_referral_data()
    print(referral_data)
    search_email = input("Enter the email address to search for: ").strip()
    if not find_referral_chain(search_email, referral_data):
        print("Email not found in referral data.")

if __name__ == "__main__":
    main()



from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# Function to read client data from CSV file
def read_client_data():
    clients = {}
    with open('client.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            client_email = row[0]
            referrer_email = row[1]
            if referrer_email not in clients:
                clients[referrer_email] = []
            clients[referrer_email].append(client_email)
    return clients

# Function to retrieve referral relationship for a given email
def get_referral_relationship(email, clients):
    relationship = []

    def traverse(email):
        if email in clients:
            for client in clients[email]:
                relationship.append(client)
                traverse(client)

    traverse(email)
    return relationship

# Route to display referral relationship
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        clients = read_client_data()
        referral_relationship = get_referral_relationship(email, clients)
        return render_template('index.html', email=email, referral_relationship=referral_relationship)
    return render_template('index.html', email=None, referral_relationship=None)

if __name__ == '__main__':
    app.run(debug=True)



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Referral Relationship</title>
</head>
<body>
    <h1>Referral Relationship</h1>
    <form method="POST">
        <label for="email">Enter Email:</label>
        <input type="email" id="email" name="email" required>
        <button type="submit">Submit</button>
    </form>
    {% if email %}
    <h2>Referral Relationship for {{ email }}:</h2>
    <ul>
        {% for referrer in referral_relationship %}
        <li>{{ referrer }}</li>
        {% endfor %}
    </ul>
    {% endif %}
</body>
</html>


from flask import Flask, render_template, request
import sqlite3
import csv

app = Flask(__name__)

# Function to create SQLite database and table
def create_database():
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clients
                 (client_email TEXT PRIMARY KEY, referral_email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert client data into the SQLite database
def insert_client_data(client_email, referral_email):
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute("INSERT INTO clients (client_email, referral_email) VALUES (?, ?)", (client_email, referral_email))
    conn.commit()
    conn.close()

# Function to read client data from a CSV file and insert into SQLite database
def insert_clients_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            client_email, referral_email = row
            insert_client_data(client_email, referral_email)

# Function to read client data from SQLite database
def read_client_data():
    clients = {}
    conn = sqlite3.connect('clients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clients")
    rows = c.fetchall()
    for row in rows:
        client_email = row[0]
        referral_email = row[1]
        if referral_email not in clients:
            clients[referral_email] = []
        clients[referral_email].append(client_email)
    conn.close()
    return clients

# Function to retrieve referral relationship for a given email
def get_referral_relationship(email, clients):
    relationship = []

    def traverse(email):
        if email in clients:
            for client in clients[email]:
                relationship.append(client)
                traverse(client)

    traverse(email)
    return relationship

# Route to display referral relationship
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        clients = read_client_data()
        referral_relationship = get_referral_relationship(email, clients)
        return render_template('index.html', email=email, referral_relationship=referral_relationship)
    return render_template('index.html', email=None, referral_relationship=None)

if __name__ == '__main__':
    create_database()
    insert_clients_from_csv('client.csv')
    app.run(debug=True)
