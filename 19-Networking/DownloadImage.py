import urllib.request

## Download an Image from the web

url = 'https://www.python.org/static/img/python-logo@2x.png'

urllib.request.urlretrieve(url, 'python.png')  # this is how we download an image

# Alternatively:
urllib.request.urlretrieve('https://www.python.org/static/img/python-logo@2x.png', 'python.png')
