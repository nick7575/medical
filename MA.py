from flask import Flask
app = Flask(__name__)

from flask import render_template
@app.route('/123')
def hello():
    return render_template('MA.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5004)