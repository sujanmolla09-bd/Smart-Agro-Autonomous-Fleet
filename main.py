import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

def agent_data_collector():
    return {
        "field_id": "BD-AGRO-ZONE-01",
        "soil_moisture_pct": 18.5,
        "temperature_c": 33.2,
        "crop_type": "Boro Rice"
    }

def agent_agro_analyzer(telemetry):
    soil_moisture = telemetry.get("soil_moisture_pct", 100)
    if soil_moisture < 25.0:
        return {
            "risk_level": "HIGH",
            "action_required": "IRRIGATE_NOW",
            "reason": "Soil moisture is below optimal threshold (25%)."
        }
    return {
        "risk_level": "LOW",
        "action_required": "NONE",
        "reason": "Optimal conditions maintained."
    }

def agent_action_executor(analysis):
    if analysis["action_required"] == "IRRIGATE_NOW":
        return {
            "execution_status": "SUCCESS",
            "command_sent": "ACTIVATE_PUMP_VALVE_01",
            "duration_minutes": 30
        }
    return {
        "execution_status": "STANDBY",
        "command_sent": "NONE",
        "duration_minutes": 0
    }

@app.route('/', methods=['GET', 'POST'])
def run_fleet():
    telemetry = agent_data_collector()
    analysis = agent_agro_analyzer(telemetry)
    execution = agent_action_executor(analysis)

    response_payload = {
        "status": "COMPLETED",
        "system": "Smart Agro Autonomous Operations Fleet",
        "workflow": {
            "step_1_data_collector": telemetry,
            "step_2_agro_analyzer": analysis,
            "step_3_action_executor": execution
        }
    }
    return jsonify(response_payload), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
