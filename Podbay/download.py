import os
import string
import sys
import urllib
import urlparse

import argparse
import feedparser


VALID_FILENAME_CHARS = "-_.() %s%s" % (string.ascii_letters, string.digits)


def print_error(message):
    sys.stderr.write(message)
    sys.stderr.flush()


def parse_args():
    parser = argparse.ArgumentParser(description='Download all media files from a show.')
    parser.add_argument('-f', '--feed', dest='feed', help='RSS feed of podcast')
    parser.add_argument('-n', '--num', dest='num', help='Number of recent items to download')
    parser.add_argument('-p', '--path', dest='path', default=os.getcwd(), help='Filesystem path to save content')
    parser.add_argument('-t', '--type', dest='type', default='audio/mpeg', help='File type to be downloaded')

    args = parser.parse_args()
    return args.feed, args.num, args.type, args.path


def get_urls_from_links(links, type):
    urls = []
    for link in links:
        if link.get('type') == type:
            urls.append(link.get('url'))
    return urls


def get_directory_name(unsafe_name):
    directory = ''.join(c for c in unsafe_name.strip() if c in VALID_FILENAME_CHARS)
    directory = directory.replace('..', '').lstrip('.')
    return directory


def get_file_name(url):
    path = urlparse.urlsplit(url).path
    return path.split('/')[-1]


def download_item(feed_data, type, base_dir):
    title = feed_data.get('title')

    directory = os.path.join(base_dir, get_directory_name(title))
    if not os.path.exists(directory):
        os.makedirs(directory)
    print('Downloading to \'{}\''.format(directory))

    urls = get_urls_from_links(feed_data.get('links', []), type)
    for url in urls:
        try:
            destination = os.path.join(directory, get_file_name(url))
            if os.path.exists(destination):
                print('File already exists \'{}\''.format(destination))
                continue

            urllib.urlretrieve(url, destination)
        except Exception:
            print_error('Failed to download \'{}\''.format(url))


def download_from_feed(feed, type, path=None, max_count=None):
    """Save a media item to the file system.

    Keyword arguments:
    feed -- url of an rss feed
    type -- file type of content to be downloaded
    path -- directory to save content to (default: current directory)
    max_count -- how many recent items from feed should be downloaded (default: all)
    """
    directory = path or os.getcwd()
    if not os.path.isdir(directory):
        raise Exception('Path \'{}\' is not a directory'.format(directory))

    try:
        f = feedparser.parse(feed)
    except Exception:
        print_error('Failed to parse feed: {}'.format(feed))
    else:
        max_count = max_count or sys.maxint
        for index, item in enumerate(f['items']):
            if index >= max_count:
                return

            download_item(item, type, directory)


if __name__ == "__main__":
    feed, max_count, type, path = parse_args()
    download_from_feed(feed, type, path, max_count)
