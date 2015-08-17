__author__ = 'jmeireles'

import requester
import domains


class VideoFetcher:

    fetcher = ''

    def __init__(self, domaininfo):
        """
        :param domaininfo:
        :return:
        """
        self.domain_info = domaininfo
        self.is_valid(domaininfo['domain'])
        module = self.my_import('domains.'+domaininfo['domain'])
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

    def fetch(self):
        """
        load the
        :return:
        """
        pass
        return self.fetcher.fetch(self.domain_info['url'])

