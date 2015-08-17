__author__ = 'jmeireles'

import requester
import domains
from rfc3987 import parse


class Spider:

    fetcher = ''

    def __init__(self):
        pass

    def build_domain(self, url):
        """
        :param domaininfo:
        :return:
        """
        d = parse(url, rule='IRI')
        li = d['authority'].split('.')
        domain = li[len(li) - 2]
        self.is_valid(domain)
        module = self.my_import('domains.'+domain)
        self.fetcher = module.Fetcher(requester.Requester())

    def my_import(self, name):
        mod = __import__(name, globals=globals())
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    def is_valid(self, domain):
        """
        Check if we have this domain plugin
        :param domain:
        """
        if domain not in domains.__all__:
            raise ValueError("Fetcher does not support this domain")

    def fetch(self, url):
        """
        load the
        :return:
        """
        self.build_domain(url)
        return self.fetcher.fetch(url)

