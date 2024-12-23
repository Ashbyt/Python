from flask import Flask
import json
from flask import Flask, render_template, redirect, url_for, request 


app = Flask(__name__)

next_id = 5


contacts = [
{ 'id': '1', 'name': 'Shaun', 'phone': '123443234343' },
{ 'id': '2', 'name': 'Bob', 'phone': '12344343432323' },
{ 'id': '3', 'name': 'John', 'phone': '12344366343' } ,
{ 'id': '4', 'name': 'Tony', 'phone': '1234434354343' },

]

@app.route('/hello')
def hello_route():
    print('I have received a request on the /hello endpoint!')
    return '<h1>Hello from the server!</h1>'

@app.get('/contacts')
def list_contacts():
    return contacts

@app.get('/contacts/<id>')
def read_single_contact(id):
        for contact in contacts:
            if contact['id'] == id: 
                return contact
        return 'that contact does not exist!'

@app.post('/contacts')
def create_contact():
    global next_id
    new_contact = {
        'id':f'{next_id}',
        'name': request.json['name'],
        'phone': request.json['phone'],

    }

    contacts.append(new_contact)

    next_id += 1
    return new_contact

#    print(request.json)
#    return 'thankyou for the data!'

@app.put('/contacts/<id>')
def update_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            contact['name'] = request.json['name'] if 'name' in request.json else contact['name']
            contact['phone'] = request.json['phone'] if 'phone' in request.json else contact['phone']
            return contact
    return 'there is no data here'

