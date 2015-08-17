#!/usr/bin/env python
__author__ = 'Faianca'

from optparse import OptionParser
from videospider import Spider

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option("-u", "--url", dest="url", help="fetch the result of the url", metavar="URL")

    (options, args) = parser.parse_args()
    if options.url is None:
        raise ValueError('Please add a valid url ex. -u http://google.pt')
    spider = Spider()
    print spider.fetch(options.url)