from flask import render_template
from app import app

@app.route("/", methods=['GET', 'POST'])
def hello():
    name = 'Vlad'
    return render_template('hello.html', name=name)

@app.route('/product/id/<int:product_id>')
def product_info(product_id):
    pass