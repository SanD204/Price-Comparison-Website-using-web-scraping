import requests
from bs4 import BeautifulSoup
#url1 = 'https://rameshwatch.com/products/titan-1639sm01'
#url2 = 'https://watchfactory.in/products/titan-90134wm01-light-leathers-iv-analog-watch-for-men'
#url3 = 'https://www.price-hunt.com/watches/titan-karishma-analog-silver-dial-mens-watch-nl-1775-bm-01.php'

print("                                                                      ")
print("**********************************************************************")

print("1.Iphone")
print("2.Titan Watch")
n = input("What do you want to compare ? ")

match n:
    case "1":
        print("Currently Not Availaible")
        exit(0);
    case "2":
        url1 = 'https://rameshwatch.com/products/titan-1639sm01'
        url2 = 'https://watchfactory.in/products/titan-90134wm01-light-leathers-iv-analog-watch-for-men'
        url3 = 'https://www.price-hunt.com/watches/titan-karishma-analog-silver-dial-mens-watch-nl-1775-bm-01.php'


response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
print("                                                                      ")
print("**********************************************************************")

# Check if the request was successful for 1st site
if response1.status_code == 200:
    # Access the content of the website
    content1 = response1.text
    print("Data Fetched succefully from 1st site")
else:
    print(f"Failed to fetch data. Status code: {response1.status_code}")

soup1 = BeautifulSoup(content1, 'html.parser')
price_elements1 = soup1.find('span', class_='product__price')
price1 = price_elements1.text.strip()
print(f"Price from 1st website: {price1}")

print("**********************************************************************")

# Check if the request was successful for 2nd site
    
if response2.status_code == 200:
    # Access the content of the website
    content2 = response2.text
    print("Data Fetched succefully from 2nd site")
else:
    print(f"Failed to fetch data. Status code: {response2.status_code}")
    
soup2 = BeautifulSoup(content2, 'html.parser')
price_elements2 = soup2.find('span', class_='product__price')
price2 = price_elements2.text.strip()
print(f"Price from 2nd website: {price2}")

print("**********************************************************************")

if response3.status_code == 200:
    # Access the content of the website
    content3 = response3.text
    print("Data Fetched succefully from 3rd site")
else:
    print(f"Failed to fetch data. Status code: {response3.status_code}")

soup3 = BeautifulSoup(content3, 'html.parser')
price_elements3 = soup3.find('span', class_='min_price bold cardo align-middle') 
price3 = price_elements3.text.strip()
print(f"Price from 3rd website: {price3}")

print("**********************************************************************")
print("                                                                      ")

#extracting brand nname
brand_elements1 = soup1.find('div', class_='product-single__vendor')
brand1 = brand_elements1.text.strip()
print(f"Brand : {brand1}")
print("                                                                      ")

if price1<price2 and price1<price3:
    print(f"BEST PRICE : {price1}")
    print("                                                                      ")
    print(url1)
elif price2<price1 and price2<price3:
    print(f"BEST PRICE : {price2}")
    print("                                                                      ")
    print(url2)
elif price3<price1 and price3<price2:
   print(f"BEST PRICE : {price3}")
   print("                                                                      ")
   print(url3)
   
print("                                                                      ")