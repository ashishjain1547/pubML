# -*- coding: utf-8 -*-

import os
import sys
import twitter

from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

# Go to http://twitter.com/apps/new to create an app and get these items

# Error 404 (Dated: 20220920)
# For URL: http://dev.twitter.com/pages/oauth_single_token

APP_NAME = 'e***1'
CONSUMER_KEY = 'I***9'
CONSUMER_SECRET = 'B***U'


def oauth_login(app_name=APP_NAME,
                consumer_key=CONSUMER_KEY, 
                consumer_secret=CONSUMER_SECRET, 
                token_file='out/twitter.oauth'):

    try:
        (access_token, access_token_secret) = read_token_file(token_file)
        
    except Exception as e: 
        # FileNotFoundError, IOError
        
        (access_token, access_token_secret) = oauth_dance(app_name, consumer_key, consumer_secret)

        if not os.path.isdir('out'):
            os.mkdir('out')

        write_token_file(token_file, access_token, access_token_secret)

        print(sys.stderr, "OAuth Success. Token file stored to", token_file)

    return twitter.Twitter(auth=twitter.oauth.OAuth(access_token, access_token_secret,
                           consumer_key, consumer_secret))

if __name__ == '__main__':

    oauth_login(APP_NAME, CONSUMER_KEY, CONSUMER_SECRET)
