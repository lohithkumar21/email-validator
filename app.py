from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='templates')

API_KEY = 'c9dc6bef11b1488ebb75fe03c2cf701e'

@app.route('/')
def index():
    return render_template('index.html', result=None)

@app.route('/validate-email', methods=['POST'])
def validate_email():
    email = request.form['email']
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={API_KEY}&email={email}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return render_template('index.html', result=data)
    else:
        return render_template('index.html', result={'error': 'Failed to validate email address'})

if __name__ == '__main__':
    app.run(debug=True)
