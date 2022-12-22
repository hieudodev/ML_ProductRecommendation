import time
import sys
import random
import string

if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str

def crawldatafromistock():
    for i in range(1,21) :
       url = f'https://www.istockphoto.com/vi/search/2/image?phrase=french%20fries&page={i}'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
               img = driver.find_element(By.XPATH,f'/html/body/div[2]/section/div/main/div/div/div[2]/div[2]/div[3]/div[{j}]/article/a/figure/picture/img')
                                           # /html/body/div[2]/section/div/main/div/div/div[2]/div[2]/div[3]/div[60]/article/a/figure/picture/img
               src = img.get_attribute('src')
               name =f'french_fies{i}_{j}.png'
               print(src)
               urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\{name}')
           except :
               print('error')

def crawldatafromamzon():
    for i in range(1,7) :
       url = f'https://www.amazon.com/s?k=Windbreaker+jacket&page={i}&crid=1VGIZ97IYMK1P&qid=1671702913&sprefix=windbreaker+jac%2Caps%2C392&ref=sr_pg_3'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,30):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
                                                #  //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[11]/div/div/div/div/div[1]/span/a/div/img
                                                #  //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[64]/div/div/div/div/div/div/div[1]/span/a/div/img
                                                #  //*[@id="anonCarousel2"]/ol/li[1]/div/div/div/div/div/div[1]/span/a/div/img  
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'Windbreaker{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\WindbreakerJacker\{name}')
           except :
               print('error')

# áo khoác măng tô 
def overcoats_jaceket():
    for i in range(1,7) :
       url = f'https://www.amazon.com/s?k=overcoats+jacket&page={i}&crid=1H1X4UQSB3EYV&qid=1671703773&sprefix=overcoats+jacket%2Caps%2C459&ref=sr_pg_3'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
                                            # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[51]/div/div/div/div/div[1]/span/a/div/img
                                            # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[12]/div/div/div/div/div[1]/span/a/div/img
           
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'overcoats{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\overcoats _jacket\{name}')
           except :
               print('error')


def poncho_jacket():
    for i in range(1,7) :
       url = f'https://www.amazon.com/s?k=poncho+jacket&page={i}&crid=33DN43WQJBU9W&qid=1671705472&sprefix=poncho+jacket%2Caps%2C726&ref=sr_pg_2'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
           
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'poncho{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\poncho_jacket\{name}')
           except :
               print('error')

# quần lửng ống rộng
def Culottes():
    for i in range(1,5) :
       url = f'https://www.amazon.com/s?k=Culottes&page={i}&crid=28SE7BITZB5I7&qid=1671706510&sprefix=culottes%2Caps%2C560&ref=sr_pg_2'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
                                               # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[61]/div/div/div/div/div[1]/span/a/div/img
           
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'culottes{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\Culottes\{name}')
           except :
               print('error')

def Overalls():
    for i in range(1,5) :
       url = f'https://www.amazon.com/s?k=Overalls&page={i}&crid=3W2J783KUTWCQ&qid=1671706809&sprefix=overalls%2Caps%2C467&ref=sr_pg_2'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            
                                               # //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[61]/div/div/div/div/div[1]/span/a/div/img
                                            #    //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[60]/div/div/div/div/div[1]/span/a/div/img
           
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'Overalls{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\Overalls\{name}')
           except :
               print('error')

# quần dài, quần tây
def Trousers():
    for i in range(1,5) :
       url = f'https://www.amazon.com/s?k=Trousers&page={i}&crid=2WGJ1M6NQ1OM9&qid=1671707759&sprefix=trousers+%2Caps%2C354&ref=sr_pg_2'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
           
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'Trousers{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\Trousers\{name}')
           except :
               print('error')
# mũ lưỡi trai
def Baseball_caps():
    for i in range(1,5) :
       url = f'https://www.amazon.com/s?k=Baseball+caps&page={i}&crid=1SJRJG7O21IQ1&qid=1671718380&sprefix=hat%2Caps%2C1076&ref=sr_pg_2'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
                                          #      //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[61]/div/div/div/div/div[1]/span/a/div/img
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'Baseball_caps{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\Baseball_caps\{name}')
           except :
               print('error')

# Giầy cao gót
def highheels():
    for i in range(1,5) :
       url = f'https://www.amazon.com/s?k=high+heels&page={i}&crid=3HA0FVO1AF3DI&qid=1671718750&sprefix=high+heels%2Caps%2C434&ref=sr_pg_2'
       
       driver = webdriver.Chrome(r'D:\Code\Project\ML-LaptopPricePredictor\DataCrawl\driver\chromedriver_win32\chromedriver.exe')
       driver.get(url)
       for j in range(1,61):
           print('start ',j)
           try :
            # try :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
            # except :
            #     img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div/div/div[1]/span/a/div/img')
            img = driver.find_element(By.XPATH,f'//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[{j}]/div/div/div/div/div[1]/span/a/div/img')
                                          #      //*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[61]/div/div/div/div/div[1]/span/a/div/img
            print('img : ',img)
            src = img.get_attribute('src')
            name =f'highheels{i}_{j}.png'
            print(src)
            urlretrieve(src,rf'D:\Code\Project\ML_ProductRecommendation\CrawlData\Images\highheels\{name}')
           except :
               print('error')

if __name__ == '__main__' :
    highheels()
    print('Done!')
    