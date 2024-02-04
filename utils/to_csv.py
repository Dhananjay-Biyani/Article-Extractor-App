import csv
import os 

def write_csv(result):
    cwd = os.getcwd()
    folder_name  = 'output'
    folder_path = os.path.join(cwd,folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    file_name = 'scraped_data.csv'
    file_path = os.path.join(folder_path,file_name)
    keys = list(result.keys())
    with open(file_path,'a',encoding="utf-8") as fp:
        write = csv.DictWriter(fp,fieldnames=keys)
        write.writeheader()
        write.writerow(result)
    