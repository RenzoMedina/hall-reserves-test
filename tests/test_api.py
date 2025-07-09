from app.api import app

def test_success():
    client = app.test_client()
    res = client.post('/reservation', json={"room":"B", "time":"14:00"})
    assert res.status_code == 201

def test_failure():
    client = app.test_client()
    client.post('/reservation', json={"room":"B", "time":"14:00"})
    res = client.post('/reservation', json={"room":"B", "time":"14:00"})
    assert res.status_code == 409