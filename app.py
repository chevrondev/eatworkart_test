from flask import Flask, render_template, redirect, url_for, request, session, flash, g 
from functools import wraps
import sqlite3

app = Flask(__name__)

# the secret_key stops the session being accessed client side  and it is needed for the session to work
app.secret_key='mysecretkey'
app.database = "eatworkart.db"



# login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash("You need to login first!")
			return redirect(url_for('login'))
	return wrap
# use decorator to link the function to a url
@app.route('/')
@login_required
def home():
	g.db=connect_db()
	cur=g.db.execute('select * from authors')
	authors=[dict(fname=row[0], lname=row[1], description=row[2]) for row in cur.fetchall()]
	g.db.close()
	# renders a template
	return render_template('index.html', authors=authors)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")
	
# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'tom' or request.form['password'] != 'eatworkart':
            error = 'Invalid Credentials. Please try again.'
        else:
			session['logged_in'] = True
			flash('You are logged in!')
        return redirect(url_for('home'))
    return render_template('login.html', error=error)
	
	
# route for handling the logout page logic
@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You are logged out!')
	return redirect(url_for('welcome'))	
	
def connect_db():
	return sqlite3.connect(app.database)


if __name__ == '__main__':
    app.run(debug=True)