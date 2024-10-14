from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cService = webdriver.ChromeService(executable_path='C:\Program Files (x86)\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=cService)
medicine_name = ["Crocin ", "diflucan", "Palbomed 75mg Capsule", "Pan D"]
website_name = ["pharmeasy", "1mg", "netmeds"]

def fetchpharmeasy():
    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)
    input_element = driver.find_element(By.NAME, "q")
    input_element.send_keys(f"{medicine_name[3]}" + " " + "pharmeasy" + Keys.ENTER)
    first_link = driver.find_element(By.CSS_SELECTOR, "div#search a")
    first_link_url = first_link.get_attribute("href")
    driver.get(f"{first_link_url}")

    def findMRP(driver, class_name_mrp, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_mrp))
            )
            return element
        except TimeoutException:
            return None
    
    def findName(driver, class_name_name, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_name))
            )
            return element
        except TimeoutException:
            return None
    
    def findCompanyName(driver, class_name_company_name, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_company_name))
            )
            return element
        except TimeoutException:
            return None
    
    class_names_mrp = [
        "PriceInfo_gcdDiscountContainer__hr0YD",
        "PriceInfo_ourPrice__jFYXr",
        "PriceInfo_striked__Hk2U_",  
    ]
    
    class_names_name = [
        "MedicineOverviewSection_medicineName__dHDQi",
    ]
    
    class_names_company_name = [
        "MedicineOverviewSection_brandName__rJFzE",
    ]
    
    #Company Name
    element_found_company_name = None
    for class_name in class_names_company_name:
        element_found_company_name = findCompanyName(driver, class_name)
        if element_found_company_name:
            break  
    
    if element_found_company_name:
        try:
            element_text = element_found_company_name.text.encode('utf-8').decode('utf-8')
            print("", element_text)
        except UnicodeEncodeError:
            print("", element_text)
    else:
        print("No elements were found.")
    
    #Name
    element_found_name = None
    for class_name in class_names_name:
        element_found_name = findName(driver, class_name)
        if element_found_name:
            break  
    
    if element_found_name:
        try:
            element_text = element_found_name.text.encode('utf-8').decode('utf-8')
            print("", element_text)
        except UnicodeEncodeError:
            print("", element_text)
    else:
        print("No elements were found.")
    
    #Price
    element_found_mrp = None
    for class_name in class_names_mrp:
        element_found_mrp = findMRP(driver, class_name)
        if element_found_mrp:
            break  
    
    if element_found_mrp:
        try:
            element_text = element_found_mrp.text.encode('utf-8').decode('utf-8')
            print("", element_text[1:])
        except UnicodeEncodeError:
            print("", element_text[5:])
    else:
        print("No elements were found.")

def fetch1mg():
    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)
    input_element = driver.find_element(By.NAME, "q")
    input_element.send_keys(f"{medicine_name[3]}" + " " + "1mg" + Keys.ENTER)
    first_link = driver.find_element(By.CSS_SELECTOR, "div#search a")
    first_link_url = first_link.get_attribute("href")
    driver.get(f"{first_link_url}")    

    '''def findMRP(driver, class_name_mrp, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_mrp))
            )
            return element
        except TimeoutException:
            return None'''
    
    def findName(driver, class_name_name, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_name))
            )
            return element
        except TimeoutException:
            return None
    
    def findCompanyName(driver, class_name_company_name, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_company_name))
            )
            return element
        except TimeoutException:
            return None
    
    class_names_mrp = [
        "PriceBoxPlanOption__offer-price___3v9x8 PriceBoxPlanOption__offer-price-cp___2QPU_", 
        "PriceBoxPlanOption__margin-right-4___2aqFt PriceBoxPlanOption__stike___pDQVN",
    ]
    
    class_names_name = [
        "DrugHeader__title-content___2ZaPo",
    ]
    
    class_names_company_name = [
        "DrugHeader__meta-value___vqYM0",
    ]
    
    #Company Name
    element_found_company_name = None
    for class_name in class_names_company_name:
        element_found_company_name = findCompanyName(driver, class_name)
        if element_found_company_name:
            break  
    
    if element_found_company_name:
        try:
            element_text = element_found_company_name.text.encode('utf-8').decode('utf-8')
            print("", element_text)
        except UnicodeEncodeError:
            print("", element_text)
    else:
        print("No elements were found.")
    
    #Name
    element_found_name = None
    for class_name in class_names_name:
        element_found_name = findName(driver, class_name)
        if element_found_name:
            break  
    
    if element_found_name:
        try:
            element_text = element_found_name.text.encode('utf-8').decode('utf-8')
            print("", element_text)
        except UnicodeEncodeError:
            print("", element_text)
    else:
        print("No elements were found.")
    
    #Price
    element_found_mrp = None
    for class_name in class_names_mrp:
        element_found_mrp = driver.find_element(By.XPATH, "//span[contains(@class, 'PriceBoxPlanOption__offer-price___3v9x8')]")
        if element_found_mrp:
            break  
    
    if element_found_mrp:
        try:
            element_text = element_found_mrp.text.encode('utf-8').decode('utf-8')
            print("", element_text[1:])
        except UnicodeEncodeError:
            print("", element_text[5:])
    else:
        print("No elements were found.")

def fetchnetmeds():
    driver.get("https://www.google.com/")
    driver.implicitly_wait(5)
    input_element = driver.find_element(By.NAME, "q")
    input_element.send_keys(f"{medicine_name[3]}" + " " + "netmeds" + Keys.ENTER)
    first_link = driver.find_element(By.CSS_SELECTOR, "div#search a")
    first_link_url = first_link.get_attribute("href")
    driver.get(f"{first_link_url}")    

    def findMRP(driver, class_name_mrp, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_mrp))
            )
            return element
        except TimeoutException:
            return None
    
    def findName(driver, class_name_name, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_name))
            )
            return element
        except TimeoutException:
            return None
    
    def findCompanyName(driver, class_name_company_name, timeout=5):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name_company_name))
            )
            return element
        except TimeoutException:
            return None
    
    class_names_mrp = [
        "final-price", 
    ]
    
    class_names_name = [
        "black-txt",
    ]
    
    class_names_company_name = [
        "drug-manu ellipsis",
    ]
    
    #Company Name
    element_found_company_name = None
    for class_name in class_names_company_name:
        element_found_company_name = findCompanyName(driver, class_name)
        if element_found_company_name:
            break  
    
    if element_found_company_name:
        try:
            element_text = element_found_company_name.text.encode('utf-8').decode('utf-8')
            print("", element_text)
        except UnicodeEncodeError:
            print("", element_text)
    else:
        print("No elements were found.")
    
    #Name
    element_found_name = None
    for class_name in class_names_name:
        element_found_name = findName(driver, class_name)
        if element_found_name:
            break  
    
    if element_found_name:
        try:
            element_text = element_found_name.text.encode('utf-8').decode('utf-8')
            print("", element_text)
        except UnicodeEncodeError:
            print("", element_text)
    else:
        print("No elements were found.")
    
    #Price
    element_found_mrp = None
    for class_name in class_names_mrp:
        element_found_mrp = findMRP(driver, class_name)
        if element_found_mrp:
            break  
    
    if element_found_mrp:
        try:
            element_text = element_found_mrp.text.encode('utf-8').decode('utf-8')
            print("", element_text[1:])
        except UnicodeEncodeError:
            print("", element_text[5:])
    else:
        print("No elements were found.")

fetchpharmeasy()
fetch1mg()
fetchnetmeds()