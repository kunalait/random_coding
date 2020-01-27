from bs4 import BeautifulSoup
import requests
import pandas as pd
def extract_product_name_and_url():
    product_url=[]
    product_name=[]
    page = requests.get('https://www.stihlusa.com/products/stihl-top-rated-products/')
    soup = BeautifulSoup(page.text, 'html.parser')
    for a in soup.find_all('a', class_='clickable-product-element',href=True):
        product_url.append(a['href'])
        product_name.append(a.text)
    return product_url,product_name

def dump_data_in_csv():
    url,name=extract_product_name_and_url()
    product_url=pd.DataFrame(url,columns=['product url'])
    product_url.to_csv('../output/product_url.csv')
    print 'product url csv file write successfully.'
    #print 'url', url
    #print 'name',name

dump_data_in_csv()

