import praw
import config

def bot_login():
    reddit = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Seth's dog comment responder v1")
    return reddit

def run_bot(r):
    for comment in r.subreddit('test').comments(limit=25):
        if "dog" in comment.body:
            print("dog has been found!") 
            comment.reply("I also love dogs")

r = bot_login()
run_bot(r)