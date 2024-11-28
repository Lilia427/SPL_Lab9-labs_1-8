import pytest
from api.response_parser import ResponseParser

def test_format_posts():
    posts = [{"id": 1, "title": "Test Post"}, {"id": 2}]
    formatted = ResponseParser.format_posts(posts)
    expected_output = (
        "ID: 1 | Title: Test Post\n"
        "ID: 2 | Title: No Title"
    )
    assert formatted == expected_output

def test_format_comments():
    comments = [
        {"id": 1, "name": "Commenter 1", "body": "This is a comment"},
        {"id": 2, "name": "Commenter 2"}
    ]
    formatted = ResponseParser.format_comments(comments)
    expected_output = (
        "ID: 1 | Name: Commenter 1\nBody: This is a comment\n"
        "ID: 2 | Name: Commenter 2\nBody: No Body"
    )
    assert formatted == expected_output

def test_format_users():
    users = [
        {"id": 1, "name": "User 1", "email": "user1@example.com"},
        {"id": 2}
    ]
    formatted = ResponseParser.format_users(users)
    expected_output = (
        "ID: 1 | Name: User 1 | Email: user1@example.com\n"
        "ID: 2 | Name: No Name | Email: No Email"
    )
    assert formatted == expected_output
