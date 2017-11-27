from BeautifulSoup import BeautifulSoup
import argparse
import urllib
import time
import sys
import os

class colors:
  BLUE = "\033[94m"
  GREEN = "\033[92m"
  ORANGE = "\033[93m"
  RESET = "\033[0m"

free_pages = 35
pro_pages = 7
revised_pages = 6

video_url = "http://media.railscasts.com/assets/episodes/videos/"
video_format = ".mp4"

current_dir = os.getcwd()

def start(pages, video_type):
  for page in range(1, pages+1):
    url = "http://railscasts.com/?page=%s&type=%s" % (page, video_type)
    data = urllib.urlopen(url).read()
    soup = BeautifulSoup(data)
    
    episode_div = soup.findAll("div", attrs={"class":"main"})
    
    find_links(episode_div, video_type)
  
def find_links(div, video_type):
  for el in div:
    video_name = el.h2.a["href"].replace("/episodes/", "") + video_format
    download(video_name, video_type)

def download(name, video_type):
  print "\n\n%sDownloading %s%s%s" % (colors.BLUE, colors.RESET, video_url, name)
  file_dir = "%s/%s" % (current_dir, video_type)
  if not os.path.exists(file_dir):
    os.makedirs(file_dir)
  urllib.URLopener().retrieve(video_url + name, "%s/%s" % (file_dir, name), reporthook)
  print "%s\nDone!%s" % (colors.GREEN, colors.RESET)

def reporthook(count, block_size, total_size):
  global start_time
  if count == 0:
    start_time = time.time()
    return
  duration = time.time() - start_time
  progress_size = int(count * block_size)
  speed = int(progress_size / (1024 * duration))
  percent = int(count * block_size * 100 / total_size)
  sys.stdout.write("%s\x1b[2K\r...%d%%, %d MB, %d KB/s, %d seconds passed %s" % 
    (colors.ORANGE, percent, progress_size / (1024 * 1024), speed, duration, colors.RESET))
  sys.stdout.flush()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='download railscast episodes')
  
  parser.add_argument('-t', '--type',
    help='type of episodes to download: free, pro or revised')
  
  args = parser.parse_args()
  
  if not len(sys.argv) > 1:
    start(free_pages, "free")
    start(free_pages, "pro")
    start(free_pages, "revised")
  else:
    start(free_pages, "%s" % args.type)
