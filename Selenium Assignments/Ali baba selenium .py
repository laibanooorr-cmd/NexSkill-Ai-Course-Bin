from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
import time


# ==========================================
# Chrome Setup
# ==========================================

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")

driver = webdriver.Chrome(options=options)

driver.set_page_load_timeout(60)

wait = WebDriverWait(driver, 30)


# ==========================================
# Alibaba URL
# ==========================================

url = "https://www.alibaba.com/trade/search?SearchText=Auto+Accessories"

print("Opening Alibaba...")

try:
    driver.get(url)
except TimeoutException:
    print("Page loading timeout. Continuing...")


# ==========================================
# Wait for page
# ==========================================

time.sleep(5)


# ==========================================
# Scroll to load products
# ==========================================

print("Scrolling page...")

for i in range(8):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(3)

print("Scrolling completed.")


# ==========================================
# Find Product Cards
# ==========================================

selectors = [

    # Old Alibaba selector
    "div.fy26-product-card-wrapper",

    # Product card
    "div.searchx-offer-item",

    # Product item
    "div[class*='product-card']",

    # Search result item
    "div[class*='searchx-product']",

]


products = []


for selector in selectors:

    try:

        products = driver.find_elements(
            By.CSS_SELECTOR,
            selector
        )

        print(
            f"Selector: {selector} --> {len(products)} products"
        )

        if len(products) > 0:
            break

    except Exception as e:

        print("Selector error:", e)


print("\nTotal Products Found:", len(products))


# ==========================================
# Extract Data
# ==========================================

data = []


for product in products:

    item = {}

    # --------------------------------------
    # TITLE
    # --------------------------------------

    title_selectors = [
        "h2 a",
        "h2",
        "a[class*='title']",
        "a[class*='product']"
    ]

    title = "NA"

    for selector in title_selectors:

        try:

            element = product.find_element(
                By.CSS_SELECTOR,
                selector
            )

            text = element.text.strip()

            if text:

                title = text
                break

        except:
            pass


    item["Title"] = title


    # --------------------------------------
    # LINK
    # --------------------------------------

    link = "NA"

    try:

        element = product.find_element(
            By.CSS_SELECTOR,
            "a"
        )

        link = element.get_attribute("href")

    except:
        pass


    item["Link"] = link


    # --------------------------------------
    # PRICE
    # --------------------------------------

    price = "NA"

    price_selectors = [
        "[class*='price']",
        "[class*='Price']"
    ]

    for selector in price_selectors:

        try:

            elements = product.find_elements(
                By.CSS_SELECTOR,
                selector
            )

            for element in elements:

                text = element.text.strip()

                if text and any(
                    x in text.upper()
                    for x in ["USD", "PKR", "$"]
                ):

                    price = text
                    break

            if price != "NA":
                break

        except:
            pass


    item["Price"] = price


    # --------------------------------------
    # MINIMUM ORDER
    # --------------------------------------

    minimum_order = "NA"

    try:

        text = product.text

        lines = text.split("\n")

        for line in lines:

            if "piece" in line.lower():

                minimum_order = line.strip()
                break

            if "order" in line.lower():

                minimum_order = line.strip()
                break


    except:
        pass


    item["Minimum Order"] = minimum_order


    # --------------------------------------
    # IMAGE
    # --------------------------------------

    image = "NA"

    try:

        img = product.find_element(
            By.CSS_SELECTOR,
            "img"
        )

        image = img.get_attribute("src")

        if not image:

            image = img.get_attribute(
                "data-src"
            )

        if not image:

            image = img.get_attribute(
                "data-lazy-src"
            )

    except:
        pass


    item["Image"] = image


    # --------------------------------------
    # ADD ITEM
    # --------------------------------------

    if (
        item["Title"] != "NA"
        or item["Price"] != "NA"
    ):

        data.append(item)


# ==========================================
# Remove Duplicate Products
# ==========================================

df = pd.DataFrame(data)


if not df.empty:

    df = df.drop_duplicates(
        subset=["Title", "Link"]
    )

    df = df.reset_index(drop=True)


# ==========================================
# Display Data
# ==========================================

print("\n================================")
print("FINAL PRODUCT COUNT:", len(df))
print("================================\n")

print(df)


# ==========================================
# Save CSV
# ==========================================

df.to_csv(
    "Alibaba-Auto-Accessories.csv",
    index=False,
    encoding="utf-8-sig"
)

print(
    "\nCSV file saved as: "
    "Alibaba-Auto-Accessories.csv"
)


# ==========================================
# Close Browser
# ==========================================

driver.quit()