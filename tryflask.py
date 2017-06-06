from flask import Flask
from flask import render_template

app = Flask(__name__)

all_people = {
    1:{'id': 1, 'name': 'Richard', 'age': 43},
    2:{'id': 2, 'name': 'Tom', 'age': 23},
    3:{'id': 3, 'name': 'Mary', 'age': 34},
    4:{'id': 4, 'name': 'John', 'age': 51},
    7:{'id': 7, 'name': 'Ann', 'age': 65}
}




@app.route('/')
def hello_world():
     return render_template('index.html')

@app.route('/people')
def show_people():
    return render_template('people.html', people=all_people.values())

@app.route('/person/<int:id>')
def show_person(id):
    p = all_people[id]
    return render_template('person.html', fruitbat=p)



if __name__ == '__main__':
    app.run(debug=True)
