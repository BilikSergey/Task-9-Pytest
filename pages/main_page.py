from playwright.sync_api import Page 
from faker import Faker

class Main_page:
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()
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
        self.input_email = page.locator('(//*[@name="email"])[2]')
        self.button_submit_register = page.locator('(//*[@type="submit"])[2]')
        self.form_account_info = page.locator('(//*[@class="login-form"])')
        self.input_password = page.locator('(//*[@id="password"])')
        self.selector_days = page.locator('(//*[@id="days"])')
        self.selector_months = page.locator('(//*[@id="months"])')
        self.selector_years = page.locator('(//*[@id="years"])')
        self.checkbox_newsletter = page.locator('(//*[@id="newsletter"])')
        self.checkbox_option = page.locator('(//*[@id="optin"])')
        self.input_first_name = page.locator('(//*[@id="first_name"])')
        self.input_last_name = page.locator('(//*[@id="last_name"])')
        self.input_company = page.locator('(//*[@id="company"])')
        self.input_address_1 = page.locator('(//*[@id="address1"])')
        self.input_address_2 = page.locator('(//*[@id="address2"])')
        self.selector_country = page.locator('(//*[@id="country"])')
        self.input_state = page.locator('(//*[@id="state"])')
        self.input_city = page.locator('(//*[@id="city"])')
        self.input_zipcode = page.locator('(//*[@id="zipcode"])')
        self.input_mobile_number = page.locator('(//*[@id="mobile_number"])')
        self.form_congrats = page.locator('(//*[@class="col-sm-9 col-sm-offset-1"])')
        self.button_continue = page.locator('(//*[@class="btn btn-primary"])')

    def visit_main_page(self) -> None:
        self.page.goto("http://automationexercise.com")

    def add_data_about_account(self) -> None:
        self.page.evaluate("""
            const ad = document.querySelector('ins.adsbygoogle');
            if (ad) {
                ad.remove();
            }
        """)
        self.input_password.type(self.fake.password())
        self.selector_days.select_option(value='1')
        self.selector_months.select_option(value='1')
        self.selector_years.select_option(value='1998')
        self.checkbox_newsletter.check()
        self.checkbox_option.check()
        self.input_first_name.type(self.fake.first_name())
        self.input_last_name.type(self.fake.last_name())
        self.input_company.type(self.fake.company())
        self.input_address_1.type(self.fake.address())
        self.input_address_2.type(self.fake.address())
        self.selector_country.select_option(value='Canada')
        self.input_state.type(self.fake.name())
        self.input_city.type(self.fake.city())
        self.input_zipcode.type(self.fake.zipcode())
        self.input_mobile_number.type(self.fake.phone_number())
        self.button_submit.click()

    def register(self, email: str, name: str) -> None:
        self.input_name.type(name)
        self.input_email.type(email)
        self.button_submit_register.click()

    def click_continue_button(self) -> None:
        self.button_continue.click() 

    def click_button_sign_up_login(self) -> None:
        self.button_sign_up_login.click()

    def click_delete_button(self) -> None:
        self.button_delete_account.click()
        
    def subscribe(self, email: str) -> None:
        self.input_subscription.type(email)
        self.arrow_button_subscribe.click()
