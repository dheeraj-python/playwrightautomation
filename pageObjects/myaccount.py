class MyAccount:

    def __init__(self, page):
        self.page = page

    def navigateorderlink(self):
        self.page.get_by_role("link", name="View your order history").click()

