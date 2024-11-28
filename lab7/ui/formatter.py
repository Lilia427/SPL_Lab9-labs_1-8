class Formatter:
    @staticmethod
    def format_post(post):
        return f"ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}"

    @staticmethod
    def format_comment(comment):
        return f"ID: {comment['id']}\nName: {comment['name']}\nEmail: {comment['email']}\nBody: {comment['body']}"

    @staticmethod
    def format_user(user):
        return f"ID: {user['id']}\nName: {user['name']}\nEmail: {user['email']}\nCompany: {user['company']['name']}"
