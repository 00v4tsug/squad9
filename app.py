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

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

# Criar novo item
@app.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' in session:
        if request.method == 'POST':
            print(request.form)  # Imprime todos os dados do formulário
            print(request.files)
            nome = request.form['nome']
            descricao = request.form['descricao']
            file = request.files['file']
            
            if not nome or not descricao or not file:
                flash("Todos os campos são obrigatórios.")
            else:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
                file.save(file_path)
                crud_data['nomes'].append(nome)
                crud_data['descricoes'].append(descricao)
                crud_data['nomearquivos'].append(file.filename)
                print (crud_data)

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
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('campanhas.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
