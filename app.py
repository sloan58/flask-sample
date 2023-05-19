from flask import Flask
from routes.palo import palo_blueprint


app = Flask(__name__)
app.register_blueprint(palo_blueprint, url_prefix='/palo')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
