from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        submitter = request.form.get('submitter')
        fact = request.form.get('fact')
       
        print(f"Submitter: {submitter}, Fact: {fact}")  
        return redirect(url_for('fact.new')) 
    return render_template('new_fact.html')
