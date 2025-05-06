from playwright.sync_api import Page 

class Register_user:
    def __init__(self, page: Page):
        self.page = page
        self.existed_email = page.locator("text=Email Address already exist!")



