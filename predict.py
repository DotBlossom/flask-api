from flask import Blueprint, request

import requests

predict_bp = Blueprint('predict', __name__)

#ㄴㄴ
@predict_bp.route('/flaskapi/predict/<int:receiptId>/<int:order>', methods=['POST'])
def response_predict_request(receiptId, order):
    
    data = request.get_json()
    
    image_url = data['imageUrl']
    metadata = data['metadata']
    

    # 다른 Flask 서비스로 요청 전송, 여기서 localhost는 yaml에서 env로 정의한 변수로 대체
    # make_response로 res를 잘 만들어주자. 
    # res = make_response(json.dumps(res, ensure_ascii=False))
    response = requests.post(f'http://localhost:5333/ocr/predict/{receiptId}/{order}', json={'imageUrl': image_url, 'metadata': metadata})
    
    # if need to refine data? or save data? -> other port 
   
   
    # response에서 predict img가 오면, image에서 upload ㄱㄱ , 5333에서 img 호출..
    

    
    
    # DB alchemy? 
    
    
    
    # response 재조립
    
    
    # result return -> loading -> img + text 
    if response.ok:       
        return response, response.status_code
    
    else:
        return response.status_code