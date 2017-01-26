import tweepy
import time


class TweetPruner:

    def __init__(self, c_key, c_secret, a_token, a_token_secret):
        auth = tweepy.OAuthHandler(c_key, c_secret)
        auth.set_access_token(a_token, a_token_secret)
        self.api = tweepy.API(auth)
        self.tweet_sample = []
        self.user_tweet_count = {}


    def grab_sample(self):

        some_tweets = []
        while not some_tweets:
            try:
                some_tweets = self.api.home_timeline(count=200, exclude_mentions=True)
            except tweepy.error.RateLimitError:
                print("sleep one min")
                time.sleep(60)

        self.tweet_sample.extend(some_tweets)
        max_id = some_tweets[-1].id

        while len(self.tweet_sample)<100: # TODO: change this conditional
            try:
                more_tweets = self.api.home_timeline(count=200, max_id=max_id, exclude_mentions=True)
                self.tweet_sample.extend(more_tweets[1:]) # exclude first tweet b/c it is the same as last tweet in last bunch
                print("  getting more tweets (%s tweets so far)" % len(self.tweet_sample))
            except tweepy.error.RateLimitError:
                print("  waiting a minute...")
                time.sleep(60)


    def count_tweets(self):

        if not self.tweet_sample:
            self.grab_sample()

        for t in self.tweet_sample:
            try:
                self.user_tweet_count[t.user.screen_name] += 1
            except KeyError:
                self.user_tweet_count[t.user.screen_name] = 1


    def show_worst_offenders(self):

        if not self.user_tweet_count:
            self.count_tweets()

        sorted_offenders = sorted(self.user_tweet_count, key=self.user_tweet_count.get)
        # if len(self.user_tweet_count) > 20: #TODO: add some way to cut down on rows returned
        #     worst_offenders = sorted_offenders[-20:]
        # else:
        #     worst_offenders = sorted_offenders
        worst_offenders = sorted_offenders

        max_tweets = self.user_tweet_count[worst_offenders[-1]]
        bar_unit = max(1,max_tweets/20)
        for u in reversed(worst_offenders):
            bar_length = int(self.user_tweet_count[u]/bar_unit)
            self.pretty_tbl_print('@'+u, self.user_tweet_count[u], bar_length*'*')


    def pretty_tbl_print(self, col1, col2, col3):
        # col 1 length 18, col 2 len 4
        tbl_row = "%s%s%s%s%s" %(col1, (18-len(str(col1)))*' ', col2, (4-len(str(col2)))*' ', col3)
        print(tbl_row)