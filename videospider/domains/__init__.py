__title__ = 'videoSpider'
__author__ = 'Jorge Faianca'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2015 Jorge Faianca'

import os
import glob

all_list = list()
for f in glob.glob(os.path.dirname(__file__)+"/*.py"):
    if os.path.isfile(f) and not os.path.basename(f).startswith('_'):
        all_list.append(os.path.basename(f)[:-3])

__all__ = all_list