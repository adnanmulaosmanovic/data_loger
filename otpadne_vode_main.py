import requests
from bs4 import BeautifulSoup
import time, datetime
import otpadne_vode_logger
import os

def count ():
    
    for i in range  (0, 90, 10):
        #print(i)
        print(f"{i} ", end="\r", flush=True)
        time.sleep(10)


def repeat():
    while True:
        os.system('cls')
        print (datetime.datetime.now())
        
        otpadne_vode_logger.datalogger()
        print("----------------------------")
    #    time.sleep(90)
        print("Novo ucitavanje za 90 sekundi:")
        count()




if __name__=="__main__":
    repeat()
    
    
 