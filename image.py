from flask import Blueprint, request, jsonify
from google.cloud import storage

from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드
google_secret_key = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS') 
bucket_name = os.environ.get('GOOGLE_BUCKET_NAME') 

upload_bp = Blueprint('upload', __name__)
send_predict_request_bp = Blueprint('predict', __name__)

# upload는 그냥 뭐 통채로 .. 해도 .. 일단은 단일 코드
@upload_bp.route('/flaskapi/upload/<long:receiptId>/<int:order>', methods=['POST'])
def upload_image(receiptId, order):
    if 'image' not in request.files:
        return jsonify({'description': 'No image file provided'}), 400

    #Type: blob(form_data)
    image_file = request.files['image']
    
    
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    
    blob = bucket.blob(image_file.filename)
    blob.upload_from_file(image_file)
    
    uploaded_image_url = f"https://storage.googleapis.com/{bucket_name}/{image_file.filename}"

    # task validations 
    

    # image_uploaded.send(image, receiptId=receiptId, imageUrl=uploaded_image_url, order=order)

    return jsonify({'imageUrl': uploaded_image_url}), 200


# 버튼 하나 더 만들자.. 최종 보내기 .. 재 업로드 or 나머지만 보내기 .. 
# 된다면 로딩 ㄱㄱ 


'''
# signal 처리, 복잡도 감소
image_uploaded = signal('image-uploaded')

@image_uploaded.connect
def send_predict_request(sender, **kwargs):
    receiptId = kwargs['receiptId']
    image_url = kwargs['imageUrl']
    order = kwargs['order']  # 필요에 따라 order 값 설정

    # 다른 Flask 서버로 요청 보내기
    response = requests.post(f'http://localhost:5333/gpu/predict/{receiptId}/{order}', json={'imageUrl': image_url})


    return response.json(), response.status_code
'''