from utils.read_json import read_json
# from utils.article_scrapper import pressgazette,thehindubusinessline
import utils.article_scrapper
import re
# import os 

def main():
    pattern = re.compile(r'(https://)?(www\.)?([a-zA-Z0-9]+)')
    media_urls = read_json()
    
    for url in media_urls:
        match = pattern.search(url)
        if match:
            domain = match.group(3)
            scrapper_function = getattr(utils.article_scrapper,domain,None)
            
            if scrapper_function is not None and callable(scrapper_function):
                result = scrapper_function()
                print(result)
                
            else:
                print(f"No scrapper function for {domain} defined")
        
if __name__ == '__main__':
    main()