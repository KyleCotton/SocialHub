"""Reddit Poster

This script allows the user to post various types of posts to reddit.

This script requires that `praw` be installed within the Python
environment you are running this script in. See `requirements.txt`.

This file can also be imported as a module and contains the following
functions:
    - redditTextPost : Makes text only post to Reddit
    - redditLinkPost : Makes text & link post to Reddit
    - redditImagePost: Makes text & image post to Reddit
"""

import praw
import json


# TODO: Check for valid inputs etc

with open("config.json") as f:
  data = json.load(f)

reddit = praw.Reddit(client_id     =data["reddit"]["client_id"],
                     client_secret =data["reddit"]["client_secret"],
                     password      =data["reddit"]["password"],
                     user_agent    =data["reddit"]["user_agent"],
                     username      =data["reddit"]["username"])


def redditTextPost(message):
    """Post a Text Post to Reddit

Makes a simple text only post to the page.
Text to be posted is required passed as an argument.

Parameters
----------
message : str, required
          The text to be posted.
"""

    reddit.subreddit("compsoc").submit(message, selftext="")
    

def redditLinkPost(message, link):
    """Post a Text Post with a Link to Reddit 

Makes a text post to the page with a included link.
Text to be posted is required passed as an argument.
Link to be posted is required passed as an argument.

Parameters
----------
message : str, required
          The text to be posted.
link    : str, required
          The link to be posted.
"""

    reddit.subreddit("compsoc").submit(message, url=link)
    

def redditImagePost(message, image):
    """Post a Image Post to Reddit

Makes a simple text only post to the page.
Text to be posted is required passed as an argument.

Parameters
----------
message : str, required
          The text to be posted.
image : str, required
          Local location of the file to be uploaded
          Supported Formats: jpg, png
"""

    reddit.subreddit("compsoc").submit_image(message, image)
