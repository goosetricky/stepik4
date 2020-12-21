import time

from pages.base_page import BasePage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = BasePage(browser, link)
    page.open()
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
    time.sleep(10)
