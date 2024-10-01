## response Type : 한글 포함일 경우
      
      res = {
        	'id?' : id,
            'ResultimgURL' : rimgURL,
            'imgURL' : imgURL,
            'answer_text' : answer,
            'num?' : num
        }
      res = make_response(json.dumps(res, ensure_ascii=False))

       
        
      # header Options
      res.headers['Content-Type'] = 'application/json; charset=utf-8' 
        
      return res;


    
