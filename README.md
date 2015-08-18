# Video Spider
Videospider is a spider to fetch video links from famous providers.

### Version
0.1.0
### Installation

```sh
$ git clone https://github.com/Faianca/video-spider.git videospider
$ cd videospider
$ pip install -r "requirements.txt"
$ python setup.py install
```

### Usage Example:
```sh
$ python main.py -u  "http://embed.novamov.com/embed.php?width=600&height=432&v=492730987cf26"
```
#### Video spider as a command
```sh
$ mv main.py /usr/bin/videospider
$ videospider -u "http://embed.novamov.com/embed.php?width=600&height=432&v=492730987cf26"
```
### Dev:
```python
from videospider import Spider
spider = Spider()
print spider.fetch("http://embed.novamov.com/embed.php?width=600&height=432&v=492730987cf26")
```

### Plugins

VideoSpider currently supports this providers.

* easyvideo
* movshare
* novamov
* playbb
* playpand
* videowing
* videozoo
* pornhub
* videoweed
* video44
* arkvid
* mp4upload
* auengine
* videonest
* animeultima
