import pytest
import allure
from playwright.sync_api import expect

@pytest.fixture
def test_before_each(main_page, page):
    with allure.step("Visit main page"):
        main_page.visit_main_page()
        allure.attach(page.screenshot(), name="main_page_loaded", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify header is visible"):
        expect(main_page.header).to_be_visible()
        allure.attach(page.screenshot(), name="header_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify slider is visible"):
        expect(main_page.slider).to_be_visible()
        allure.attach(page.screenshot(), name="slider_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click 'Sign Up / Login' button"):
        main_page.click_button_sign_up_login()
        allure.attach(page.screenshot(), name="click_sign_up_login", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify sign-up form is visible"):
        expect(main_page.sign_up_form).to_be_visible()
        allure.attach(page.screenshot(), name="sign_up_form_visible", attachment_type=allure.attachment_type.PNG)

def test_verify_correct_login(test_before_each, login_user, main_page, user_data, page):
    with allure.step("Log in with valid credentials"):
        login_user.login(user_data["email"], user_data["password"])
        allure.attach(page.screenshot(), name="login_success", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify 'Logged in as' message"):
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        allure.attach(page.screenshot(), name="logged_in_message", attachment_type=allure.attachment_type.PNG)

    # Uncomment if you want to test account deletion:
    # with allure.step("Click delete account"):
    #     main_page.click_delete_button()
    #     allure.attach(page.screenshot(), name="clicked_delete", attachment_type=allure.attachment_type.PNG)

    # with allure.step("Verify account deleted"):
    #     expect(main_page.form_account_deleted).to_be_visible()
    #     allure.attach(page.screenshot(), name="account_deleted", attachment_type=allure.attachment_type.PNG)

def test_verify_incorrect_login(test_before_each, login_user, fake, page):
    with allure.step("Attempt login with incorrect credentials"):
        login_user.login(fake.email(), fake.password())
        allure.attach(page.screenshot(), name="login_failed", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify error message is shown"):
        expect(login_user.wrong_credentials).to_be_enabled()
        allure.attach(page.screenshot(), name="wrong_credentials", attachment_type=allure.attachment_type.PNG)

def test_verify_logout(test_before_each, login_user, main_page, user_data, page):
    with allure.step("Log in with valid credentials"):
        login_user.login(user_data["email"], user_data["password"])
        allure.attach(page.screenshot(), name="login_for_logout", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify 'Logged in as' message"):
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        allure.attach(page.screenshot(), name="logged_in_message_before_logout", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click logout button"):
        login_user.click_logout_button()
        allure.attach(page.screenshot(), name="clicked_logout", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify sign-up form is visible again"):
        expect(main_page.sign_up_form).to_be_visible()
        allure.attach(page.screenshot(), name="sign_up_form_after_logout", attachment_type=allure.attachment_type.PNG)
