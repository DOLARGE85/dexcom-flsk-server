from flask import Flask, jsonify
from pydexcom import Dexcom

app = Flask(__name__)

# Dexcom 계정 정보 (테스트용, 실제 배포 시 환경변수로 관리 권장)
DEXCOM_USERNAME = "your_dexcom_username"
DEXCOM_PASSWORD = "your_dexcom_password"

@app.route("/glucose", methods=["GET"])
def get_glucose():
    dexcom = Dexcom(DEXCOM_USERNAME, DEXCOM_PASSWORD)
    reading = dexcom.get_current_glucose_reading()
    if reading:
        return jsonify({
            "value": reading.value,
            "trend": reading.trend,
            "datetime": str(reading.datetime)
        })
    else:
        return jsonify({"error": "No data"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
