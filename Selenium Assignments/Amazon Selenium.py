from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
# Amazon URL
# ==========================================

url = "https://www.amazon.com/s?k=smart+home+devices"

print("Opening Amazon...")

try:
    driver.get(url)

except TimeoutException:
    print("Page loading timeout. Continuing...")


# ==========================================
# Wait for Page
# ==========================================

time.sleep(5)


# ==========================================
# Scroll Page
# ==========================================

print("Scrolling page...")

for i in range(8):

    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    time.sleep(2)


print("Scrolling completed.")


# ==========================================
# Find Amazon Products
# ==========================================

selectors = [

    "div[data-component-type='s-search-result']",

    "div.s-result-item[data-asin]",

    "div[data-asin]"

]


products = []


for selector in selectors:

    try:

        products = driver.find_elements(
            By.CSS_SELECTOR,
            selector
        )

        print(
            f"Selector: {selector} --> "
            f"{len(products)} products"
        )

        if len(products) > 0:
            break

    except Exception as e:

        print("Selector error:", e)


print("\nTotal Products Found:", len(products))


# ==========================================
# Extract Product Data
# ==========================================

data = []


for product in products:

    item = {}


    # ======================================
    # TITLE
    # ======================================

    title = "NA"

    title_selectors = [

        "h2 a span",

        "h2 span",

        "h2",

        "span.a-size-medium",

        "span.a-size-base-plus"

    ]


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


    item["Product_Name"] = title


    # ======================================
    # LINK
    # ======================================

    link = "NA"


    try:

        element = product.find_element(
            By.CSS_SELECTOR,
            "h2 a"
        )

        link = element.get_attribute("href")


    except:

        try:

            element = product.find_element(
                By.CSS_SELECTOR,
                "a.a-link-normal"
            )

            link = element.get_attribute("href")

        except:

            pass


    item["Product_Link"] = link


    # ======================================
    # PRICE
    # ======================================

    price = "NA"


    price_selectors = [

        "span.a-price span.a-offscreen",

        "span.a-price-whole",

        "span.a-offscreen"

    ]


    for selector in price_selectors:

        try:

            element = product.find_element(
                By.CSS_SELECTOR,
                selector
            )

            text = element.text.strip()

            if text:

                price = text
                break

        except:

            pass


    item["Product_Price"] = price


    # ======================================
    # RATING
    # ======================================

    rating = "NA"


    rating_selectors = [

        "span.a-icon-alt",

        "i.a-icon-star-small span.a-icon-alt",

        "span[class*='rating']"

    ]


    for selector in rating_selectors:

        try:

            element = product.find_element(
                By.CSS_SELECTOR,
                selector
            )

            text = element.text.strip()

            if text:

                rating = text
                break

        except:

            pass


    item["Product_Rating"] = rating


    # ======================================
    # REVIEWS
    # ======================================

    reviews = "NA"


    try:

        review_element = product.find_element(
            By.CSS_SELECTOR,
            "span.a-size-base.s-underline-text"
        )

        reviews = review_element.text.strip()

    except:

        pass


    item["Reviews"] = reviews


    # ======================================
    # IMAGE
    # ======================================

    image = "NA"


    try:

        img = product.find_element(
            By.CSS_SELECTOR,
            "img.s-image"
        )

        image = img.get_attribute("src")


        if not image:

            image = img.get_attribute(
                "data-src"
            )


    except:

        pass


    item["Product_Image"] = image


    # ======================================
    # ASIN
    # ======================================

    try:

        asin = product.get_attribute(
            "data-asin"
        )

        if asin:

            item["ASIN"] = asin

        else:

            item["ASIN"] = "NA"

    except:

        item["ASIN"] = "NA"


    # ======================================
    # ADD DATA
    # ======================================

    if (
        item["Product_Name"] != "NA"
        or item["Product_Price"] != "NA"
    ):

        data.append(item)


# ==========================================
# Create DataFrame
# ==========================================

df = pd.DataFrame(data)


# ==========================================
# Remove Duplicates
# ==========================================

if not df.empty:

    df = df.drop_duplicates(
        subset=["Product_Name", "Product_Link"]
    )

    df = df.reset_index(drop=True)


# ==========================================
# Display Data
# ==========================================

print("\n====================================")
print("FINAL PRODUCT COUNT:", len(df))
print("====================================\n")

print(df)


# ==========================================
# Save CSV
# ==========================================

df.to_csv(
    "Amazon-Smart-Home-Products.csv",
    index=False,
    encoding="utf-8-sig"
)


print(
    "\nCSV file saved successfully!"
)

print(
    "File Name: Amazon-Smart-Home-Products.csv"
)


# ==========================================
# Close Browser
# ==========================================

driver.quit()