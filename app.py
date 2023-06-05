from flask import jsonify,Flask,render_template, request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask_task'
 
mysql = MySQL(app)
 
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('users.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM login_table WHERE email=%s AND password=%s",(email,password))
        result = cursor.fetchone()
        cursor.close()
        if result:
            # Credentials are correct
            return jsonify({'valid': True})
        else:
            # Invalid credentials
            return jsonify({'valid': False})
        
 
app.run(host='localhost', port=5000)
