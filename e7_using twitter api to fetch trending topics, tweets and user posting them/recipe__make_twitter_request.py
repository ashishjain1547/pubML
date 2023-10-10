# -*- coding: utf-8 -*-

import sys
import time

#from urllib2 import URLError
from urllib.error import URLError
import twitter

# See recipe__get_friends_followers.py for an example of how you might use 
# make_twitter_request to do something like harvest a bunch of friend ids for a user

def make_twitter_request(t, twitterFunction, max_errors=3, *args, **kwArgs): 

    # A nested function for handling common HTTPErrors. Return an updated value 
    # for wait_period if the problem is a 503 error. Block until the rate limit is 
    # reset if a rate limiting issue

    def handle_http_error(e, t, wait_period=2):

        if wait_period > 3600: # Seconds
            print >> sys.stderr, 'Too many retries. Quitting.'
            raise e

        if e.e.code == 401:
            print >> sys.stderr, 'Encountered 401 Error (Not Authorized)'
            return None

        if e.e.code in (502, 503):
            print >> sys.stderr, 'Encountered %i Error. Will retry in %i seconds' % \
                    (e.e.code, wait_period)
            time.sleep(wait_period)
            wait_period *= 1.5
            return wait_period

        # Rate limit exceeded. Wait 15 mins. See https://dev.twitter.com/docs/rate-limiting/1.1/limits
        if e.e.code == 429: 
            now = time.time()  # UTC
            sleep_time = 15*60 # 15 mins
            print >> sys.stderr, 'Rate limit reached: sleeping for 15 mins'
            time.sleep(sleep_time)
            return 0

        # What else can you do?
        raise e

    wait_period = 2
    error_count = 0
    while True:
        try:
            return twitterFunction(*args, **kwArgs)
        except twitter.api.TwitterHTTPError as e:
            error_count = 0
            wait_period = handle_http_error(e, t, wait_period)
            if wait_period is None:
                return
        except URLError as e:
            error_count += 1
            print >> sys.stderr, "URLError encountered. Continuing."
            if error_count > max_errors:
                print >> sys.stderr, "Too many consecutive errors...bailing out."
                raise
