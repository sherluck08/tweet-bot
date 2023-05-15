import os
import random
import time
from datetime import datetime, timedelta

import schedule
from dotenv import load_dotenv


from twitter_utils import TwitterUtils


def send_tweet():
    status = "Yur tweet message here"
    twitter = TwitterUtils()

    twitter.tweet(status)


schedule.every(3).hours.do(send_tweet)

if __name__ == "__main__":
    print("[+] Tweeting every 3 hours....")
    # main()
    send_tweet()
    while True:
        schedule.run_pending()
        time.sleep(1)
