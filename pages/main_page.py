from playwright.sync_api import Page 

class Main_page:
    def __init__(self, page: Page):
        self.page = page
        self.header = page.locator('//*[@id="header"]')
        self.slider = page.locator('//*[@id="slider"]')
        self.input_name = page.locator('(//*[@name="name"])')
        self.button_sign_up_login = page.locator('//*[@href="/login"]')
        self.sign_up_form = page.locator('//*[@class="signup-form"]')
        self.form_with_entry_message = page.locator('a:has(i.fa-user)')
        self.button_delete_account = page.locator('(//a[@href="/delete_account"])')
        self.form_account_deleted = page.locator('(//*[@class="col-sm-9 col-sm-offset-1"])')
        self.button_submit = page.locator('(//*[@type="submit"])[1]')
        self.title_subscription = page.locator('(//*[@class="single-widget"])')
        self.arrow_button_subscribe = page.locator('(//*[@id="subscribe"])')
        self.successful_message_subscribed = page.locator('(//*[@class="alert-success alert"])')
        self.input_subscription = page.locator('(//*[@id="susbscribe_email"])')

    def visit_main_page(self) -> None:
        self.page.goto("http://automationexercise.com")

    def click_button_sign_up_login(self) -> None:
        self.button_sign_up_login.click()

    def click_delete_button(self) -> None:
        self.button_delete_account.click()
        
    def subscribe(self, email: str) -> None:
        self.input_subscription.type(email)
        self.arrow_button_subscribe.click()
