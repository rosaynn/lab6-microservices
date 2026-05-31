from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

STUDENT_N = 7

AUDIT_SERVICE_URL = "http://audit-service:8000"

app = FastAPI(title=f"Management Service N{STUDENT_N}")

ACTIONS = []


class ActionRequest(BaseModel):
    action_name: str


@app.post("/action")
def create_action(action: ActionRequest):

    try:
        audit_response = requests.post(
            f"{AUDIT_SERVICE_URL}/audit/log",
            json={
                "action": f"Management action: {action.action_name}"
            }
        )

    except requests.exceptions.ConnectionError:
        raise HTTPException(
            status_code=503,
            detail="Audit Service unavailable"
        )

    if audit_response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail="Audit logging failed"
        )

    new_action = {
        "id": len(ACTIONS) + 701,
        "action_name": action.action_name,
        "status": "Completed"
    }

    ACTIONS.append(new_action)

    return {
        "student_id": STUDENT_N,
        "message": "Action completed",
        "action": new_action
    }


@app.get("/actions")
def get_actions():

    return {
        "student_id": STUDENT_N,
        "actions": ACTIONS
    }