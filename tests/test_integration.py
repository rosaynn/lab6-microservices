import requests
import time


MG_URL = "http://localhost:9007"
AU_URL = "http://localhost:8007"


def test_create_action_and_audit_docker():
    # post an action to management
    r = requests.post(f"{MG_URL}/action", json={"action_name": "deploy"}, timeout=5)
    assert r.status_code == 200
    data = r.json()
    assert data.get("message") == "Action completed"

    # verify management lists the action
    list_r = requests.get(f"{MG_URL}/actions", timeout=5)
    assert list_r.status_code == 200
    actions = list_r.json().get("actions", [])
    assert any(a.get("action_name") == "deploy" for a in actions)

    # give services a short moment to propagate
    time.sleep(0.1)

    # search recent audit ids for the created audit entry
    found = False
    for aid in range(701, 801):
        resp = requests.get(f"{AU_URL}/audit/{aid}")
        if resp.status_code == 200:
            audit = resp.json().get("audit", {})
            if audit.get("action", "").startswith("Management action: deploy"):
                found = True
                break

    assert found, "Audit entry for the management action was not found"
