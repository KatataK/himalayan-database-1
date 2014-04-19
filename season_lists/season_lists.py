import requests
import lxml.html

def index_url():
    return 'http://www.himalayandatabase.com/seasonlists.html'

def list_urls(index_url):
    response = requests.get(index_url)
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)
    return html.xpath('//table[position()=5]/descendant::a/@href')

def persons(list_url):
    response = requests.get(list_url)
    # html.xpath('//table/blah/blah')
    raise NotImplementedError('I really need to write a tutorial on XPath.')

for list_url in list_urls(index_url()):
    for person in persons(list_url):
        print(person)
