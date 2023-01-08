from flask_app import app, mongo
from flask import render_template, request, flash, redirect, url_for

@app.route('/')
def home():
    return redirect(url_for('insert_page'))


@app.route('/insert', methods=['POST', 'GET'])
def insert_page():
    if request.method == 'POST':
        try:
            name = request.form.get('name').lstrip().rstrip()
            age = int(request.form.get('age'))
            mongo.db.users.insert_one({'name': name, 'age': age})
            flash('Value Entered Succesfully')
        except ValueError:
            flash('Value error! Enter correct values')
    return render_template('insert.html')


@app.route('/view', methods=['POST', 'GET'])
def view_page():
    documents = None
    if request.method == 'POST':
        temp_documents = list(mongo.db.users.find({}))
        documents = list()
        for temp_doc in temp_documents:
            name = temp_doc['name']
            age = temp_doc['age']
            documents.append([name, age])
        return render_template('view.html', documents=documents)
    return render_template('view.html', documents=documents)


@app.route('/view_by_query', methods=['POST', 'GET'])
def view_by_query_page():
    result = None
    if request.method == 'POST':
        name = request.form.get('name')
        res = mongo.db.users.find_one({'name': name})
        if res:
            result = res
        else:
            result = 'No Match Found'
    return render_template('view_by_query.html', result=result)