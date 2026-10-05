import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
from datetime import datetime

def create_bsObj(website_url):
    """Create a beautifulsoup object for the input URL."""
    #Request data from the website
    response = requests.get(website_url)
    status_code = response.status_code #status code attribute
    if status_code == 200:
        #Extract Web Code
        web_data = response.text
        # Create a beautifulsoup object from web data
        bsObj = BeautifulSoup(web_data,"html.parser")
    return bsObj

def create_page_url_list(website_url):
    """ Create Web Page Url lists."""
    # Request data from the website
    main_bsObj = create_bsObj(website_url)

    #Exact Web Page Count
    page_links = main_bsObj.find_all(class_="page-numbers")
    page_numbers = [int(tag.text) for tag in page_links if tag.text.strip().isdigit()]
    page_count = max(page_numbers) if page_numbers else 1
    #print(page_count)

    #Create Web Page urls for each page
    page_url_list = []
    for page_num in range(1, page_count+1):
        page_url = website_url + "?page=" + str(page_num)
        page_url_list.append(page_url)
    return page_url_list

def extract_name(item_tag_var):
    """Extract Product Name from item tag"""
    item_name_tag = item_tag_var.find("h3", class_="wd-entities-title")
    item_name = item_name_tag.text.strip() if item_name_tag else None
    return item_name

def extract_price(item_tag_var):
    """Extract Product Name From Item Tag"""
    item_price_tag = item_tag_var.find("span", class_="woocommerce-Price-amount amount")
    item_price = float(item_price_tag.text.replace(",","").replace("Ks",""))
    return item_price

def extract_link(item_tag_var):
    """Extract Product Link"""
    item_name_tag = item_tag_var.find("h3", class_="wd-entities-title")
    item_link_tag = item_name_tag.find("a") if item_name_tag else None
    item_link = item_link_tag.get("href") if item_link_tag else None
    return item_link

def export_as_excel(name_list, price_list, link_list):
    """Export data as Excel file"""
    df = pd.DataFrame({"Name":name_list,
                       "Price":price_list,
                       "Link":link_list})
    
    current_dt = datetime.now()
    current_dt_format = current_dt.strftime("%Y-%m-%d %H-%M-%S") #Change Date Time format
    #Insert Datetime column
    df["Extracted DateTime"] = current_dt
    
    # Create filename
   
    #Export as excel
    df.to_excel(f"C:\\Users\\htethtet.aung\\Documents\\PythonBasic\\WebDataCollection\\Daily Record Files\\Exported Data {current_dt_format}.xlsx", index=False)
    df.to_excel("Last Update Data.xlsx", index=False)
    print("Product Info are exported as excel file successfully...")
    return None
################################# Main #########################################

# Setup Main Url
my_url = "https://mobilekingmyanmar.com/product-category/apple"

#Create a list for web page url
my_page_url_list = create_page_url_list(my_url)

#Data  Extraction from each page url
item_name_list = []
item_price_list = []
item_link_list = []
for page_url in tqdm(my_page_url_list):
    #Create bs4 object for web page
    page_bsObj = create_bsObj(page_url)
    #Use find all method to search data tags
    item_tags_list = page_bsObj.find_all("div", class_="product-wrapper")
    
    for item_tag in item_tags_list:
                 
        #Extract Name
        item_name = extract_name(item_tag)
        item_name_list.append(item_name)
        
        #Extract Price
        item_price = extract_price(item_tag)
        item_price_list.append(item_price)
                
        #Extract link
        item_link = extract_link(item_tag)
        item_link_list.append(item_link)
        
 #Export as excel
export_as_excel(name_list=item_name_list,
                price_list=item_price_list,
                link_list=item_link_list)


