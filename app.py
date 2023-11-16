from flask import Flask, render_template

app = Flask(__name__)


@app.route('/sushi')
def sushi():  # put application's code here
    barca1 = 'Barca Individual'
    barca2 = 'Barca Casal'
    barca3 = 'Barca Daora'
    barca4 = 'Barca Grande'
    lista = [barca1, barca2, barca3, barca4]
    return render_template('Sushi.html', lista=lista)

@app.route('/note')
def note():
    Nota = 'Nova Anotação'
    return render_template('Note.html',Nota = Nota)


if __name__ == '__main__':
    app.run()
