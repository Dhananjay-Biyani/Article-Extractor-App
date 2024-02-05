import json 
import os 
import logging

def read_json() -> list:
    
    """
    Read parameters from config file 
    
    Return 
    urls: list
                list containing links of media articles
    """
    
    logging.basicConfig(filename='log_file.log' ,level=logging.INFO, format = " %(levelname)s - %(asctime)s - %(messages)s")
    try:
        config_file_path = os.path.join(os.getcwd(),"input\config.json")
        with open(config_file_path) as fp:
            configs = json.load(fp)
            urls = configs['media_url']
        return urls 
    
    except Exception as e:
        logging.info(f"Unable to read config file :{e}")