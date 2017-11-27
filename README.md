# railscast-dl

A python script to download all railscast episodes including Free, Pro and Revised episodes, since Ryan Bates has now made all episodes open to the public.

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
$ python dl.py
```

### Note

Since the script downloads every video (over 400), the script will inevitably take a long time. 

As shown in the screenshot, a progress indicator is shown per video. To get an idea of how long the whole thing should take, simply multiply the time taken for one video by 417 (total number of videos). 

For example, if one video took 30 seconds to download:

```
30 * 417 = 12510 seconds
12510 seconds = 3 hours 28 minutes 30 seconds
```