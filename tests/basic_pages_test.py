import pytest
import allure
from playwright.sync_api import expect

@pytest.fixture
def test_before_each(main_page):
    with allure.step("Visit main page and verify key elements"):
        main_page.visit_main_page()
        expect(main_page.header).to_be_visible()
        expect(main_page.slider).to_be_visible()

@allure.title("Contact Us Page: Submit contact form")
@allure.description("Verifies that the user can access the contact form, fill it, submit it, and return to the homepage.")
def test_contact_us_page(test_before_each, basic_pages, fake, page):
    with allure.step("Click 'Contact Us' button"):
        basic_pages.click_contact_us_button()
        allure.attach(page.screenshot(), name="clicked_contact_us", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify contact form is visible"):
        expect(basic_pages.form_get_in_touch).to_be_visible()
        allure.attach(page.screenshot(), name="contact_form_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Fill in the contact form with fake data"):
        basic_pages.fill_form(fake.email(), fake.name(), fake.first_name(), fake.name())
        allure.attach(page.screenshot(), name="form_filled", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify success message after submission"):
        expect(basic_pages.message_successful_submitted).to_be_visible()
        allure.attach(page.screenshot(), name="form_submitted", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click 'Home' button to return to main page"):
        basic_pages.click_home_button()
        allure.attach(page.screenshot(), name="returned_home", attachment_type=allure.attachment_type.PNG)

@allure.title("Test Cases Page: Navigate and verify")
@allure.description("Checks that the Test Cases page opens correctly and matches the expected URL.")
def test_test_cases_page(test_before_each, page, basic_pages, url_for_pages):
    with allure.step("Click 'Test Cases' button"):
        basic_pages.click_button_test_cases()
        allure.attach(page.screenshot(), name="clicked_test_cases", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify page URL matches expected"):
        expect(page).to_have_url(url_for_pages["test_cases"])
        allure.attach(page.screenshot(), name="verified_url", attachment_type=allure.attachment_type.PNG)

@allure.title("Home Page: Verify subscription feature")
@allure.description("Scrolls to the bottom, subscribes with email, and checks success message.")
def test_verify_subscription_home(test_before_each, page, fake, main_page):
    with allure.step("Scroll to bottom of the page"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(page.screenshot(), name="scrolled_down", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify 'Subscription' title is visible"):
        expect(main_page.title_subscription).to_contain_text("Subscription")
        allure.attach(page.screenshot(), name="subscription_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Subscribe with fake email"):
        main_page.subscribe(fake.email())
        allure.attach(page.screenshot(), name="subscribed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify subscription success message"):
        expect(main_page.successful_message_subscribed).to_be_visible()
        allure.attach(page.screenshot(), name="subscription_success", attachment_type=allure.attachment_type.PNG)

@allure.title("Scroll with Arrow: Scroll down and up using arrow button")
@allure.description("Scrolls to the bottom, uses scroll-up arrow, and checks content is visible at the top.")
def test_verify_scroll_up_using_arrow_button_and_scroll_down_functionality(test_before_each, page, main_page, basic_pages, messages):
    with allure.step("Scroll to bottom of the page"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(page.screenshot(), name="scrolled_down", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify 'Subscription' section is visible"):
        expect(main_page.title_subscription).to_contain_text("Subscription")
        allure.attach(page.screenshot(), name="subscription_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click scroll-up arrow button"):
        basic_pages.click_button_scroll_up()
        allure.attach(page.screenshot(), name="clicked_scroll_up", attachment_type=allure.attachment_type.PNG)

    with allure.step("Wait until scroll is at the top"):
        page.wait_for_function("() => window.scrollY === 0", timeout=5000)
        assert page.evaluate("() => window.scrollY") == 0
        allure.attach(page.screenshot(), name="scrolled_up", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify top carousel content is visible"):
        expect(basic_pages.form_carousel_inner).to_contain_text(messages["carousel"])
        allure.attach(page.screenshot(), name="carousel_visible", attachment_type=allure.attachment_type.PNG)

@allure.title("Scroll Without Arrow: Scroll down and manually back up")
@allure.description("Tests scrolling down and manually up without using the arrow, and verifies top content.")
def test_verify_scroll_up_without_arrow_button_and_scroll_down_functionality(test_before_each, page, main_page, basic_pages, messages):
    with allure.step("Scroll to bottom of the page"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(page.screenshot(), name="scrolled_down", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify 'Subscription' section is visible"):
        expect(main_page.title_subscription).to_contain_text("Subscription")
        allure.attach(page.screenshot(), name="subscription_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Scroll manually back to the top"):
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_function("() => window.scrollY === 0", timeout=5000)
        assert page.evaluate("() => window.scrollY") == 0
        allure.attach(page.screenshot(), name="scrolled_up_manual", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify top carousel content is visible"):
        expect(basic_pages.form_carousel_inner).to_contain_text(messages["carousel"])
        allure.attach(page.screenshot(), name="carousel_visible", attachment_type=allure.attachment_type.PNG)
