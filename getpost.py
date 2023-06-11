import praw
import json
import requests
import re
import credentails
from pathlib import Path
def postdata():
        print(credentails.reddit.read_only)
        subreddit = credentails.reddit.subreddit("AmItheAsshole")
        for post in subreddit.new(limit=1):
                title = (post.title)
                body = post.selftext.replace('\n', '').replace('\u2019','').replace('\r', '').replace('\u00e9', '')
                body = re.sub(r'[^a-zA-Z0-9.\s]', '', body)

        post_data ={
                "title" : title,
                "post_body" : body
                }

        with open("post_data.json", "w") as file:
                json.dump(post_data, file, indent=4)
                print("passed 1")
        
        data = Path("post_data.json").read_text()
        final = json.loads(data)
        #print(final)
        print("passed 2")
        return final

        






