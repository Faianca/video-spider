__author__ = 'jmeireles'

from abc import ABCMeta, abstractmethod


class AbstractFetcher:
    __metaclass__ = ABCMeta

    def __init__(self, requester):
        self.requester = requester

    @abstractmethod
    def fetch(self, url):
        pass