import requests
from bs4 import BeautifulSoup
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YourPasss",
    database="project_database"
)

print("                                                                      ")
print("*******************************************************************************************************************************************************")
print("                                                                      ")

print("1.Titan Watch")
print("2.Victus Laptop")
print("3.Boat Airdropes")
print("4.exit")
n = input("What do you want to compare ? ")
print("                                                                      ")
print("*******************************************************************************************************************************************************")
print("                                                                      ")
match n:
    case "1":
        cursor1 = db.cursor()
        cursor1.execute("SELECT urls FROM product_info_table WHERE product_id = 'watch1' ")
        data1 = cursor1.fetchone()
        url1 = data1[0]

        class_type_cursor1 = db.cursor()
        class_type_cursor1.execute("SELECT class_type FROM product_info_table WHERE product_id = 'watch1' ")
        class_type_data1 = class_type_cursor1.fetchone()
        class_type1 = class_type_data1[0]

        class_name_cursor1 = db.cursor()
        class_name_cursor1.execute("SELECT class_name FROM product_info_table WHERE product_id = 'watch1' ")
        class_name_data1 = class_name_cursor1.fetchone()
        class_name1 = class_name_data1[0]

        cursor2 = db.cursor()
        cursor2.execute("SELECT urls FROM product_info_table WHERE product_id = 'watch2' ")
        data2 = cursor2.fetchone()
        url2 = data2[0]

        class_type_cursor2 = db.cursor()
        class_type_cursor2.execute("SELECT class_type FROM product_info_table WHERE product_id = 'watch2' ")
        class_type_data2 = class_type_cursor2.fetchone()
        class_type2 = class_type_data2[0]

        class_name_cursor2 = db.cursor()
        class_name_cursor2.execute("SELECT class_name FROM product_info_table WHERE product_id = 'watch2' ")
        class_name_data2 = class_name_cursor2.fetchone()
        class_name2 = class_name_data2[0]
        print("BRAND: TITAN")
        print("1639SM01")
        print("Silver Dial Silver Stainless Steel Strap Watch")
        print("GENDER: Men")
        print("MOVEMENT: Quartz")
        print("COLLECTION: KARISHMA")
        print("FUNCTION: Analog")
        print("CASE MATERIAL: Metal")
        print("STRAP MATERIAL: Stainless Steel")
        print("CASE SHAPE: Round")
        print("DIAL COLOR: Silver")
        print("WARRANTY PERIOD: 24 Months")
        print("WARRANTY DETAILS: This watch offers 24 months warranty on the Movement and 12 months warranty on the Battery from the date of purchase.")
    case "2":
        cursor1 = db.cursor()
        cursor1.execute("SELECT urls FROM product_info_table WHERE product_id = 'laptop1' ")
        data1 = cursor1.fetchone()
        url1 = data1[0]

        class_type_cursor1 = db.cursor()
        class_type_cursor1.execute("SELECT class_type FROM product_info_table WHERE product_id = 'laptop1' ")
        class_type_data1 = class_type_cursor1.fetchone()
        class_type1 = class_type_data1[0]

        class_name_cursor1 = db.cursor()
        class_name_cursor1.execute("SELECT class_name FROM product_info_table WHERE product_id = 'laptop1' ")
        class_name_data1 = class_name_cursor1.fetchone()
        class_name1 = class_name_data1[0]

        cursor2 = db.cursor()
        cursor2.execute("SELECT urls FROM product_info_table WHERE product_id = 'laptop2' ")
        data2 = cursor2.fetchone()
        url2 = data2[0]

        class_type_cursor2 = db.cursor()
        class_type_cursor2.execute("SELECT class_type FROM product_info_table WHERE product_id = 'laptop2' ")
        class_type_data2 = class_type_cursor2.fetchone()
        class_type2 = class_type_data2[0]

        class_name_cursor2 = db.cursor()
        class_name_cursor2.execute("SELECT class_name FROM product_info_table WHERE product_id = 'laptop2' ")
        class_name_data2 = class_name_cursor2.fetchone()
        class_name2 = class_name_data2[0]
        print("HP Victus Gaming Laptop 39.62 cm 15-fb0147AX")
        print("AMD Ryzen™ 5 processor")
        print("Windows 11 Home Single Language")
        print("39.6 cm (15.6) diagonal FHD display")
        print("AMD Radeon™ RX 6500M Graphics")
        print("512 GB PCIe® NVMe™ SSD Hard drive")
        print("8 GB RAM DDR4")
        print("Backlit keyboard with numeric keypad/Wide Vision 720p HD camera/B&O Speakers")
    case "3":
        cursor1 = db.cursor()
        cursor1.execute("SELECT urls FROM product_info_table WHERE product_id = 'boatairdropes1' ")
        data1 = cursor1.fetchone()
        url1 = data1[0]

        class_type_cursor1 = db.cursor()
        class_type_cursor1.execute("SELECT class_type FROM product_info_table WHERE product_id = 'boatairdropes1' ")
        class_type_data1 = class_type_cursor1.fetchone()
        class_type1 = class_type_data1[0]

        class_name_cursor1 = db.cursor()
        class_name_cursor1.execute("SELECT class_name FROM product_info_table WHERE product_id = 'boatairdropes1' ")
        class_name_data1 = class_name_cursor1.fetchone()
        class_name1 = class_name_data1[0]

        cursor2 = db.cursor()
        cursor2.execute("SELECT urls FROM product_info_table WHERE product_id = 'boatairdropes2' ")
        data2 = cursor2.fetchone()
        url2 = data2[0]

        class_type_cursor2 = db.cursor()
        class_type_cursor2.execute("SELECT class_type FROM product_info_table WHERE product_id = 'boatairdropes2' ")
        class_type_data2 = class_type_cursor2.fetchone()
        class_type2 = class_type_data2[0]

        class_name_cursor2 = db.cursor()
        class_name_cursor2.execute("SELECT class_name FROM product_info_table WHERE product_id = 'boatairdropes2' ")
        class_name_data2 = class_name_cursor2.fetchone()
        class_name2 = class_name_data2[0]
        print("boAt Airdopes 121v2 On Ear True Wireless (TWS)")
        print("14 Hours Playback")
        print("IPX7 Water Resistant")
        print("Active Noise cancellation")
        print("IPX7 Water Resistant")
        print("Bluetooth V 5.0 Black")
        print("COLOR: Black")
        print("BIS/ISI License number:R - 41171557")
    case "4":
        exit(0);


response1 = requests.get(url1)
response2 = requests.get(url2)
print("                                                                      ")
print("*******************************************************************************************************************************************************")
print("                                                                      ")

if response1.status_code == 200:
    # Access the content of the website
    content1 = response1.text
    print("Data Fetched succefully from 1st site")
else:
    print(f"Failed to fetch data. Status code: {response1.status_code}")

soup1 = BeautifulSoup(content1, 'html.parser')
price_elements1 = soup1.find(class_type1, class_=class_name1)
price1 = price_elements1.text.strip()
print(f"Price from 1st website: {price1}")

print("                                                                      ")
print("*******************************************************************************************************************************************************")
print("                                                                      ")

    
if response2.status_code == 200:
    # Access the content of the website
    content2 = response2.text
    print("Data Fetched succefully from 2nd site")
else:
    print(f"Failed to fetch data. Status code: {response2.status_code}")
    
soup2 = BeautifulSoup(content2, 'html.parser')
price_elements2 = soup2.find(class_type2, class_=class_name2)
price2 = price_elements2.text.strip()
print(f"Price from 2nd website: {price2}")

print("                                                                      ")
print("*******************************************************************************************************************************************************")
print("                                                                      ")

print("Price from website-1:")
print(price1)
print("                                                                      ")
print("URL of website-1:")
print(url1)

print("                                                                      ")
print("*******************************************************************************************************************************************************")
print("                                                                      ")

print("Price from website-2:")
print(price2)
print("                                                                      ")
print("URL of website-2:")
print(url2)
print("                                                                      ")
print("*******************************************************************************************************************************************************")
