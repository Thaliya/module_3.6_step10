import pytest
from selenium.webdriver.common.by import By
# import time

link1 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link2 = "https://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/"


@pytest.mark.parametrize("link", [link1, link2])
def test_add_to_basket_button(browser, link):
    browser.get(link)
    # time.sleep(30)

    assert len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) == 1, \
        "Expected the button to add to basket to be displayed"
    # el_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    # assert el_basket.text == "Ajouter au panier", f"Expected the button text to be 'Ajouter au panier' \
    #                           but the page returned '{el_basket.text}'"
