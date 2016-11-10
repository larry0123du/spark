from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Drh66939224!@localhost/spark'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(30), unique=False)
	lastname = db.Column(db.String(30), unique=False)
	major = db.Column(db.String(20), unique=False)
	year = db.Column(db.String(10), unique=False)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, firstname, lastname, major, year, email):
		self.firstname = firstname
		self.lastname = lastname
		self.major = major
		self.year = year
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.email

		
@app.route('/')
def index():
	return render_template('spark.html')

@app.route('/registration/2016')
def register():
	return render_template('registration.html')

@app.route('/done', methods=['POST'])
def done():
	if request.method == 'POST':
		firstname = request.form['first']
		lastname = request.form['last']
		major = request.form['major']
		year = request.form['year']
		email = request.form['email']
		user = User(firstname, lastname, major, year, email)
		db.session.add(user)
		db.session.commit()
		return render_template('done.html', firstname = firstname)


if __name__ == '__main__':
	app.run(debug=True)
