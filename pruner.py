import tweepy
import time
import datetime


class TweetPruner:

    def __init__(self, c_key, c_secret, a_token, a_token_secret):
        auth = tweepy.OAuthHandler(c_key, c_secret)
        auth.set_access_token(a_token, a_token_secret)
        self.api = tweepy.API(auth)
        self.tweet_sample = []


    def grab_sample(self):

        last_id = None
        while len(self.tweet_sample)<800: # 800 is the limit
            try:
                grabbed = self.api.home_timeline(count=200, max_id=last_id, exclude_mentions=True)
                if len(grabbed)==1: # if hitting the limit
                    break

                self.tweet_sample.extend(grabbed[1:]) # exclude first tweet b/c it is the same as last tweet in last bunch
                print("  grabbing tweets ({} tweets so far)".format(len(self.tweet_sample)))
                last_id = grabbed[-1].id
            except tweepy.error.RateLimitError:
                print("  waiting a minute...")
                time.sleep(60)


    def count_tweets(self, keyword=None):

        user_tally = {}

        if not self.tweet_sample:
            self.grab_sample()

        for t in self.tweet_sample:
            if not keyword or keyword.lower() in t.text.lower():
                try:
                    user_tally[t.user.screen_name] += 1
                except KeyError:
                    user_tally[t.user.screen_name] = 1

        return user_tally


    def show_worst_offenders(self, max_show=None, keyword=None):

        user_tally = self.count_tweets(keyword=keyword)

        sorted_offenders = sorted(user_tally, key=user_tally.get)
        if max_show and len(user_tally) > max_show:
            worst_offenders = sorted_offenders[-max_show:]
        else:
            worst_offenders = sorted_offenders

        max_tweets = user_tally[worst_offenders[-1]]
        bar_unit = max(1,max_tweets/20)

        num_str = '{} '.format(max_show) if max_show else ''
        if keyword:
            print("\n\n\nTHESE ARE THE {}PEOPLE WHO ARE TWEETING '{}' THE MOST\n".format(num_str, keyword.upper()))
        else:
            print("\n\n\nTHESE ARE THE {}PEOPLE WHO ARE HOGGING THE MOST SPACE\n".format(num_str))

        self.pretty_tbl_print('handle', 'tweets', '')
        print('-'*45)
        for u in reversed(worst_offenders):
            bar_length = int(user_tally[u]/bar_unit)
            self.pretty_tbl_print('@'+u, user_tally[u], bar_length*'*')


    def pretty_tbl_print(self, col1, col2, col3):
        # col 1 length 24, col 2 len 4
        tbl_row = "{}{}{}{}{}".format(col1, (24-len(str(col1)))*' ', col2, (4-len(str(col2)))*' ', col3)
        print(tbl_row)
