"""main application file, possibly the only application file. python 3.11.4"""

import urllib3
import xmltodict

FEED = "https://rpilocator.com/feed/"

def getfeed():
    """gets xml feed and converts it into a dict"""
    http = urllib3.PoolManager()
    response = http.request('GET', FEED)
    print(response.read().decode('utf-8'))
    xmldict = xmltodict.parse(response.read())
    return xmldict

def main():
    """main logic"""
    xml = getfeed()
    for i,k in xml:
        print(i + ': ' + k)

if __name__ == "__main__":
    main()

