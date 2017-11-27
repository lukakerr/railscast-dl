from BeautifulSoup import BeautifulSoup
import urllib
import time
import sys
import os

current_dir = os.getcwd()

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

def start(pagination_length, video_type):
  for page in range(1, pagination_length+1):
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
  print "\n\n" + colors.BLUE + "Downloading " + colors.RESET + video_url + name
  file_dir = "%s/%s" % (current_dir, video_type)
  if not os.path.exists(file_dir):
    os.makedirs(file_dir)
  urllib.URLopener().retrieve(video_url + name, file_dir + "/" + name, reporthook)
  print colors.GREEN + "\nDone!" + colors.RESET

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
  start(free_pages, "free")
  start(pro_pages, "pro")
  start(revised_pages, "revised")
