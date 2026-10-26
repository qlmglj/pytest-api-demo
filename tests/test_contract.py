import pytest

SCHEMA = {"userId": int, "id": int, "title": str, "body": str}


@pytest.mark.network
def test_post_response_contract(api):
    data = api.get("/posts/1").json()
    for field, expected_type in SCHEMA.items():
        assert field in data, f"返回体缺少字段 {field}"
        assert isinstance(data[field], expected_type), (
            f"字段 {field} 类型应为 {expected_type.__name__}，实际 {type(data[field]).__name__}"
        )
