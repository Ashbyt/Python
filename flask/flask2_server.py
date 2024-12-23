from flask import Flask

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True)


# python3 -m venv venv
#source venv/bin/activate
#http://127.0.0.1:5000/hello
