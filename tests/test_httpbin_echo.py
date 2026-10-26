import pytest


@pytest.mark.network
@pytest.mark.parametrize("code", [200, 201, 400, 401, 403, 418, 500, 503])
def test_status_codes(httpbin, code):
    resp = httpbin.get(f"/status/{code}")
    assert resp.status_code == code


@pytest.mark.network
def test_query_params_are_echoed(httpbin):
    resp = httpbin.get("/get", params={"keyword": "pytest", "page": 2})
    assert resp.status_code == 200
    assert resp.json()["args"] == {"keyword": "pytest", "page": "2"}


@pytest.mark.network
def test_json_body_is_echoed(httpbin):
    payload = {"module": "login", "case_id": 7}
    resp = httpbin.post("/post", json=payload)
    assert resp.status_code == 200
    assert resp.json()["json"] == payload
