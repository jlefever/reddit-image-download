import sys, praw
from praw import objects

# User Credentials
username = sys.argv[1]
password = sys.argv[2]

# Reddit Object
user_agent = "Reddit Image Downloader"
r = praw.Reddit(user_agent=user_agent)

r.login(username, password, disable_warning=True)
saved = r.user.get_saved(sort=u'new', time=u'all', limit=None)

for s in saved:
	print(str(s).encode("utf-8"))

# def download_direct_image(submission):

# def download_imgur(submssion):

# def download_gfycat(submssion):