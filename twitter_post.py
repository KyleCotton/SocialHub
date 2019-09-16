"""Twitter Poster

This script allows the user to post various types of posts to twitter.

This script requires that `tweepy` be installed within the Python
environment you are running this script in. See `requirements.txt`.

This file can also be imported as a module and contains the following
functions:
    - twitterTextPost : Makes text only post to Twitter
    - twitterLinkPost : Makes text & link post to Twitter
    - twitterImagePost: Makes text & image post to Twitter
"""
# TODO: Check for valid inputs etc

import tweepy
import json

with open("config.json") as f:
  data = json.load(f)

auth = tweepy.OAuthHandler(data["twitter"]["consumer_key"],
                           data["twitter"]["consumer_secret"])
auth.set_access_token(data["twitter"]["access_token"],
                      data["twitter"]["access_token_secret"])

api = tweepy.API(auth)


def twitterTextPost(message):
    """Post a Text Post to Twitter

Makes a simple text only post to the page.
Text to be posted is required passed as an argument.

Parameters
----------
message : str, required
          The text to be posted.
"""
    
    api.update_status(message)


def twitterLinkPost(message, link):
    """Post a Text Post with a Link to Twitter 

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
    
    api.update_status(message+"\n"+link)

def twitterImagePost(message, image):
    """Post a Image Post to Twitter

Makes a simple text only post to the page.
Text to be posted is required passed as an argument.

Parameters
----------
message : str, required
          The text to be posted.
image   : str, required
          Local location of the file to be uploaded
          Supported Formats: jpg, png
"""

    api.update_with_media(image, message)
