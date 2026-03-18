import sys
import requests

BASE_URL = "https://api.github.com"

HEADERS = {"Accept": "application/vnd.github+json"}


def fetch_user(username: str) -> dict:
    url = f"{BASE_URL}/users/{username}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
    except requests.exceptions.ConnectionError:
        print("Network error: could not reach GitHub. Check your internet connection.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Network error: the request timed out. Try again in a moment.")
        sys.exit(1)

    if response.status_code == 404:
        print(f"User not found: '{username}' does not exist on GitHub.")
        sys.exit(1)
    if response.status_code == 403:
        reset = response.headers.get("X-RateLimit-Reset", "unknown")
        print(f"Rate limit hit: you've exceeded 60 requests/hour (unauthenticated limit). "
              f"Resets at UNIX timestamp {reset}. Wait a bit and try again.")
        sys.exit(1)
    if not response.ok:
        print(f"Unexpected error {response.status_code}: {response.json().get('message', 'no details')}")
        sys.exit(1)

    return response.json()


def fetch_top_repos(username: str, top_n: int = 5) -> list[dict]:
    url = f"{BASE_URL}/users/{username}/repos"
    params = {"per_page": 100, "type": "owner"}
    try:
        response = requests.get(url, headers=HEADERS, params=params, timeout=10)
    except requests.exceptions.ConnectionError:
        print("Network error: could not reach GitHub while fetching repos.")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("Network error: repo request timed out.")
        sys.exit(1)

    if response.status_code == 403:
        print("Rate limit hit while fetching repos. Wait a bit and try again.")
        sys.exit(1)
    if not response.ok:
        return []

    repos = response.json()
    sorted_repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)
    return sorted_repos[:top_n]


def display_profile(user: dict, repos: list[dict]) -> None:
    divider = "─" * 50

    print(f"\n{divider}")
    print(f"  GitHub Profile: {user.get('login', 'N/A')}")
    print(divider)
    print(f"  Name          : {user.get('name') or '—'}")
    print(f"  Bio           : {user.get('bio') or '—'}")
    print(f"  Public Repos  : {user.get('public_repos', 0)}")
    print(f"  Followers     : {user.get('followers', 0)}")
    print(f"  Following     : {user.get('following', 0)}")
    print(f"  Location      : {user.get('location') or '—'}")
    print(f"  Profile URL   : {user.get('html_url', '—')}")

    print(f"\n  Top {len(repos)} Repos by Stars")
    print(f"  {'─' * 46}")
    if not repos:
        print("  No public repositories found.")
    else:
        for i, repo in enumerate(repos, 1):
            name     = repo.get("name", "unknown")
            stars    = repo.get("stargazers_count", 0)
            language = repo.get("language") or "N/A"
            print(f"  {i}. {name}")
            print(f"     ⭐ {stars} stars   |   Language: {language}")

    print(f"{divider}\n")


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <github_username>")
        sys.exit(1)

    username = sys.argv[1].strip()
    print(f"Fetching GitHub profile for '{username}'...")

    user  = fetch_user(username)
    repos = fetch_top_repos(username)
    display_profile(user, repos)


if __name__ == "__main__":
    main()