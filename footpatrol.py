from selenium.webdriver.common.by import By
# https://www.footpatrol.com/

# Buttons/fields are in a form of xpath
cookie_button = "//*[@class='btn btn-level1 accept-all-cookies']"
search_button = "//*[@id='searchButton']"
search_field = "//*[@id='srchInput']"

# Scripts are in a form of web scripts
cookie_accept_script = "document.getElementsByClassName(\"btn btn-level1 accept-all-cookies\")[0]" \
                       ".dispatchEvent(new Event(\"click\"))"
search_button_click_script = "document.getElementById(\"searchButton\")." \
                             "dispatchEvent(new Event(\"click\"))"
price_sort_scripts = ["document.querySelector('[value=price-low-high]').selected = true",
                      "document.getElementById(\"sortFormTop\").dispatchEvent(new Event(\"submit\"))"]


def gather_info(driver) -> bool:
    all_items = driver.find_elements(By.CLASS_NAME, "itemInformation")
    if len(all_items) == 0:
        print("Could not gather info about items")
        return False

    for i, item in enumerate(all_items):
        name = item.find_elements(By.CLASS_NAME, "itemTitle")[0].find_elements(By.TAG_NAME, "a")[0].text
        if not name:
            print(f"Could not find name of item {i + 1}")
            continue

        price = item.find_elements(By.CLASS_NAME, "itemPrice")[0]. \
            find_elements(By.CLASS_NAME, "pri")[0]
        price_with_sale = price.find_elements(By.CLASS_NAME, "now")
        if len(price_with_sale) != 0:
            price = price_with_sale[0]

        if not price:
            print(f"Could not find price of item {i + 1}")

        if name and price:
            print(f"{i + 1} ", name, price.text)

    return True
