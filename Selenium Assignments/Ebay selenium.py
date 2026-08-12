from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException
)
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
# eBay URL
# ==========================================

url = "https://www.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094"


# ==========================================
# Open eBay
# ==========================================

print("Opening eBay...")

try:
    driver.get(url)

except TimeoutException:
    print("Page loading timeout. Continuing...")


# ==========================================
# Wait for page
# ==========================================

time.sleep(5)


# ==========================================
# Scroll page
# ==========================================

print("Scrolling page...")

for i in range(5):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(2)

print("Scrolling completed.")


# ==========================================
# Helper Function
# ==========================================

def getData(tag, selector):

    try:

        element = tag.find_element(
            By.CSS_SELECTOR,
            selector
        )

        return element

    except NoSuchElementException:

        return None


# ==========================================
# Find Product Container
# ==========================================

container_selectors = [

    "ul.brwrvr__item-results.brwrvr__item-results--list",

    "ul.brwrvr__item-results",

    "ul[class*='item-results']"

]


cell_phones = None


for selector in container_selectors:

    try:

        cell_phones = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, selector)
            )
        )

        print(
            "Product container found using:",
            selector
        )

        break

    except TimeoutException:

        print(
            "Container not found:",
            selector
        )


# ==========================================
# If container not found
# ==========================================

if cell_phones is None:

    print(
        "\nCould not find eBay product container."
    )

    driver.quit()

    exit()


# ==========================================
# Find Products
# ==========================================

product_selectors = [

    "li.brwrvr__item-card",

    "li[class*='item-card']",

    "li.s-item"

]


products = []


for selector in product_selectors:

    try:

        products = cell_phones.find_elements(
            By.CSS_SELECTOR,
            selector
        )

        print(
            f"Selector: {selector} --> "
            f"{len(products)} products"
        )

        if len(products) > 0:

            break

    except Exception:

        pass


print(
    "\nTotal Products Found:",
    len(products)
)


# ==========================================
# Extract Data
# ==========================================

cell_phones_list = []


for cell_phone in products:

    cell_phone_dictionary = {}


    # ======================================
    # TITLE
    # ======================================

    title = getData(
        cell_phone,
        "h3.textual-display.bsig__title__text"
    )


    if title:

        cell_phone_dictionary["Title"] = (
            title.text.strip()
        )

    else:

        # Backup selector
        title = getData(
            cell_phone,
            "h3.s-item__title"
        )

        if title:

            cell_phone_dictionary["Title"] = (
                title.text.strip()
            )

        else:

            cell_phone_dictionary["Title"] = "NA"


    # ======================================
    # PRICE
    # ======================================

    price = getData(
        cell_phone,
        "span.textual-display.bsig__price.bsig__price--displayprice"
    )


    if price:

        cell_phone_dictionary["Price"] = (
            price.text.strip()
        )

    else:

        # Backup selector
        price = getData(
            cell_phone,
            "span.s-item__price"
        )

        if price:

            cell_phone_dictionary["Price"] = (
                price.text.strip()
            )

        else:

            cell_phone_dictionary["Price"] = "NA"


    # ======================================
    # IMAGE
    # ======================================

    image = getData(
        cell_phone,
        "a.brwrvr__item-card__image-link img.brwrvr__item-card__image"
    )


    if image:

        image_url = image.get_attribute("src")

        if not image_url:

            image_url = image.get_attribute(
                "data-src"
            )

        cell_phone_dictionary["Image"] = (
            image_url if image_url else "NA"
        )

    else:

        # Backup selector
        image = getData(
            cell_phone,
            "img.s-item__image"
        )

        if image:

            cell_phone_dictionary["Image"] = (
                image.get_attribute("src")
            )

        else:

            cell_phone_dictionary["Image"] = "NA"


    # ======================================
    # STATUS / CONDITION
    # ======================================

    status = "NA"


    status_selectors = [

        "span.textual-display.bsig__generic.bsig__listingCondition.secondary",

        "span[class*='listingCondition']",

        "span.s-item__condition"

    ]


    status_elements = []


    for selector in status_selectors:

        try:

            status_elements = (
                cell_phone.find_elements(
                    By.CSS_SELECTOR,
                    selector
                )
            )

            if len(status_elements) > 0:

                break

        except:

            pass


    if len(status_elements) > 0:

        status = status_elements[0].text.strip()


    cell_phone_dictionary["Status"] = status


    # ======================================
    # COMPANY
    # ======================================

    company = "NA"


    if len(status_elements) > 1:

        company = status_elements[-1].text.strip()


    # Backup: seller
    if company == "NA":

        try:

            seller = cell_phone.find_element(
                By.CSS_SELECTOR,
                "span.s-item__seller-info-text"
            )

            company = seller.text.strip()

        except:

            pass


    cell_phone_dictionary["Company"] = company


    # ======================================
    # LINK
    # ======================================

    link = "NA"


    try:

        link_element = cell_phone.find_element(
            By.CSS_SELECTOR,
            "a"
        )

        link = link_element.get_attribute(
            "href"
        )

    except:

        pass


    cell_phone_dictionary["Link"] = link


    # ======================================
    # ADD TO LIST
    # ======================================

    if (
        cell_phone_dictionary["Title"] != "NA"
        or cell_phone_dictionary["Price"] != "NA"
    ):

        cell_phones_list.append(
            cell_phone_dictionary
        )


# ==========================================
# Close Browser
# ==========================================

driver.quit()


# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(
    cell_phones_list
)


# ==========================================
# Remove Duplicates
# ==========================================

if not df.empty:

    df = df.drop_duplicates(
        subset=["Title", "Link"]
    )

    df = df.reset_index(drop=True)


# ==========================================
# Display Data
# ==========================================

print("\n====================================")
print(
    "FINAL PRODUCTS:",
    len(df)
)
print("====================================\n")

print(df)


# ==========================================
# Save CSV
# ==========================================

df.to_csv(
    "Ebay-Selenium.csv",
    index=False,
    encoding="utf-8-sig"
)


print(
    "\nCSV file saved successfully!"
)

print(
    "File: Ebay-Selenium.csv"
)