from flask import (
    Flask,
    render_template,
    url_for,
    redirect,
    request,
    flash,
)

app = Flask(__name__)
app.secret_key = '262405'

@app.route('/')
def home():
    return render_template(
        'home.html',
        title = 'Homepage',
    )

@app.route('/projects')
def projects():
    return render_template(
        'projects.html',
        title = 'Projects',
    )

@app.route('/profile/<member>')
def profile(member):
    return f'this member identification is : {member}'

@app.route('/api')
def api():
    return render_template(
        'api.html',
        title = 'API',
    )

@app.route('/api/post-data', methods=['GET', 'POST'])
def post_data():
    if request.method == 'GET':
        return redirect(url_for('api'))
    else:
        temperature = float(request.form['temperature']) if request.form['temperature'] != '' else 0
        humidity = float(request.form['humidity']) if request.form['humidity'] != '' else 0
        return f'{temperature:.2f}\n{humidity:.2f}%'

@app.route('/admin')
def admin():
    flash('Admin page not ready')
    return redirect(url_for('home'))

app.run(
    host = '0.0.0.0',
    port = 5000,
    debug = True,
)