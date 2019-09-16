from facebook_post import *
from reddit_post import *
from twitter_post import *

import argparse


def main():
    print("Posting to CompSoc Social Media")
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str,help="Text to be posted")
    parser.add_argument("-l", "--link", help="Make a link post")
    parser.add_argument("-i", "--image", help="Make an image post")

    args = parser.parse_args()

    if args.image:
        try:
            facebookImagePost(args.text, args.image)
        except:
            print("Error: FB img post")

        try:
            twitterImagePost(args.text, args.image)
        except:
            print("Error: TWTR img post")

        try:
            redditImagePost(args.text, args.image)
        except:
            print("Error: RDT img post")
            
    elif args.link:
        try:
            facebookLinkPost(args.text, args.link)
        except:
            print("Error: FB lnk post")
        
        try:
            twitterLinkPost(args.text, args.link)
        except:
            print("Error: TWTR lnk post")
        
        try:
            redditLinkPost(args.text, args.link)
        except:
            print("Error: RDT lnk post")
        
    else:
        try:
            facebookTextPost(args.text, args.text)
        except:
            print("Error: FB txt post")
        
        try:
            twitterTextPost(args.text, args.text)
        except:
            print("Error: TWTR txt post")
        
        try:
            redditTextPost(args.text, args.text)
        except:
            print("Error: RDT txt post")

if __name__ == '__main__':
    main()
