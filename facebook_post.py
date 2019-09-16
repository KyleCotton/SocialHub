"""Facebook Poster

This script allows the user to post various types of posts to facebook.

This script requires that `facebook-sdk` be installed within the Python
environment you are running this script in. See `requirements.txt`.

This file can also be imported as a module and contains the following
functions:
    - facebookTextPost : Makes text only post to Facebook
    - facebookLinkPost : Makes text & link post to Facebook
    - facebookImagePost: Makes text & image post to Facebook
"""

import facebook
import json

# TODO: Check for valid inputs etc

with open("config.json") as f:
  data = json.load(f)

fb = facebook.GraphAPI(access_token = data["facebook"]["page_access_token"])


def facebookTextPost(message):
    """Post a Text Post to Facebook

Makes a simple text only post to the page.
Text to be posted is required passed as an argument.

Parameters
----------
message : str, required
          The text to be posted.
"""

    fb.put_object(
        parent_object="me",
        connection_name="feed",
        message=message)

def facebookLinkPost(message, link):
    """Post a Text Post with a Link to Facebook 

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
    
    fb.put_object(
        parent_object="me",
        connection_name="feed",
        message=message,
        link=link)


def facebookImagePost(message, image):
    """Post a Image Post to Facebook

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
    
    fb.put_photo(
        parent_object="me",
        connection_name="feed",
        message=message,
        image=open(image, "rb"))
