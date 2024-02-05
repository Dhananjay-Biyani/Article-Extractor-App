from utils.read_json import read_json
from utils.to_csv import write_csv
import utils.article_scrapper
import re
import logging
# import os 

def main():
    logging.basicConfig(filename='log_file.log' ,level=logging.INFO, format = " %(levelname)s - %(asctime)s - %(messages)s")
    pattern = re.compile(r'(https://)?(www\.)?([a-zA-Z0-9]+)')
    media_urls = read_json()
    try:
        for url in media_urls:
            match = pattern.search(url)
            if match:
                domain = match.group(3)
                scrapper_function = getattr(utils.article_scrapper,domain,None)
                
                if scrapper_function is not None and callable(scrapper_function):
                    result = scrapper_function(url)
                    write_csv(result)
    except Exception as e:
                logging.info(f"No scrapper function for {domain} defined")
        
if __name__ == '__main__':
    main()