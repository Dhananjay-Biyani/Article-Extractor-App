import csv
import os 
import logging

def write_text(result):
    """
    Creates an output folder and dumps the dictionary data into a csv file 
    
    Parameters
    Result: Dictionary
            Containing scraped data to store in csv
            
    """
    
    logging.basicConfig(filename='log_file.log' , format = " %(levelname)s - %(asctime)s - %(messages)s" ,level=logging.INFO)
    try:
        cwd = os.getcwd()
        folder_name  = 'output'
        folder_path = os.path.join(cwd,folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        file_name = 'scraped_data.txt'
        file_path = os.path.join(folder_path,file_name)
        with open(file_path,'a',encoding="utf-8") as fp:
            for keys ,values in result.items():
                fp.write('%s:%s\n'%(keys,values))
                fp.write(" ")
            
    except Exception as e:
        logging.info(f"Unable to create output file: {e}")