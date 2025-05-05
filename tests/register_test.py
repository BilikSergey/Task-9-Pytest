import pytest
import allure
from playwright.sync_api import expect

@pytest.fixture
def test_before_each(main_page, page):
    with allure.step("Visit main page"):
        main_page.visit_main_page()
        allure.attach(page.screenshot(), name="visit_main_page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify header is visible"):
        expect(main_page.header).to_be_visible()
        allure.attach(page.screenshot(), name="header_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify slider is visible"):
        expect(main_page.slider).to_be_visible()
        allure.attach(page.screenshot(), name="slider_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click Sign Up / Login button"):
        main_page.click_button_sign_up_login()
        allure.attach(page.screenshot(), name="sign_up_clicked", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify Sign Up form is visible"):
        expect(main_page.sign_up_form).to_be_visible()
        allure.attach(page.screenshot(), name="sign_up_form_visible", attachment_type=allure.attachment_type.PNG)

def test_verify_correct_register_and_delete(test_before_each, main_page, register_user, fake, page):
    with allure.step("Register new user"):
        register_user.register(fake.email(), fake.name())
        allure.attach(page.screenshot(), name="registered", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify account info form is visible"):
        expect(register_user.form_account_info).to_be_visible()
        allure.attach(page.screenshot(), name="account_info_form", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add account data"):
        register_user.add_data_about_account()
        allure.attach(page.screenshot(), name="account_data_added", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify congratulations form is visible"):
        expect(register_user.form_congrats).to_be_visible()
        allure.attach(page.screenshot(), name="congrats_form", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click Continue after registration"):
        register_user.click_continue_button()
        allure.attach(page.screenshot(), name="clicked_continue", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify user is logged in"):
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        allure.attach(page.screenshot(), name="logged_in", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click Delete Account"):
        main_page.click_delete_button()
        allure.attach(page.screenshot(), name="clicked_delete", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify account deleted message"):
        expect(main_page.form_account_deleted).to_be_visible()
        allure.attach(page.screenshot(), name="account_deleted", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click Continue after deletion"):
        register_user.click_continue_button()
        allure.attach(page.screenshot(), name="continue_after_delete", attachment_type=allure.attachment_type.PNG)

def test_verify_correct_email_for_registration(test_before_each, register_user, fake, user_data, page):
    with allure.step("Attempt to register with existing email"):
        register_user.register(user_data["email"], fake.name())
        allure.attach(page.screenshot(), name="existing_email_attempt", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify 'email already exists' message appears"):
        expect(register_user.existed_email).to_be_enabled()
        allure.attach(page.screenshot(), name="email_exists_message", attachment_type=allure.attachment_type.PNG)
