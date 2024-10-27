from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import json

app = Flask(__name__)

cService = ChromeService(executable_path='C:/Program Files (x86)/chromedriver-win64/chromedriver.exe')

def get_driver():
    """Helper to initialize the Chrome driver with headless option."""
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        options.add_argument('--no-sandbox')  # Recommended for running in some environments
        options.add_argument('--disable-dev-shm-usage')  # Avoid issues with shared memory in Docker
        options.add_argument('--disable-gpu')  # Disable GPU acceleration, useful for headless mode
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-popup-blocking')
        options.add_argument("--disable-javascript")
        # Initialize the driver with the options and service
        return webdriver.Chrome(service=cService, options=options)
    except WebDriverException as e:
        print(f"WebDriver initialization failed: {e}")
        return None

medicine_name = ["Crocin", "diflucan", "Palbomed 75mg Capsule", "Pan D"]

def fetchpharmeasy():
    driver = get_driver()
    if not driver:
        return {"error": "Failed to initialize WebDriver for Pharmeasy"}

    try:
        driver.get("https://www.google.com/")
        driver.implicitly_wait(5)
        input_element = driver.find_element(By.NAME, "q")
        input_element.send_keys(f"{medicine_name[3]}" + " " + "pharmeasy" + Keys.ENTER)
        first_link = driver.find_element(By.CSS_SELECTOR, "div#search a")
        first_link_url = first_link.get_attribute("href")
        driver.get(first_link_url)

        def find_element(driver, class_name, timeout=5):
            """Helper to find elements by class name."""
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.CLASS_NAME, class_name))
                )
                return element
            except TimeoutException:
                return None

        class_names_mrp = [
            "PriceInfo_gcdDiscountContainer__hr0YD",
            "PriceInfo_ourPrice__jFYXr",
            "PriceInfo_striked__Hk2U_",  
        ]
        class_names_name = ["MedicineOverviewSection_medicineName__dHDQi"]
        class_names_company_name = ["MedicineOverviewSection_brandName__rJFzE"]

        company_name_element = None
        for class_name in class_names_company_name:
            company_name_element = find_element(driver, class_name)
            if company_name_element:
                break

        company_name = company_name_element.text if company_name_element else "Not Found"

        name_element = None
        for class_name in class_names_name:
            name_element = find_element(driver, class_name)
            if name_element:
                break

        name = name_element.text if name_element else "Not Found"

        price_element = None
        for class_name in class_names_mrp:
            price_element = find_element(driver, class_name)
            if price_element:
                break

        price = price_element.text[1:] if price_element else "Not Found"

    except Exception as e:
        print(f"Error in Pharmeasy fetch: {e}")
        return {"error": f"Failed to fetch Pharmeasy: {str(e)}"}

    finally:
        driver.quit()

    return {
        "website": "Pharmeasy",
        "medicine_name": name,
        "company_name": company_name,
        "price": price
    }

def fetch1mg():
    driver = get_driver()
    if not driver:
        return {"error": "Failed to initialize WebDriver for 1mg"}

    try:
        driver.get("https://www.google.com/")
        driver.implicitly_wait(5)
        input_element = driver.find_element(By.NAME, "q")
        input_element.send_keys(f"{medicine_name[3]}" + " " + "1mg" + Keys.ENTER)
        first_link = driver.find_element(By.CSS_SELECTOR, "div#search a")
        first_link_url = first_link.get_attribute("href")
        driver.get(first_link_url)

        def find_element(driver, class_name, timeout=5):
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.CLASS_NAME, class_name))
                )
                return element
            except TimeoutException:
                return None

        class_names_mrp = ["PriceBoxPlanOption__offer-price___3v9x8"]
        class_names_name = ["DrugHeader__title-content___2ZaPo"]
        class_names_company_name = ["DrugHeader__meta-value___vqYM0"]

        company_name_element = None
        for class_name in class_names_company_name:
            company_name_element = find_element(driver, class_name)
            if company_name_element:
                break

        company_name = company_name_element.text if company_name_element else "Not Found"

        name_element = None
        for class_name in class_names_name:
            name_element = find_element(driver, class_name)
            if name_element:
                break

        name = name_element.text if name_element else "Not Found"

        price_element = None
        for class_name in class_names_mrp:
            price_element = find_element(driver, class_name)
            if price_element:
                break

        price = price_element.text[1:] if price_element else "Not Found"

    except Exception as e:
        print(f"Error in 1mg fetch: {e}")
        return {"error": f"Failed to fetch 1mg: {str(e)}"}

    finally:
        driver.quit()

    return {
        "website": "1mg",
        "medicine_name": name,
        "company_name": company_name,
        "price": price
    }

def fetchnetmeds():
    driver = get_driver()
    if not driver:
        return {"error": "Failed to initialize WebDriver for Netmeds"}

    try:
        driver.get("https://www.google.com/")
        driver.implicitly_wait(5)
        input_element = driver.find_element(By.NAME, "q")
        input_element.send_keys(f"{medicine_name[3]}" + " " + "netmeds" + Keys.ENTER)
        first_link = driver.find_element(By.CSS_SELECTOR, "div#search a")
        first_link_url = first_link.get_attribute("href")
        driver.get(first_link_url)

        def find_element(driver, class_name, timeout=5):
            try:
                element = WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((By.CLASS_NAME, class_name))
                )
                return element
            except TimeoutException:
                return None

        class_names_mrp = ["final-price"]
        class_names_name = ["black-txt"]
        class_names_company_name = ["drug-manu ellipsis"]

        company_name_element = None
        for class_name in class_names_company_name:
            company_name_element = find_element(driver, class_name)
            if company_name_element:
                break

        company_name = company_name_element.text if company_name_element else "Not Found"

        name_element = None
        for class_name in class_names_name:
            name_element = find_element(driver, class_name)
            if name_element:
                break

        name = name_element.text if name_element else "Not Found"

        price_element = None
        for class_name in class_names_mrp:
            price_element = find_element(driver, class_name)
            if price_element:
                break

        price = price_element.text[5:] if price_element else "Not Found"

    except Exception as e:
        print(f"Error in Netmeds fetch: {e}")
        return {"error": f"Failed to fetch Netmeds: {str(e)}"}

    finally:
        driver.quit()

    return {
        "website": "Netmeds",
        "medicine_name": name,
        "company_name": company_name,
        "price": price
    }

@app.route('/get_medicine_data', methods=['GET'])
def get_medicine_data():
    results = []
    results.append(fetchpharmeasy())
    results.append(fetch1mg())
    results.append(fetchnetmeds())
    
    return jsonify({"data": results})

if __name__ == '__main__':
    app.run(debug=True)
