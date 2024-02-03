import json 

def read_json():
    
    """
    Read parameters from config file 
    
    Return 
    media_urls: list
                      list containing links of media articles
    """
    with open(r'D:\Python assignments\Assignment_3\Article-Extractor-App\input\config.json') as fp:
        configs = json.load(fp)
        urls = configs['media_url']
    return urls 