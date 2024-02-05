import json 
# import glob
import os 

def read_json() -> list:
    
    """
    Read parameters from config file 
    
    Return 
    urls: list
                list containing links of media articles
    """
    config_file_path = os.path.join(os.getcwd(),"input\config.json")
    with open(config_file_path) as fp:
        configs = json.load(fp)
        urls = configs['media_url']
    return urls 