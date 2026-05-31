from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

STUDENT_N = 7

app = FastAPI(title=f"Audit Service N{STUDENT_N}")

AUDIT_LOGS = {
    701: {
        "id": 701,
        "action": "System started"
    }
}


class AuditRequest(BaseModel):
    action: str


@app.get("/audit/{id}")
def get_audit(id: int):

    if id not in AUDIT_LOGS:
        raise HTTPException(
            status_code=404,
            detail="Audit record not found"
        )

    return {
        "student_id": STUDENT_N,
        "audit": AUDIT_LOGS[id]
    }


@app.post("/audit/log")
def create_log(log: AuditRequest):

    new_id = max(AUDIT_LOGS.keys()) + 1

    AUDIT_LOGS[new_id] = {
        "id": new_id,
        "action": log.action
    }

    return {
        "student_id": STUDENT_N,
        "message": "Audit log created",
        "audit": AUDIT_LOGS[new_id]
    }