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
        _list = 'main_list'
        global service_manager
        service_manager = ServiceManager(_api_key, _username)
        l = service_manager.get_list(_list)
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


@app.route("/delete_subscriber/<email>", methods=['DELETE'])
def delete_subscriber(email):
    _email = email
    service_manager.delete_subscriber(_list, _email)
    return json.dumps({'html': '<span>User Deleted</span>'})


@app.route("/add_subscriber/", methods=['PUT'])
def add_subscriber():
    _name = request.form['inputName']
    _email = request.form['inputMail']
    service_manager.add_subscriber(_list, _email, _name)
    return json.dumps({'html': '<span>User Added</span>'})


if __name__ == "__main__":
    app.run()
