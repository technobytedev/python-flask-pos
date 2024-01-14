from flask import Flask
from flask import render_template

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', site_name="Online POS")

@app.route('/receipt')
def receipt():
    return render_template('receipt.html', site_name="Online POS")


