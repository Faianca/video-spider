#!/usr/bin/env python
__author__ = 'Faianca'

from src.videoFetcher import VideoFetcher
from optparse import OptionParser
from rfc3987 import parse
import re


def fetch(url):
    # Validate URL
    d = parse(url, rule='IRI')
    li = d['authority'].split('.')
    domain = li[len(li) - 2]
    domainInfo = {'domain': domain, 'url': url}

    videoFetcher = VideoFetcher(domainInfo)
    url = videoFetcher.fetch()
    return url


if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="fetch the result of the url", metavar="URL")

    (options, args) = parser.parse_args()
    if options.url is None:
        raise ValueError('Please add a valid url ex. -u http://google.pt')

    print fetch(options.url)