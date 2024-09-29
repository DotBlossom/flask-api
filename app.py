from flask import Flask
from flask_cors import CORS

from image import upload_bp
from predict import predict_bp


app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
   return 'This is Home!'


app.register_blueprint(upload_bp)
app.register_blueprint(predict_bp)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)