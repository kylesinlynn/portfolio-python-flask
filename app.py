from flask import Flask, render_template

portfolio = Flask(__name__)

@portfolio.route('/')
@portfolio.route('/<url>')
def home(url=None):
	return render_template('home.html', title='Home')

@portfolio.route('/contact')
def contact():
	return render_template('contact.html', title='Contact')
