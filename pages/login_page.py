from playwright.sync_api import Page 
from pages.main_page import Main_page

class Login_user:
    def __init__(self, page: Page):
        self.page = page
        self.main_page = Main_page(page)
        self.input_password = page.locator('(//*[@name="password"])')
        self.input_email = page.locator('(//*[@name="email"])[1]')
        self.wrong_credentials = page.locator("text=Your email or password is incorrect!")
        self.button_logout = page.locator('(//a[@href="/logout"])')

    def login(self, email: str, password: str) -> None:
        self.input_email.type(email)
        self.input_password.type(password)
        self.main_page.button_submit.click()

    def click_logout_button(self) -> None:
        self.button_logout.click()
