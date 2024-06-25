"""Find the video in Internet Archive by with name 
show it"""

import sys, webbrowser, requests


def search(title):
    """Fetch a list of tuple, which consist from 3 elements(
        identifier, title, description), that describe videos 
        whose titles partially match the value of the title variable"""
    search_url = "https://archive.org/advancedsearch.php"
    params = {
        'q': 'title:({}) AND mediatype:(movies)'.format(title),
        'fl': 'identifier,title,description',
        'output': 'json',
        'rows': 10,
        'page': 1,
    }
    resp = requests.get(search_url, params=params)
    data = resp.json()
    docs = [(doc['identifier'], doc['title'], doc['description'])
            for doc in data['response']['docs']]
    print(docs)
    return docs

def choose(docs):
    """Output number of string, title and partially description 
    for the each tuple from the list :docs.Let's user choose
    number of string. If it  is correct, we will return the first
    element of a chosen tuple ('identifier'). In the other case,
    return None.
    """
    last = len(docs) - 1
    for num, doc in enumerate(docs):
        print(f"{num}: ({doc[1][:5]}) {doc[2][:10]}...")
    index = input(f"Which would you like to see (0 to {last})? ")
    try:
        return docs[int(index)][1]
    except:
        return None
    
def display(identifier):
    """Display a video from the archive in a browser via the identifier"""
    details_url =  "https://archive.org/details/{}".format(identifier)
    print("Loading", details_url)
    webbrowser.open(details_url)
        
def main(title):
    """Find all films, whose name matches with the value of 
    variable :title. We recognize a choose of the user and
    display it in the browser"""    
    identifiers = search(title)
    if identifiers:
        identifier = choose(identifiers)
        if identifier:
            display(identifier)
        else:
            print('Nothing selected')
    else:
        print("Nothing found for", title)
        
        
if __name__ == "__main__":
    main(sys.argv[1])