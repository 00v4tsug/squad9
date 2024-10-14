from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {'admin': 'password'}
crud_data = []
crud_data = {
    'nomes': [],
    'descricoes': [],
    'nomearquivos': []
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        username = request.form['id-gestor']
        password = request.form['senha']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials. Please try again.')
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST': 
        username = request.form['id-gestor']
        password = request.form['senha']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials. Please try again.')
    return render_template('login.html')

@app.route('/')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', crud_data=crud_data)
    else:
        return redirect(url_for('login'))

# Criar novo item
@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' in session:
        if request.method == 'POST':
            if 'file' not in request.files:
                return redirect(url_for('create'))
            nome = request.form['nome']
            descricao = request.form['descricao']
            file = request.files['file']
            if file.filename == '':
                return redirect(url_for('create'))
            if file:
                if name:
                    if descricao:
                        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                        file.save(file_path)
                        crud_data['nomes'].append(nome)
                        crud_data['descricoes'].append(descricao)
                        crud_data['nomearquivos'].append(file.filename)
                    else:
                        return redirect(url_for('create'))
                        flash('Campo Descriçao Campanha na consta.')
                else:
                    return redirect(url_for('create'))
                    flash('Campo Nome Campanha na consta.')
            else:
                return redirect(url_for('create'))
                flash('É preciso selecionar uma imagem.') 

        return render_template('create.html')
    else:
        return redirect(url_for('login'))

# Atualizar item
@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update(index):
    if 'user' in session:
        if request.method == 'POST':
            new_item = request.form['item']
            crud_data[index] = new_item
            return redirect(url_for('dashboard'))
        return render_template('update.html', item=crud_data[index], index=index)
    else:
        return redirect(url_for('login'))

# Deletar item
@app.route('/delete/<int:index>')
def delete(index):
    if 'user' in session:
        crud_data.pop(index)
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

@app.route('/campanhas')
def campanhas():
    if 'user' in session:
        if request.method == 'POST':
            item = request.form['item']
            crud_data.append(item)
            return redirect(url_for('dashboard'))
        return render_template('campanhas.html')
    else:
        return redirect(url_for('login'))

@app.route('/premiacoes')
def premiacoes():
    if 'user' in session:
        if request.method == 'POST':
            item = request.form['item']
            crud_data.append(item)
            return redirect(url_for('dashboard'))
        return render_template('premiacoes.html')
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
