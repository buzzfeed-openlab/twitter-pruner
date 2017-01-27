# twitter-prune
Identify who's hogging too much space in your twitter feed! All you need is Python & a Twitter account.

If you don't know what GitHub is - hi! & welcome! This is a place where people put their code & collaborate on projects, among other things. Here, you can view a project's [history](https://github.com/buzzfeed-openlab/twitter-pruner/commits/master) & [discussions](https://github.com/buzzfeed-openlab/twitter-pruner/issues).

## How to use this

**1. Download this code**

If you have git:
```bash
git clone https://github.com/buzzfeed-openlab/twitter-pruner.git
cd twitter-pruner
```

If you don't know what git is...don't worry - click the green "Clone or download" button. Then, open up the command line (if you're on a Mac, it's the Terminal app) and navigate inside this project directory (the rest of the commands in these instructions will only work if you are in the right directory).

**2. Install required python libraries**

Make sure you have Python installed (if you're on a Mac, you already have Python).

Make sure you have pip, too. (Context: open-source code usually makes it easier to do something that'd be tedious to do from scratch. pip is for easily installing Python code that other people have written - in this case, [tweepy](http://www.tweepy.org/), a python library that makes it easier to work with the Twitter api)

Optional but recommended: make a virtual environment using [virtualenv](https://virtualenv.readthedocs.io/en/latest/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html). This is a good practive b/c it helps you manage your environments when you work on many projects with varying dependencies. If that last sentence sounds like gibberish...don't worry about it for now.

To install required python libraries:
```bash
pip install -r requirements.txt
```

**2. Copy the example script**

```bash
cp run.py.example run.py
```
You now have your own script, `run.py` (this is gitignored to keep twitter credentials from accidently getting into version control)

**2. Add Twitter API credentials**

Edit `run.py` with your twitter credentials.

To get twitter api credentials, go to https://apps.twitter.com/ & create a new app. Then, in the 'Keys & Access Tokens' tab, click the 'Create my access token' button. You'll need the Consumer Key, Consumer Secret, Access Token, & Access Token Secret. These credentials allow you to programmatically read & write tweets! (This means you should keep them secret)

**3. Run the script!**

```bash
python run.py
```
Feel free to play around with the arguments passed into the `show_worst_offenders()` method.

Now, mute or unfollow people with the ~objective data~ you've collected. Rinse & repeat.
