    from utils.read_json import read_json
from utils.to_text import write_text
import utils.article_scrapper
import re
import logging

def main():
    logging.basicConfig(filename='log_file.log', format = "%(levelname)s - %(asctime)s - %(message)s",level=logging.DEBUG)
    pattern = re.compile(r'(https://)?(www\.)?([a-zA-Z0-9]+)')
    media_urls = read_json()
    try:
        for url in media_urls:
            match = pattern.search(url)
            if match:
                domain = match.group(3)
                scrapper_function = getattr(utils.article_scrapper,domain,None)
                
                if scrapper_function is not None and callable(scrapper_function):
                    headline , paragraph_content , url = scrapper_function(url)
                    write_text(headline , paragraph_content , url)
            logging.info(f"Data scraped successfully for {url}")
            
    except Exception as e:
                logging.error(f"No scrapper function for {domain} defined: {e}")
        
if __name__ == '__main__':
    main()