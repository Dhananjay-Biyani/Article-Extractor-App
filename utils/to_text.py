import csv
import os 
import logging

def write_text(headline , paragraph_content , url):
    """
    Creates an output folder and dumps the dictionary data into a csv file 
    
    Parameters
    Result: Dictionary
            Containing scraped data to store in csv
            
    """
    
    logging.basicConfig(filename='log_file.log' , format = " %(levelname)s - %(asctime)s - %(messages)s" ,level=logging.DEBUG)
    try:
        cwd = os.getcwd()
        folder_name  = 'output'
        folder_path = os.path.join(cwd,folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            
        file_name = 'scraped_data.txt'
        file_path = os.path.join(folder_path,file_name)
        with open(file_path,'w',encoding="UTF-8") as fp:
            # for keys ,values in result.items():
            #     fp.write('%s:%s\n'%(keys,values))
            #     fp.write(" ")
            fp.write(f"News Headline: {headline}""\n")
            fp.write(f"Conetnt: {paragraph_content}""\n")
            fp.write(f"News Link: {url}""\n")
            fp.write("--------------------------------------------------------------------------------------------\n")
            
        logging.info("Output stored successfully in scrapped_data.txt file ")
            
    except Exception as e:
        logging.error(f"Unable to create output file: {e}")