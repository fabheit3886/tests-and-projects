from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
# ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('index'))
    # ...