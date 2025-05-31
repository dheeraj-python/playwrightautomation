import json
import time

import pytest
from playwright.sync_api import Page, Playwright
from pageObjects.login import LoginPage
from pageObjects.myaccount import MyAccount

#read the data from JSON (converting JSON data into python object using json.load & storing into login_data object
with open('credentials.json', 'r') as f:
    login_data = json.load(f)
    user_login_list = login_data['user_credentials']


#Parametrizing the user_credentials into dynamic variable.


@pytest.mark.parametrize('user_credentials', user_login_list)
def test_user_login(playwright: Playwright, user_credentials, browser_instance, LoginPage=LoginPage, MyAccount=MyAccount):
    username = user_credentials["userEmail"]
    password = user_credentials["userPassword"]
    LoginPage = LoginPage(browser_instance)  #object for LoginPage Class
    LoginPage.navigate()
    LoginPage.login(username, password)
    time.sleep(2)
    MyAccount = MyAccount(browser_instance)
    MyAccount.navigateorderlink()

    time.sleep(3)
