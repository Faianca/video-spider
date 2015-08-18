__title__ = 'videoSpider'
__author__ = 'Jorge Faianca'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2015 Jorge Faianca'

import bs4
import requests
import dryscrape
import urlparse
from urllib import urlencode, quote, unquote
import gzip
import re
import StringIO

IE_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
FF_USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
IOS_USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25'
ANDROID_USER_AGENT = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'


class Requester:
    def __init__(self):
        pass

    def send(self, url):
        return requests.get(url)

    def get(self, url, pageLoad=False, headers={}):
        """
        Get with javascript loaded
        :param url:
        :param pageLoad:
        :return:
        """
        if pageLoad:
            session = dryscrape.Session()
            session.set_header('User-Agent', ANDROID_USER_AGENT)
            session.visit(url)
            response = session.body()
        else:
            response = requests.get(url, headers=headers)

        return bs4.BeautifulSoup(response.text)


    @staticmethod
    def build_url(url, params):
        url_parts = list(urlparse.urlparse(url))

        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)

        url_parts[4] = urlencode(query)
        url = urlparse.urlunparse(url_parts)

        return url


class HttpResponse:
    '''
    This class represents a resoponse from an HTTP request.

    The content is examined and every attempt is made to properly encode it to
    Unicode.

    .. seealso::
        :meth:`Net.http_GET`, :meth:`Net.http_HEAD` and :meth:`Net.http_POST`
    '''

    content = ''
    '''Unicode encoded string containing the body of the reposne.'''


    def __init__(self, response):
        '''
        Args:
            response (:class:`mimetools.Message`): The object returned by a call
            to :func:`urllib2.urlopen`.
        '''
        encoding = ''
        self._response = response
        html = response.read()
        try:
            if response.headers['content-encoding'].lower() == 'gzip':
                html = gzip.GzipFile(fileobj=StringIO.StringIO(html)).read()
        except:
            pass

        try:
            content_type = response.headers['content-type']
            if 'charset=' in content_type:
                encoding = content_type.split('charset=')[-1]
        except:
            pass

        r = re.search('<meta\s+http-equiv="Content-Type"\s+content="(?:.+?);' +
                      '\s+charset=(.+?)"', html, re.IGNORECASE)
        if r:
            encoding = r.group(1)

        try:
            html = unicode(html, encoding)
        except:
            pass

        self.content = html


    def get_headers(self):
        '''Returns a List of headers returned by the server.'''
        return self._response.info().headers



    def get_url(self):
        '''
        Return the URL of the resource retrieved, commonly used to determine if
        a redirect was followed.
        '''
        return self._response.geturl()
