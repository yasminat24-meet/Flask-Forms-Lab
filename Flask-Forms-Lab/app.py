from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "yasmin"
password = "123"
facebook_friends=["sarah","saeed","ward", "George", "Fouad", "nada","waseem"]

@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		#return 'You just made a post request!'
		username2=request.form['username']
		password2=request.form['password']

		if username2==username and password2==password:
			return redirect(url_for('home_page'))
		else:
			return render_template('login.html')

	else:
		return render_template('login.html')

@app.route('/home')
def home_page():
	return render_template('home.html',p= facebook_friends)

@app.route('/friend_exists/<string:name>')
def friend(name):
		if name in facebook_friends:
			result=True
		else:
			result=False
		return render_template('friend_exists.html',name=name,result=result)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)