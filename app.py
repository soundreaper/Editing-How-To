from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    """Index page of the application"""
    return render_template('main.html', page="index")


@app.route('/sony_vegas')
def sony_vegas():
    """Page for editing tutorials using Sony Vegas"""
    return render_template('main.html', page="sony_vegas")

@app.route('/adobe')
def adobe():
    """Page for editing tutorials using Adobe Software"""
    return render_template('main.html', page="adobe")

if __name__ == '__main__':
    app.run(debug=True)