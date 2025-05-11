import json
import time

import pytest
from playwright.sync_api import Page, Playwright

#read the data from JSON (converting JSON data into python object using json.load & storing into login_data object
with open('credentials.json', 'r') as f:
    login_data = json.load(f)
    user_login_list = login_data['user_credentials']


#Parametrizing the user_credentials into dynamic variable.
@pytest.mark.parametrize('user_credentials', user_login_list)
def test_user_login(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://awesomeqa.com/ui/index.php?route=account/login")
    page.get_by_placeholder("E-Mail Address").fill(user_credentials["userEmail"])
    page.get_by_placeholder("Password").fill(user_credentials["userPassword"])
    page.get_by_role("button", name="Login").click()
    time.sleep(5)
