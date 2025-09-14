import time

from playwright.sync_api import Page, Playwright, expect
#from util.utils import credential

def test_login_functionality(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://awesomeqa.com/ui/index.php?route=account/register")


def test_registration_page(page: Page):
    page.goto("https://awesomeqa.com/ui/index.php?route=account/register")
    page.get_by_label("First Name").fill("DheerajS")
    page.get_by_label("Last Name").fill("SharmaS")
    page.get_by_label("E-Mail").fill("drj19001@gmail.com")
    page.get_by_label("Telephone").fill("7007183401")
    page.get_by_role("textbox", name="* Password", exact=True).fill("Nrjshrm12")
    page.get_by_role("textbox", name="* Password Confirm", exact=True).fill("Nrjshrm12")
    page.get_by_role("checkbox").check()
    page.get_by_role("button", name="Continue").click()
    #check for the below text should be visible after clicking on Continue button
    expect(page.get_by_text("Your Account Has Been Created!")).to_be_visible()
    time.sleep(5)




