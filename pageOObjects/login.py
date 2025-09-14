class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://awesomeqa.com/ui/index.php?route=account/login")

    def login(self, username, password):
        self.page.get_by_placeholder("E-Mail Address").fill(username)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role("button", name="Login").click()
