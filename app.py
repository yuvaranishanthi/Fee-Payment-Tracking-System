from flask import Flask, render_template
from routes.auth import auth
from routes.booking import booking

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(booking)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)