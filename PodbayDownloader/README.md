Podbay Downloader
=================

Podbay provides easy access to thousands of great podcasts, but there is no way to download all of the current content for a show. This tool assists in efficiently downloading such content using an rss feed.

### Setup ###
Prerequisites: Python 2.7 and pip

Install additional required packages: `pip install -r requirements.txt`

### Parameters ###
* `-f`, `--feed` : Url of a rss feed for the show
* `-t`, `--type` : File type of content to be downloaded (default: `audio/mpeg`)
* `-p`, `--path` : Filesystem path to save content to (default: current directory)
* `-n`, `--num` : Number of recent items to download (default: all)

### Sample Usage ###
Download content from [TED Radio Hour](http://podbay.fm/show/523121474) using its [RSS feed](http://podbay.fm/show/523121474).

1. Download all content. `python download.py -f http://www.npr.org/rss/podcast.php?id=510298`
1. Download latest 2 content items. `python download.py -f http://www.npr.org/rss/podcast.php?id=510298 -n 2`
1. Download content to a specific directory. `python download.py -f http://www.npr.org/rss/podcast.php?id=510298 -p /home/ravangen/Music/TED`
