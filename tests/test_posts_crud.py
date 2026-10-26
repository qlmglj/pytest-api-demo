import pytest

POST_IDS = [1, 2, 3, 50]


@pytest.mark.network
@pytest.mark.parametrize("post_id", POST_IDS)
def test_get_post_by_id(api, post_id):
    resp = api.get(f"/posts/{post_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == post_id
    assert data["title"]


@pytest.mark.network
def test_list_posts_filtered_by_user(api):
    resp = api.get("/posts", params={"userId": 1})
    assert resp.status_code == 200
    posts = resp.json()
    assert len(posts) == 10
    assert {p["userId"] for p in posts} == {1}


@pytest.mark.network
def test_create_post_echoes_payload(api):
    payload = {"title": "接口自动化练习", "body": "pytest + requests", "userId": 1}
    resp = api.post("/posts", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    for key, value in payload.items():
        assert data[key] == value
    assert "id" in data


@pytest.mark.network
def test_update_post(api):
    resp = api.put("/posts/1", json={"id": 1, "title": "updated", "userId": 1})
    assert resp.status_code == 200
    assert resp.json()["title"] == "updated"


@pytest.mark.network
def test_delete_post(api):
    resp = api.delete("/posts/1")
    assert resp.status_code in (200, 204)


@pytest.mark.network
def test_missing_post_returns_404(api):
    resp = api.get("/posts/999999")
    assert resp.status_code == 404
