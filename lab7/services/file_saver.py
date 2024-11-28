import json
import csv


class FileSaver:
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}.")

    @staticmethod
    def save_to_csv(data, filename, headers):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}.")

    @staticmethod
    def save_to_txt(data, filename):
        with open(filename, "w") as file:
            file.write(data)
        print(f"Data saved to {filename}.")

    @staticmethod
    def format_posts_for_txt(posts):
        formatted_posts = []
        for post in posts:
            formatted_posts.append(
                f"Post ID: {post['id']}\n"
                f"User ID: {post['userId']}\n"
                f"Title: {post['title']}\n"
                f"Body:\n{post['body']}\n"
                f"{'-'*40}\n"
            )
        return "".join(formatted_posts)
