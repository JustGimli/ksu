import requests
from requests.exceptions import Timeout, TooManyRedirects, ConnectionError
from bs4 import BeautifulSoup

def get_links(query="python web dev") -> dict:
    query = query.replace(" ", "+")
    result = []

    URL = f"https://google.com/search?q={query}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    
    try:
        resp = requests.get(URL, headers=headers)
    except  (TooManyRedirects, Timeout, ConnectionError) as e:
        print(e) # raise connection handler as e:
    
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "lxml")
        

        for g in soup.find_all("div",class_="yuRUbf"):
            item = {
                "title": g.a.h3.text,
                "link": g.a.get("href") 
            }
            result.append(item)
        
        return result
    else:
        result = {
            "title": "Unknown error",
            "link": "None"
        }
        return result

