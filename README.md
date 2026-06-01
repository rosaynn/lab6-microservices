# lab6-microservices
lab6-microservices

Quick test
---------

Run the simple integration test (requires `pytest`):

```bash
pip install pytest
pytest -q
```

The repository contains two services: `audit_service` and `management_service`. The management service posts audit logs to the audit service before completing actions.

See the sequence diagram in `sequence_diagram.md` for the interaction flow.

**How to present to a teacher**

- **What to show:** Run the system with Docker Compose and demonstrate the Management Service calling the Audit Service to record actions. Show the POST /action flow, then show the audit entry created via GET /audit/{id}.
- **Commands to run:**

```bash
docker-compose up --build
# in another terminal
curl -X POST http://localhost:9007/action -H 'Content-Type: application/json' -d '{"action_name":"deploy"}'
curl http://localhost:9007/actions
curl http://localhost:8007/audit/702
```

- **Explain:** `management_service` sends a POST to `audit_service` at `/audit/log` before completing any action; `audit_service` stores logs in-memory and exposes `GET /audit/{id}` to verify.
- **Testing notes:** Use `pytest` to run `tests/test_integration.py`. The test uses HTTP requests against locally running containers (no FastAPI imports needed), so you only need `pytest` and `requests` installed in your environment:

```bash
python -m pip install -r tests/requirements.txt
pytest -q
```

