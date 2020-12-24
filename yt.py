import pafy, time, datetime
def out_red(text):
    print("\033[31m {} \033[0m" .format(text))
def out_green(text):
	print("\033[32m {} \033[0m" .format(text))
def out_blue(text):
	print("\033[34m {} \033[0m" .format(text))
banner = """
 ____________________________
|                            |
| YouTube Video Downloader   |
| Author: ilya1391           |
| Version: 1.0               |
| Status: Stable             |
|____________________________|
"""
out_blue(banner)
time.sleep(0.6)
url = input('\033[34mEnter your link on Youtube Video (https://www.youtube.com/watch?v=XXXXXXX) -> \033[0m')
try:
	video = pafy.new(url)
	streams = video.streams
	best_stream = video.getbest()
	best_stream.download()
	out_green("Complete download video!")
except:
	out_red("Error download video. Please cheking your link!")