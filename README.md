# railscast-dl

A python script to download all Railscast episodes including Free, Pro and Revised episodes, since Ryan Bates has now made all episodes open to the public.

The script creates directories inside the directory that the script is run in, named after the episode category - `/free`, `/pro` or `/revised`. 

<div style="text-align:center">
  <img src="https://i.imgur.com/PNN7WtF.png" alt="railscast-dl">
</div>

### Usage

```bash
# Clone the repository
$ git clone https://github.com/lukakerr/railscast-dl.git

# Change directories
$ cd railscast-dl

# Install requirements (BeautifulSoup)
$ pip install -r requirements.txt

# Run the script
$ python dl.py          # Download all episodes
$ python dl.py -t free  # Just download free episodes (can choose from free, pro or revised)
```

### Note

If every single video is downloaded, the script will inevitably take a long time. 

As shown in the screenshot, a progress indicator is shown per video. To get an idea of how long the whole thing would take, multiply the time taken for one video by 417 (total number of videos). 

For example, if one video took 30 seconds to download (at 1.5MB/s in Australia, will probably be faster elsewhere):

```
30 * 417 = 12510 seconds
12510 seconds = 3 hours 28 minutes 30 seconds
```