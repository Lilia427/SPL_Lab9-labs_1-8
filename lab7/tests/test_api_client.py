import pytest
from api.api_client import ApiClient

@pytest.fixture
def api_client():
    return ApiClient()

def test_get_posts(api_client):
    posts = api_client.get_posts()
    assert isinstance(posts, list)
    assert len(posts) > 0
    assert "id" in posts[0]

def test_get_post(api_client):
    post = api_client.get_post(1)
    assert isinstance(post, dict)
    assert post["id"] == 1

def test_get_comments_for_post(api_client):
    comments = api_client.get_comments_for_post(1)
    assert isinstance(comments, list)
    assert len(comments) > 0
    assert "postId" in comments[0]
    assert comments[0]["postId"] == 1
