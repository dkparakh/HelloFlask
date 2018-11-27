from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(

    SECRET_KEY='Dhriti@0506',
    SQLALCHEMY_DATABASE_URI='postgres://postgres:Dhriti@0506@localhost/catalog_db',
    SQLAlCHEMY_TRACK_MODIFICATIONS=False
)

db: SQLAlchemy = SQLAlchemy(app)

# BASIC ROUTE

@app.route('/index')
@app.route('/')

def hello_flask():
    return 'Hello Flask!'


@app.route('/new/')
def query_strings(greeting='Customer'):
    query_val = request.args.get('greeting',greeting)
    return '<h1> Welcome to Indian Grocery Stores, {0}!!! </h1>'.format(query_val)

@app.route('/user')
@app.route('/user/<name>')
def no_query_strings(name='New Customer'):
    return '<h1> Welcome to Indian Grocery Stores, {0}!!! </h1>'.format(name)

@app.route('/text/<string:name>')
def working_with_strings(name):
    return '<h1> Welcome to Indian Grocery Stores, {0}!!! </h1>'.format(name)


@app.route('/numbers/<int:num>')
def working_with_numbers(num):
    return '<h1> Welcome to Indian Grocery Stores, {0}!!! </h1>'.format(num)

@app.route('/add/<int:num1>/<int:num2>')
def adding_numbers(num1,num2):
    return '<h1> Welcome to Indian Grocery Stores, {0}!!! </h1>'.format(num1+num2)

@app.route('/Product/<float:num1>/<float:num2>')
def product_numbers(num1,num2):
    return '<h1> Welcome to Indian Grocery Stores, {0}!!! </h1>'.format(num1*num2)

@app.route('/temp')
def using_templates():
    return render_template('hello.html')

@app.route('/watch')
def movies_2017():
    movie_list = ['Jolly LLB 2','Raees', 'Hindi Medium', 'Toilet', 'Golmaal Again', 'Sarkar 3']
    return render_template('Movies.html',movies=movie_list,name='Parakh1')

@app.route('/tables')
def movies_plus():
    movie_dict = {'Jolly LLB 2': 10.00,
                  'Raees': 9.45,
                  'Hindi Medium': 10.25,
                  'Toilet': 9.00,
                  'Golmaal Again': 11.00,
                  'Sarkar 3': 9.11}
    return render_template('table_data.html',movies=movie_dict,name='Parakh2')

@app.route('/macros')
def jinja_macros():
    movie_dict = {'Jolly LLB 2': 10.00,
                  'Raees': 9.45,
                  'Hindi Medium': 10.25,
                  'Toilet': 9.00,
                  'Golmaal Again': 11.00,
                  'Sarkar 3': 9.11}
    return render_template('using_macros.html',movies=movie_dict)

@app.route('/filters')
def filter_data():
    movie_dict = {'Jolly LLB 2': 10.00,
                  'Raees': 9.45,
                  'Hindi medium': 10.25,
                  'Toilet': 9.00,
                  'Golmaal again': 11.00,
                  'Sarkar 3': 9.11}
    return render_template('filter_data.html',movies=movie_dict,name=None,film='Dhriti Parakh')

class Publication(db.Model):

    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'This id is {}, Name is {}'.format(self.id, self.name)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)