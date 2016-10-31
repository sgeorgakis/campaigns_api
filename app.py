from flask import Flask, render_template, request, redirect, url_for, json
from ServiceManager import *

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html.jnj2')

@app.route("/subscribers/", methods=['POST'])
def interact():
    try:
    	_api_key = request.form['inputApiKey']
    	_username = request.form['inputUsername']
    	global _list
    	_list = request.form['inputList']
    	global service_manager
    	service_manager = ServiceManager('35e30789cd6c5e86fe4b2ee9c9951107', 'Stefanos Georgakis')
    	l = service_manager.get_list('main_list')
    	#service_manager = ServiceManager(_api_key, _username)
    	#l = service_manager.get_list(_list)
    	return render_template(
    		'active_subscribers.html.jnj2',
    		subscribers=service_manager.get_active_subscribers(l)
    		)
    except (
    	NoClientFound,
    	NoListFound,
    	WrongAPI,
    	NotFound
    	) as e:
    	return render_template('error_page.html.jnj2', message=str(e))

"""
@app.route("/delete_subscriber/", methods=['DELETE'])
def delete_subscriber():
	#_email = request.form['inputUsername']
	#return _email
	#.args.get
	print request.args.get('inputUsername')
	print request.query_string
	return json.dumps({'html':'<span>' + request.query_string + '</span>'})
	#service_manager.delete_subscriber(_list, )
"""

@app.route("/add_subscriber/", methods=['PUT'])
def add_subscriber():
	_name = request.form['inputName']
	_email = request.form['inputMail']
	l = service_manager.get_list(_list)
	print _name + "\n" + _email
	service_manager.add_subscriber(l, _email, _name)
	return redirect(url_for(interact))

if __name__ == "__main__":
    app.run()
