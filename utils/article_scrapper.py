from bs4 import BeautifulSoup
import requests
import logging

def pressgazette(url) -> dict:
    """
    Takes url as a parameter and extracts news headline and text content
    
    Parameters
    url: String
         news article url to scrape data 
         
    Returns
    Dictionary: containing headline and text content 

    """
    logging.basicConfig(filename='log_file.log' ,level=logging.INFO, format = " %(levelname)s - %(asctime)s - %(messages)s")
    paragraph_content = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    try:    
        response = requests.get(url,headers=headers)
        html_text = response.text
        soup = BeautifulSoup(html_text , 'lxml')
        headline = soup.find_all('h1',class_ = 'c-article-header__title')[0].text
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
                paragraph_content.append(paragraph.text.replace("\n",""))
        return {'Headline': headline , 'Text': paragraph_content }
    
    except Exception as  e:
        logging.info(f"Unable to fetch data for pressgazette {e}")
        

    
def thehindubusinessline(url) -> dict:
    """
    Takes url as a parameter and extracts news headline and text content
    
    Parameters
    url: String
         news article url to scrape data 
         
    Returns
    Dictionary: containing headline and text content
    
    """
    logging.basicConfig(filename='log_file.log' ,level=logging.INFO, format = " %(levelname)s - %(asctime)s - %(messages)s")
    paragraph_content = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    try:    
        response = requests.get(url,headers=headers)
        html_text = response.text
        soup = BeautifulSoup(html_text,'lxml')
        headline = soup.find_all('h1')[0].text
        bold_text = soup.find_all('h2',class_ = 'bl-sub-text')[0].text
        paragraph_content.append(bold_text.replace("\xa0", ""))
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            paragraph_content.append(paragraph.text.replace("\xa0", ""))  
        return {'Headline': headline ,'Text': paragraph_content}
    
    except Exception as e:
        logging.info(f"Unable to fetch data for thehindubusinessline: {e}")