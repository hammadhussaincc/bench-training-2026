import requests
import json
from collections import Counter
from datetime import datetime, timezone


class RedditHeadlineAnalyzer:
    def __init__(self, url, limit, stopwords):
        self.url = f"{url}?limit={limit}"
        self.stopwords = stopwords

    def get_response(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            valid_response = response.json()
            return valid_response
        except requests.exceptions.Timeout:
            print("Error: Request timed out while connecting to Reddit.")
            return None

        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to Reddit.")
            return None

        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            return None

    def extract_posts(self, payload):
        children = payload.get("data", {}).get("children", [])
        posts = [item.get("data", {}) for item in children]
        return posts

    def clean_words(self, title):
        words = title.lower().split()
        cleaned_words = []

        for word in words:
            clean_word = ""
            for char in word:
                if char.isalnum():
                    clean_word += char

            if clean_word and clean_word not in self.stopwords:
                cleaned_words.append(clean_word)

        return cleaned_words

    def word_frequency(self, posts):
        all_words = []

        for post in posts:
            title = post.get("title", "")
            words = self.clean_words(title)
            all_words.extend(words)

        frequency = Counter(all_words)
        return frequency.most_common(20)

    def most_upvoted_post(self, posts):
        if not posts:
            return None

        max_post = posts[0]

        for post in posts:
            if post.get("score", 0) > max_post.get("score", 0):
                max_post = post

        return {
            "title": max_post.get("title", ""),
            "score": max_post.get("score", 0),
            "author": max_post.get("author", ""),
            "url": max_post.get("url", "")
        }

    def average_upvotes(self, posts):
        if not posts:
            return 0

        total = 0
        for post in posts:
            total += post.get("score", 0)

        avg = total / len(posts)
        return avg

    def posts_today_vs_older(self, posts):
        today_date = datetime.now(timezone.utc).date()
        today_count = 0
        older_count = 0

        for post in posts:
            created_utc = post.get("created_utc", 0)
            post_date = datetime.fromtimestamp(created_utc, timezone.utc).date()

            if post_date == today_date:
                today_count += 1
            else:
                older_count += 1

        return {
            "today": today_count,
            "older": older_count
        }

    def create_report(self):
        payload = self.get_response()
        posts = self.extract_posts(payload)

        top_words = self.word_frequency(posts)
        max_post = self.most_upvoted_post(posts)
        avg_upvotes = self.average_upvotes(posts)
        today_vs_older = self.posts_today_vs_older(posts)

        report = {
            "top_20_words": [{"word": word, "count": count} for word, count in top_words],
            "most_upvoted_post": max_post,
            "average_upvotes": avg_upvotes,
            "posts_from_today": today_vs_older["today"],
            "posts_older": today_vs_older["older"]
        }

        return report

    def save_report(self, report, filename="report.json"):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

    def run(self):
        report = self.create_report()

        print("\nTop 20 Words:")
        for item in report["top_20_words"]:
            print(f"{item['word']} : {item['count']}")

        print("\nMost Upvoted Post:")
        print(report["most_upvoted_post"])

        print("\nAverage Upvotes:")
        print(report["average_upvotes"])

        print("\nPosts From Today:")
        print(report["posts_from_today"])

        print("\nOlder Posts:")
        print(report["posts_older"])

        self.save_report(report)
        print("\nReport saved to report.json")


stopwords = {
    "the", "a", "an", "to", "of", "and", "in", "on", "for", "is", "it",
    "this", "that", "with", "as", "at", "by", "from", "be", "are", "was",
    "were", "or", "but", "if", "then", "so", "than", "too", "very", "has",
    "have", "had", "will", "would", "can", "could", "should", "do", "does",
    "did", "not", "no", "you", "your", "we", "they", "he", "she", "i"
}

analyzer = RedditHeadlineAnalyzer(
    url="https://reddit.com/r/technology/top.json",
    limit=50,
    stopwords=stopwords
)

analyzer.run()