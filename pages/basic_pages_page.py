from playwright.sync_api import Page 
from pages.main_page import Main_page

class Basic_pages:
    def __init__(self, page: Page):
        self.page = page
        self.main_page = Main_page(page)
        self.button_contact_us = page.locator('(//a[@href="/contact_us"])')
        self.button_test_cases = page.locator('(//a[@href="/test_cases"])[1]')
        self.button_cart = page.locator('(//a[@href="/view_cart"])[1]')
        self.form_get_in_touch = page.locator('(//*[@class="title text-center"])[2]')
        self.input_email = page.locator('(//*[@name="email"])')
        self.input_subject = page.locator('(//*[@name="subject"])')
        self.input_message = page.locator('(//*[@name="message"])')
        self.input_upload_file = page.locator('(//*[@name="upload_file"])')
        self.message_successful_submitted = page.locator('(//*[@class="status alert alert-success"])')
        self.button_home = page.locator('(//*[@class="btn btn-success"])')
        self.button_scroll_up = page.locator('(//*[@id="scrollUp"])')
        self.form_carousel_inner = page.locator('(//*[@class="carousel-inner"])[1]')

    def fill_form(self, email: str, name: str, subject: str, message: str) -> None:
        self.page.evaluate("""
            const ad = document.querySelector('ins.adsbygoogle');
            if (ad) {
                ad.remove();
            }
        """)
        self.main_page.input_name.type(name)
        self.input_email.type(email)
        self.input_subject.type(subject)
        self.input_message.type(message)
        self.input_upload_file.set_input_files("data/sample.txt")
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.main_page.button_submit.click()

    def click_contact_us_button(self) -> None:
        self.button_contact_us.click()

    def click_button_scroll_up(self) -> None:
        self.page.evaluate("""
            const ad = document.querySelector('ins.adsbygoogle');
            if (ad) {
                ad.remove();
            }
        """)
        self.button_scroll_up.click()

    def click_home_button(self) -> None:
        self.button_home.click()

    def click_button_test_cases(self) -> None:
        self.button_test_cases.click()