import sys, praw
import requests
from posixpath import basename
from urllib.request import urlretrieve

def main():
	# User Credentials
	username = sys.argv[1]
	password = sys.argv[2]

	# Reddit Object
	user_agent = "Reddit Image Downloader"
	r = praw.Reddit(user_agent=user_agent)

	r.login(username, password, disable_warning=True)
	saved = r.user.get_saved(sort=u'new', time=u'all', limit=None)

	# Download gfycat videos
	saved_subs  = [x for x in saved if type(x) is praw.objects.Submission]
	gfycat_urls = [x.url for x in saved_subs if x.domain == 'gfycat.com']
	#image_urls  = [x.url for x in saved_subs if request.get(x.url).headers.get('content-type').startswith('image')]

	gfycat_download(gfycat_urls, True)

def gfycat_download(urls, mp4):
	for url in urls:
		gfycat_id = basename(url)
		api_url = 'http://gfycat.com/cajax/get/' + gfycat_id

		res = requests.get(api_url).json()
		if 'gfyItem' in res:
			video_url   = res['gfyItem']['mp4Url'] if mp4 else res['gfyItem']['webmUrl']
			reddit_text = res['gfyItem']['redditIdText']
			filename  = reddit_text if reddit_text != None else gfycat_id
			filesize  = res['gfyItem']['webmSize']
			if filesize != 0:
				print("Saving " + filename + " (" + str(filesize) + " Bytes)")
				urlretrieve(video_url, filename=filename + '.mp4' if mp4 else '.webm')
		else:
			print(url + " was deleted.")

#def image_download(urls):


if __name__ == "__main__": main()