from bs4 import BeautifulSoup
import requests

def pressgazette(url):
    """

    """
    paragraph_content = []
    # url ="https://pressgazette.co.uk/media-audience-and-business-data/media_metrics/most-popular-websites-news-world-monthly-2/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
    response = requests.get(url,headers=headers)
    html_text = response.text
    soup = BeautifulSoup(html_text , 'lxml')
    headline = soup.find_all('h1',class_ = 'c-article-header__title')[0].text
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
            paragraph_content.append(paragraph.text.replace("\n",""))
    return {'Headline': headline , 'Text': paragraph_content }
    
def thehindubusinessline(url):
    """
    
    """
    paragraph_content = []
    # url = "https://www.thehindubusinessline.com/multimedia/audio/what-is-the-economics-behind-marathons/article67803923.ece"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
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
    