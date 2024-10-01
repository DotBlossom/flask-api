from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/flaskapi/<int:id>', methods=['POST'])
def send_to_gpu_server(id):
    if 'image' not in request.files:
        return jsonify({"에러": "이미지 없음"}), 400

    image_file = request.files['image']

    # OCR URL
    ocr_url = 'http://127.0.0.1:5000/ocr'
    
    # 이미지 파일을 OCR에 맞춰 변환(dict 형식)
    files = {'image': (image_file.filename, image_file, image_file.content_type)}

    try:
        # OCR POST 요청
        ocr_response = requests.post(ocr_url, files=files)

        # OCR 요청 성공시
        if ocr_response.ok:
            ocr_data = ocr_response.json()
            call_menu_item = []  # 메뉴 아이템 초기화

            # OCR 데이터에서 필요한 정보를 추출
            if '메뉴 및 가격' in ocr_data:
                call_menu_item = ocr_data['메뉴 및 가격']
            
            
            # 추가적인 처리 로직
            return jsonify({"메뉴 및 가격": call_menu_item}), 200
            
        else:
            return jsonify({"OCR 요청 실패": ocr_response.text}), 500

    except Exception as e:
        return jsonify({"이미지 전송 오류": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
