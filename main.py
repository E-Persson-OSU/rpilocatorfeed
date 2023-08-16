"""main application file, possibly the only application file. python 3.11.4"""

from urllib3 import PoolManager
import xmltodict



FEED = "https://rpilocator.com/feed/"

def getfeed():
    """gets web feed and converts it into a list"""
    # proxy = FreeProxy(country_id=['US'], rand=True, anonym=True).get()
    # http = ProxyManager(proxy_url=proxy, headers=make_urllib_header())
    http = PoolManager()
    response = http.request('GET', FEED)
    return response.data.decode('utf-8')

def getitems(response):
    """convert response to list of dicts containing information from the items"""
    xml = xmltodict.parse(response)
    listofdicts = xml['rss']['channel']['item']
    return listofdicts

def main():
    """main logic"""
    resp = getfeed()
    getitems(response=resp)
    

if __name__ == "__main__":
    main()
