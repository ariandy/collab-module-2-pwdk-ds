from flask import Flask, render_template
from cleaning_data import data_covid, top15
from plotting import bubble

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    data = data_covid()
    return render_template('table_data.html', data=data)

@app.route('/top15/<feature>')
def rank(feature):
    data = top15(feature)
    return render_template('top15.html', data=data)

@app.route('/plots/<feature>')
def plots(feature):
    data = bubble(feature, 'Viridis')
    return render_template('plots.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=6900)