## What it does?

- connects to Reddit API
- fetches top 50 posts from r/technology
- takes all post titles
- removes common words like the, a, to
- counts which words appear the most
- finds the most upvoted post
- calculates average upvotes
- checks how many posts are from today and how many are older
- saves all results in a file named report.json

# How it does?

- `__init__()` → sets the API URL and stores the stopwords list.
- `get_response()` → sends request to Reddit and gets JSON data.
- `extract_posts()` → pulls out the actual post data from the Reddit response.
- `clean_words()` → cleans title words by lowercasing, removing punctuation, and skipping stopwords.
- `word_frequency()` → counts how many times each useful word appears in all titles.
- `most_upvoted_post()` → finds the post with the highest score.
- `average_upvotes()` → calculates the average score of all fetched posts.
- `posts_today_vs_older()` → checks which posts were made today and which are older.
- `create_report()` → combines all analysis results into one report dictionary.
- `save_report()` → writes the final report into `report.json`.
- `run()` → runs the full program from fetching data to printing and saving results.

## How to run it?

To run it just type:
'python mini_project.py

## Example Output (Actual Output)

{
"top_20_words": [
{
"word": "ai",
"count": 8
},
{
"word": "data",
"count": 5
},
{
"word": "new",
"count": 5
},
{
"word": "tech",
"count": 4
},
{
"word": "store",
"count": 3
},
{
"word": "why",
"count": 3
},
{
"word": "how",
"count": 3
},
{
"word": "its",
"count": 3
},
{
"word": "down",
"count": 3
},
{
"word": "layoffs",
"count": 2
},
{
"word": "now",
"count": 2
},
{
"word": "lost",
"count": 2
},
{
"word": "life",
"count": 2
},
{
"word": "says",
"count": 2
},
{
"word": "climate",
"count": 2
},
{
"word": "change",
"count": 2
},
{
"word": "us",
"count": 2
},
{
"word": "sony",
"count": 2
},
{
"word": "memory",
"count": 2
},
{
"word": "card",
"count": 2
}
],
"most_upvoted_post": {
"title": "Epic Games Layoffs Included Terminally Ill Father, Whose Family Has Now Lost His Life Insurance",
"score": 33147,
"author": "Turbostrider27",
"url": "https://www.thegamer.com/epic-games-layoff-terminally-ill-father/"
},
"average_upvotes": 1693.638888888889,
"posts_from_today": 8,
"posts_older": 28
}
