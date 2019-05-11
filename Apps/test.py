from Apps.mathematicians_scrapper import simple_get
from bs4 import BeautifulSoup

def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician.
    """
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        # set() function ensures that we will not end up with duplicate names
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name > 0):
                    names.append(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

def get_hits_on_name(name):
    """
    Accepts a name of a mathematician and returns the number of hits
    that mathematician's Wikipedia page received in the last 60 days, as an int
    """
