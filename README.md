# twitter_post
Twitter Post Action Repo

## Example usage

```yaml
name: publish-to-twitter
on: [release]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: 3.x

      - name: Install dependencies
        run: |
          pip install tweepy

      - name: Publish tweet
        uses: intelowlproject/twitter-post
        with:
          status: Add publish notes here
          api_key: ${{ secrets.TWITTER_API_KEY}}
          api_key_secrets: ${{ secrets.TWITTER_API_KEY_SECRET}}
          access_token: ${{ secrets.TWITTER_ACCESS_TOKEN}}
          access_token_secret: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET}}
```
