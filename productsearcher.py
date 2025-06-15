from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas
import datetime
from slugify import slugify





def search_product(product_name: str):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://mercadolivre.com.br/")
        driver.find_element(By.ID, "cb1-edit").click()
        driver.find_element(By.ID, "cb1-edit").send_keys(product_name)
        driver.find_element(By.ID,  "cb1-edit").send_keys(Keys.RETURN)
    except Exception as e:
        return {"error": f"something went wrong looking for search bar: {e}"}

    try:
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".ui-search-layout.ui-search-layout--grid > .ui-search-layout__item")
    except Exception as e:
        return {"error": f"something went wrong looking for product cards: {e}"}
    
    product_names:list[str] = []
    product_prices:list[str] = []

    for card in product_cards:
        try:
            product_name_result = card.find_element(By.CLASS_NAME, "poly-component__title").text
            price_fraction = card.find_element(By.CLASS_NAME, "andes-money-amount__fraction").text
            price_cents = card.find_element(By.CLASS_NAME, "andes-money-amount__cents").text
            product_price = f"R${price_fraction}, {price_cents}"

            product_names.append(product_name_result)
            product_prices.append(product_price)
        except Exception as e:
            continue
    driver.quit()
    data = {
        "Product": product_names,
        "Price": product_prices
    }

    today_date = datetime.date.today()
    dataframe = pandas.DataFrame(data)
    dataframe.to_excel(f"{slugify(product_name)}-price-research-{today_date}.xlsx")
    

    return {"message": "done!"}
