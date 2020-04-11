import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(30)
    try:
       btn = browser.find_elements_by_class_name("btn-add-to-basket")
       assert len(btn) == 1, "Error: Non-unique selector selected"
    finally:
       time.sleep(1)




