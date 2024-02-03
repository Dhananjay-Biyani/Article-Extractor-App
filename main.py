from utils.read_json import read_json
import os 

def main():
    output_dir = os.getcwd()
    media_urls = read_json()
    for url in media_urls:
        pass