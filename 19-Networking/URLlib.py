import urllib.request


## Open and read a webpage

try :
    
    url= urllib.request.urlopen('https://python.org/')
    content = url.read()   # read the page and store it in this variable
    url.close()  # we no longer need the url once read.
    
except urllib.error.HTTPError:   # handle exception if url not found.
    print('Wepbage not found.')
    exit()


f = open('python.html','wb')
f.write(content)
f.close()