from playwright.sync_api import Page 
from faker import Faker
from pages.main_page import Main_page

class Register_user:
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()
        self.main_page = Main_page(page)
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
        self.existed_email = page.locator("text=Email Address already exist!")

    def register(self, email: str, name: str) -> None:
        self.main_page.input_name.type(name)
        self.input_email.type(email)
        self.button_submit_register.click()

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
        self.main_page.button_submit.click()

    def click_continue_button(self) -> None:
        self.button_continue.click() 

