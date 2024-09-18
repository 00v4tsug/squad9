from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {'admin': 'password'}
crud_data = []

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        username = request.form['id-gestor']
        password = request.form['senha']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials. Please try again.')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', crud_data=crud_data)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
