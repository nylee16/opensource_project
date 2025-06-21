from flask import Flask, request, jsonify
from fire_detection_inference import FireDetectionInference
import os
import logging

# Hugging Face 토큰 설정
from huggingface_hub import login
login("") # hugging face 토큰 입력

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# 전역 변수로 모델 인스턴스 생성
try:
    detector = FireDetectionInference()
    logger.info("Fire detection model loaded successfully")
except Exception as e:
    logger.error(f"Failed to load model: {e}")
    detector = None

@app.route('/health', methods=['GET'])
def health_check():
    """헬스 체크 엔드포인트"""
    return jsonify({
        "status": "healthy",
        "model_loaded": detector is not None
    })

@app.route('/predict', methods=['POST'])
def predict_fire():
    """단일 오디오 파일에 대한 화재 감지 예측"""
    try:
        # 요청 데이터 확인
        if 'audio_file' not in request.files:
            return jsonify({
                "error": "No audio file provided",
                "situation": "error",
                "confidence": 0.0
            }), 400
        
        audio_file = request.files['audio_file']
        
        # 파일 확장자 확인
        if not audio_file.filename.lower().endswith('.wav'):
            return jsonify({
                "error": "Only WAV files are supported",
                "situation": "error",
                "confidence": 0.0
            }), 400
        
        # 임시 파일로 저장
        temp_path = f"temp_{audio_file.filename}"
        audio_file.save(temp_path)
        
        try:
            # 예측 수행
            result = detector.predict_fire_situation(temp_path)
            
            # 임시 파일 삭제
            os.remove(temp_path)
            
            return jsonify(result)
            
        except Exception as e:
            # 임시 파일 삭제
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise e
            
    except Exception as e:
        logger.error(f"Error in predict endpoint: {e}")
        return jsonify({
            "error": str(e),
            "situation": "error",
            "confidence": 0.0
        }), 500

@app.route('/predict_path', methods=['POST'])
def predict_fire_by_path():
    """파일 경로를 통한 화재 감지 예측"""
    try:
        data = request.get_json()
        
        if not data or 'audio_path' not in data:
            return jsonify({
                "error": "No audio path provided",
                "situation": "error",
                "confidence": 0.0
            }), 400
        
        audio_path = data['audio_path']
        
        # 파일 존재 확인
        if not os.path.exists(audio_path):
            return jsonify({
                "error": "Audio file not found",
                "situation": "error",
                "confidence": 0.0
            }), 404
        
        # 예측 수행
        result = detector.predict_fire_situation(audio_path)
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Error in predict_path endpoint: {e}")
        return jsonify({
            "error": str(e),
            "situation": "error",
            "confidence": 0.0
        }), 500

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    """디렉토리 내 모든 wav 파일에 대한 배치 예측"""
    try:
        data = request.get_json()
        
        if not data or 'audio_directory' not in data:
            return jsonify({
                "error": "No audio directory provided",
                "summary": {},
                "detailed_results": []
            }), 400
        
        audio_directory = data['audio_directory']
        
        # 디렉토리 존재 확인
        if not os.path.exists(audio_directory):
            return jsonify({
                "error": "Audio directory not found",
                "summary": {},
                "detailed_results": []
            }), 404
        
        # 배치 예측 수행
        results = detector.batch_predict(audio_directory)
        
        return jsonify(results)
        
    except Exception as e:
        logger.error(f"Error in batch_predict endpoint: {e}")
        return jsonify({
            "error": str(e),
            "summary": {},
            "detailed_results": []
        }), 500

@app.route('/ui_status', methods=['GET'])
def get_ui_status():
    """UI 상태 정보 반환"""
    return jsonify({
        "model_status": "loaded" if detector is not None else "not_loaded",
        "supported_actions": [
            "show_fire_alert",
            "show_normal_screen", 
            "show_warning",
            "show_error"
        ],
        "api_endpoints": [
            "/health",
            "/predict",
            "/predict_path", 
            "/batch_predict",
            "/ui_status"
        ]
    })

if __name__ == '__main__':
    # 개발 서버 실행 (포트 5001로 변경)
    app.run(host='0.0.0.0', port=5001, debug=True) 