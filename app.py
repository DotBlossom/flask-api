from flask import Flask
from flask_cors import CORS

from image import upload_bp
from predict import predict_bp

from google.cloud import storage
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # bucket Connections
   KEY_PATH = os.environ.get('GOOGLE_APPLICATION_PATH')
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = KEY_PATH



    
   storage_client = storage.Client()
   buckets = list(storage_client.list_buckets())
   print(buckets)

   return 'hello'

app.register_blueprint(upload_bp)
app.register_blueprint(predict_bp)

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)