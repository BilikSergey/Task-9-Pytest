import pytest
import allure
import os
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


def test_product_page(test_before_each, page, product_page, url_for_pages, details_of_wares):
    with allure.step("Click Products button"):
        product_page.click_button_products()
        allure.attach(page.screenshot(), name="click_products_button", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify URL for products page"):
        expect(page).to_have_url(url_for_pages["products"])
        allure.attach(page.screenshot(), name="verify_products_url", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify product list is visible"):
        expect(product_page.list_of_wares).to_be_visible()
        allure.attach(page.screenshot(), name="product_list_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click on a product to view details"):
        product_page.click_button_view_ware()
        allure.attach(page.screenshot(), name="view_product_details", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify URL for product details page"):
        expect(page).to_have_url(url_for_pages["products_details_1"])
        allure.attach(page.screenshot(), name="verify_product_details_url", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify product information on the page"):
        expect(product_page.product_information).to_contain_text(details_of_wares["name"])
        expect(product_page.product_information).to_contain_text(details_of_wares["category"])
        expect(product_page.product_information).to_contain_text(details_of_wares["price"])
        expect(product_page.product_information).to_contain_text(details_of_wares["availability"])
        expect(product_page.product_information).to_contain_text(details_of_wares["condition"])
        expect(product_page.product_information).to_contain_text(details_of_wares["brand"])
        allure.attach(page.screenshot(), name="product_information", attachment_type=allure.attachment_type.PNG)


def test_search_product(test_before_each, page, product_page, url_for_pages, details_of_wares):
    with allure.step("Click Products button"):
        product_page.click_button_products()
        allure.attach(page.screenshot(), name="click_products_button", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify URL for products page"):
        expect(page).to_have_url(url_for_pages["products"])
        allure.attach(page.screenshot(), name="verify_products_url", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify product list is visible"):
        expect(product_page.list_of_wares).to_be_visible()
        allure.attach(page.screenshot(), name="product_list_visible", attachment_type=allure.attachment_type.PNG)

    with allure.step("Search for product"):
        product_page.search_for_ware(details_of_wares["name"])
        allure.attach(page.screenshot(), name="search_for_product", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify product info in the search results"):
        expect(product_page.form_of_product_information).to_contain_text(details_of_wares["name"])
        expect(product_page.form_of_product_information).to_contain_text(details_of_wares["price"])
        allure.attach(page.screenshot(), name="search_results", attachment_type=allure.attachment_type.PNG)


def test_verify_subscription_cart(test_before_each, page, fake, main_page, product_page):
    with allure.step("Click Cart button"):
        product_page.click_button_cart()
        allure.attach(page.screenshot(), name="click_cart_button", attachment_type=allure.attachment_type.PNG)

    with allure.step("Scroll to bottom of the page"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        allure.attach(page.screenshot(), name="scroll_bottom", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify subscription title"):
        expect(main_page.title_subscription).to_contain_text("Subscription")
        allure.attach(page.screenshot(), name="verify_subscription_title", attachment_type=allure.attachment_type.PNG)

    with allure.step("Subscribe with fake email"):
        main_page.subscribe(fake.email())
        allure.attach(page.screenshot(), name="subscribe_success", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify successful subscription message"):
        expect(main_page.successful_message_subscribed).to_be_visible()
        allure.attach(page.screenshot(), name="successful_subscription", attachment_type=allure.attachment_type.PNG)


def test_add_product_to_cart(test_before_each, page, product_page, details_of_wares, details_of_wares_2):
    with allure.step("Click Products button"):
        product_page.click_button_products()
        allure.attach(page.screenshot(), name="click_products_button", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add first product to cart"):
        product_page.click_add_to_cart_1()
        allure.attach(page.screenshot(), name="add_first_product", attachment_type=allure.attachment_type.PNG)

    with allure.step("Continue shopping"):
        product_page.click_button_continue_shopping()
        allure.attach(page.screenshot(), name="continue_shopping", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add second product to cart"):
        product_page.click_add_to_cart_2()
        allure.attach(page.screenshot(), name="add_second_product", attachment_type=allure.attachment_type.PNG)

    with allure.step("View cart"):
        product_page.click_button_view_cart()
        allure.attach(page.screenshot(), name="view_cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify products in the cart"):
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["name"])
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["price"])
        expect(product_page.cart_quantity_1).to_contain_text("1")
        expect(product_page.form_of_product_at_cart_2).to_contain_text(details_of_wares_2["name"])
        expect(product_page.form_of_product_at_cart_2).to_contain_text(details_of_wares_2["price"])
        expect(product_page.cart_quantity_2).to_contain_text("1")
        allure.attach(page.screenshot(), name="cart_products", attachment_type=allure.attachment_type.PNG)


def test_verify_product_quantity_in_cart(test_before_each, page, product_page, details_of_wares, url_for_pages):
    with allure.step("Click View Product button"):
        product_page.click_button_view_ware()
        allure.attach(page.screenshot(), name="view_product", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify product details URL"):
        expect(page).to_have_url(url_for_pages["products_details_1"])
        allure.attach(page.screenshot(), name="product_details_url", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify product information on the details page"):
        expect(product_page.product_information).to_contain_text(details_of_wares["name"])
        expect(product_page.product_information).to_contain_text(details_of_wares["category"])
        expect(product_page.product_information).to_contain_text(details_of_wares["price"])
        expect(product_page.product_information).to_contain_text(details_of_wares["availability"])
        expect(product_page.product_information).to_contain_text(details_of_wares["condition"])
        expect(product_page.product_information).to_contain_text(details_of_wares["brand"])
        allure.attach(page.screenshot(), name="product_information_details", attachment_type=allure.attachment_type.PNG)

    with allure.step("Increase product quantity and add to cart"):
        product_page.increase_quantity_of_ware()
        product_page.click_button_add_to_cart()
        allure.attach(page.screenshot(), name="increase_quantity_add_to_cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("View cart and verify quantity"):
        product_page.click_button_view_cart()
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["name"])
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["price"])
        expect(product_page.cart_quantity_1).to_contain_text("4")
        allure.attach(page.screenshot(), name="verify_quantity_in_cart", attachment_type=allure.attachment_type.PNG)


def test_place_order_register_while_checkout(test_before_each, page, product_page, main_page, url_for_pages, register_user, fake, messages):
    with allure.step("Add product to cart and view cart"):
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        allure.attach(page.screenshot(), name="add_to_cart_view_cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Proceed to checkout"):
        product_page.click_button_proceed_to_checkout()
        allure.attach(page.screenshot(), name="proceed_to_checkout", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click on Login/Register button"):
        product_page.click_button_login_register()
        allure.attach(page.screenshot(), name="login_register_button", attachment_type=allure.attachment_type.PNG)

    with allure.step("Register new user during checkout"):
        register_user.register(fake.email(), fake.name())
        allure.attach(page.screenshot(), name="user_registration", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify account information form is visible"):
        expect(register_user.form_account_info).to_be_visible()
        allure.attach(page.screenshot(), name="account_info_form", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add user account data"):
        register_user.add_data_about_account()
        allure.attach(page.screenshot(), name="account_data_added", attachment_type=allure.attachment_type.PNG)

    with allure.step("Click continue after registration"):
        register_user.click_continue_button()
        allure.attach(page.screenshot(), name="continue_after_registration", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify user is logged in"):
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        allure.attach(page.screenshot(), name="user_logged_in", attachment_type=allure.attachment_type.PNG)

    with allure.step("Proceed to checkout"):
        product_page.click_button_cart()
        product_page.click_button_proceed_to_checkout()
        allure.attach(page.screenshot(), name="checkout_page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify address and review forms are visible"):
        expect(product_page.form_address_delivery).to_be_enabled()
        expect(product_page.form_address_invoice).to_be_enabled()
        expect(product_page.form_review_order).to_be_visible()
        allure.attach(page.screenshot(), name="address_review_forms", attachment_type=allure.attachment_type.PNG)

    with allure.step("Fill order description and place order"):
        product_page.fill_textarea_description()
        product_page.click_button_place_order()
        allure.attach(page.screenshot(), name="place_order", attachment_type=allure.attachment_type.PNG)

    with allure.step("Fill payment data and verify order"):
        product_page.fill_payment_data(fake.name(), fake.credit_card_number(), fake.credit_card_security_code(), fake.month(), fake.year())
        expect(product_page.form_order_congrats).to_contain_text(messages["card_congrats"])
        allure.attach(page.screenshot(), name="payment_order_congrats", attachment_type=allure.attachment_type.PNG)

    with allure.step("Delete user account"):
        main_page.click_delete_button()
        allure.attach(page.screenshot(), name="delete_account", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify account deleted"):
        expect(main_page.form_account_deleted).to_be_visible()
        allure.attach(page.screenshot(), name="account_deleted", attachment_type=allure.attachment_type.PNG)


def test_place_order_register_before_checkout(test_before_each, page, product_page, main_page, url_for_pages, register_user, fake, messages):
    with allure.step("Click Sign Up/Login button to register new user"):
        main_page.click_button_sign_up_login()
        allure.attach(page.screenshot(), name="signup_login", attachment_type=allure.attachment_type.PNG)

    with allure.step("Register new user with email and name"):
        register_user.register(fake.email(), fake.name())
        allure.attach(page.screenshot(), name="register_user", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify account info form is visible and add data"):
        expect(register_user.form_account_info).to_be_visible()
        register_user.add_data_about_account()
        allure.attach(page.screenshot(), name="account_info_form", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify congratulations message after successful registration"):
        expect(register_user.form_congrats).to_be_visible()
        register_user.click_continue_button()
        allure.attach(page.screenshot(), name="registration_congrats", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify user is logged in"):
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        allure.attach(page.screenshot(), name="user_logged_in", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add product to cart and proceed to checkout"):
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        expect(page).to_have_url(url_for_pages["cart"])
        product_page.click_button_proceed_to_checkout()
        allure.attach(page.screenshot(), name="proceed_to_checkout", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify address and review forms are visible"):
        expect(product_page.form_address_delivery).to_be_enabled()
        expect(product_page.form_address_invoice).to_be_enabled()
        expect(product_page.form_review_order).to_be_visible()
        allure.attach(page.screenshot(), name="address_review_forms", attachment_type=allure.attachment_type.PNG)

    with allure.step("Place order and fill payment details"):
        product_page.fill_textarea_description()
        product_page.click_button_place_order()
        product_page.fill_payment_data(fake.name(), fake.credit_card_number(), fake.credit_card_security_code(), fake.month(), fake.year())
        allure.attach(page.screenshot(), name="payment_details", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify order success message"):
        expect(product_page.form_order_congrats).to_contain_text(messages["card_congrats"])
        allure.attach(page.screenshot(), name="order_congrats", attachment_type=allure.attachment_type.PNG)

    with allure.step("Delete user account"):
        main_page.click_delete_button()
        allure.attach(page.screenshot(), name="delete_account", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify account deleted"):
        expect(main_page.form_account_deleted).to_be_visible()
        allure.attach(page.screenshot(), name="account_deleted", attachment_type=allure.attachment_type.PNG)


def test_place_order_login_before_checkout(test_before_each, page, product_page, main_page, url_for_pages, login_user, fake, messages, user_data):
    with allure.step("Click Sign Up/Login button to login user"):
        main_page.click_button_sign_up_login()
        allure.attach(page.screenshot(), name="signup_login", attachment_type=allure.attachment_type.PNG)

    with allure.step("Login with existing user credentials"):
        expect(main_page.sign_up_form).to_be_visible()
        login_user.login(user_data["email"], user_data["password"])
        allure.attach(page.screenshot(), name="user_login", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify user is logged in"):
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        allure.attach(page.screenshot(), name="user_logged_in", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add product to cart and proceed to checkout"):
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        expect(page).to_have_url(url_for_pages["cart"])
        product_page.click_button_proceed_to_checkout()
        allure.attach(page.screenshot(), name="proceed_to_checkout", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify address and review forms are visible"):
        expect(product_page.form_address_delivery).to_be_enabled()
        expect(product_page.form_address_invoice).to_be_enabled()
        expect(product_page.form_review_order).to_be_visible()
        allure.attach(page.screenshot(), name="address_review_forms", attachment_type=allure.attachment_type.PNG)

    with allure.step("Place order and fill payment details"):
        product_page.fill_textarea_description()
        product_page.click_button_place_order()
        product_page.fill_payment_data(fake.name(), fake.credit_card_number(), fake.credit_card_security_code(), fake.month(), fake.year())
        allure.attach(page.screenshot(), name="payment_details", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify order success message"):
        expect(product_page.form_order_congrats).to_contain_text(messages["card_congrats"])
        allure.attach(page.screenshot(), name="order_congrats", attachment_type=allure.attachment_type.PNG)


def test_remove_products_from_cart(test_before_each, page, product_page, url_for_pages):
    with allure.step("Add product to cart and view cart"):
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        expect(page).to_have_url(url_for_pages["cart"])
        allure.attach(page.screenshot(), name="view_cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Remove product from cart"):
        product_page.click_button_delete_from_cart()
        allure.attach(page.screenshot(), name="remove_from_cart", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify cart is empty"):
        expect(product_page.form_empty_cart).to_be_visible()
        expect(product_page.form_of_product_at_cart_1).not_to_be_visible()
        allure.attach(page.screenshot(), name="empty_cart", attachment_type=allure.attachment_type.PNG)


def test_view_category_products(test_before_each, page, product_page, names_of_categories):
    with allure.step("Verify and view Women category products"):
        expect(product_page.form_category).to_be_enabled()
        product_page.click_button_women_category()
        expect(product_page.title_of_category).to_have_text(names_of_categories["dresses"])
        allure.attach(page.screenshot(), name="women_category", attachment_type=allure.attachment_type.PNG)

    with allure.step("Verify and view Men category products"):
        product_page.click_button_men_category()
        expect(product_page.title_of_category).to_have_text(names_of_categories["tshirts"])
        allure.attach(page.screenshot(), name="men_category", attachment_type=allure.attachment_type.PNG)


def test_view_cart_brand_products(test_before_each, page, product_page, wares_of_polo, names_of_categories, url_for_pages, wares_of_h_and_m):
    with allure.step("View Polo brand products"):
        product_page.click_button_products()
        expect(product_page.form_brand).to_be_enabled()
        product_page.click_button_brand_polo()
        expect(page).to_have_url(url_for_pages["polo_page"])
        expect(product_page.title_of_category).to_contain_text(names_of_categories["polo"])
        expect(product_page.form_product_of_polo).to_contain_text(wares_of_polo["ware_of_polo_1"])
        allure.attach(page.screenshot(), name="polo_products", attachment_type=allure.attachment_type.PNG)

    with allure.step("View H&M brand products"):
        product_page.click_button_brand_h_and_m()
        expect(page).to_have_url(url_for_pages["h&m_page"])
        expect(product_page.title_of_category).to_contain_text(names_of_categories["h&m"])
        expect(product_page.form_product_of_polo).to_contain_text(wares_of_h_and_m["ware_of_h&m_1"])
        allure.attach(page.screenshot(), name="hm_products", attachment_type=allure.attachment_type.PNG)
def test_search_products_and_verify_cart_after_login(test_before_each, page, product_page, details_of_wares, user_data, url_for_pages, login_user, main_page):
    with allure.step("Click on Products button and verify products page"):
        product_page.click_button_products()
        expect(page).to_have_url(url_for_pages["products"])
        expect(product_page.list_of_wares).to_be_visible()
        allure.attach(page.screenshot(), name="products_page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Search for product and verify details"):
        product_page.search_for_ware(details_of_wares["name"])
        expect(product_page.form_of_product_information).to_contain_text(details_of_wares["name"])
        expect(product_page.form_of_product_information).to_contain_text(details_of_wares["price"])
        allure.attach(page.screenshot(), name="product_search_results", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add product to cart and view cart"):
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["name"])
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["price"])
        expect(product_page.cart_quantity_1).to_contain_text("1")
        allure.attach(page.screenshot(), name="view_cart_after_add", attachment_type=allure.attachment_type.PNG)

    with allure.step("Login and verify cart after login"):
        product_page.click_button_login_register_at_view_cart()
        expect(main_page.sign_up_form).to_be_visible()
        login_user.login(user_data["email"], user_data["password"])
        product_page.click_button_cart()
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["name"])
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["price"])
        expect(product_page.cart_quantity_1).to_contain_text("1")
        allure.attach(page.screenshot(), name="cart_after_login", attachment_type=allure.attachment_type.PNG)


def test_add_review_on_product(test_before_each, page, product_page, fake, url_for_pages):
    with allure.step("Navigate to product page and verify review section"):
        product_page.click_button_products()
        expect(page).to_have_url(url_for_pages["products"])
        expect(product_page.list_of_wares).to_be_visible()
        product_page.click_button_view_ware()
        expect(product_page.form_write_review).to_be_visible()
        allure.attach(page.screenshot(), name="product_page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Fill out and submit product review"):
        product_page.fill_review_from(fake.name(), fake.email(), fake.name())
        expect(product_page.message_successful_review).to_be_visible()
        allure.attach(page.screenshot(), name="review_submitted", attachment_type=allure.attachment_type.PNG)


def test_add_to_cart_from_recommended_items(test_before_each, page, product_page, details_of_wares):
    with allure.step("Scroll down and verify recommended items section"):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        expect(product_page.form_recomended_items).to_be_visible()
        allure.attach(page.screenshot(), name="recommended_items", attachment_type=allure.attachment_type.PNG)

    with allure.step("Add recommended product to cart and verify cart"):
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["name"])
        expect(product_page.form_of_product_at_cart_1).to_contain_text(details_of_wares["price"])
        expect(product_page.cart_quantity_1).to_contain_text("1")
        allure.attach(page.screenshot(), name="cart_after_recommended_add", attachment_type=allure.attachment_type.PNG)


def test_verify_address_details_in_checkout_page(test_before_each, page, main_page, register_user, fake, product_page, url_for_pages, messages):
    with allure.step("Register a new user and add product to cart"):
        main_page.click_button_sign_up_login()
        register_user.register(fake.email(), fake.name())
        expect(register_user.form_account_info).to_be_visible()
        register_user.add_data_about_account()
        expect(register_user.form_congrats).to_be_visible()
        register_user.click_continue_button()
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        expect(page).to_have_url(url_for_pages["cart"])
        allure.attach(page.screenshot(), name="cart_before_checkout", attachment_type=allure.attachment_type.PNG)

    with allure.step("Proceed to checkout and verify address details"):
        product_page.click_button_proceed_to_checkout()
        expect(product_page.form_address_delivery).to_be_enabled()
        expect(product_page.form_address_invoice).to_be_enabled()
        expect(product_page.form_review_order).to_be_visible()
        allure.attach(page.screenshot(), name="checkout_page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Place order and verify order confirmation"):
        product_page.fill_textarea_description()
        product_page.click_button_place_order()
        product_page.fill_payment_data(fake.name(), fake.credit_card_number(), fake.credit_card_security_code(), fake.month(), fake.year())
        expect(product_page.form_order_congrats).to_contain_text(messages["card_congrats"])
        allure.attach(page.screenshot(), name="order_confirmation", attachment_type=allure.attachment_type.PNG)

    with allure.step("Delete user account after order"):
        main_page.click_delete_button()
        expect(main_page.form_account_deleted).to_be_visible()
        allure.attach(page.screenshot(), name="account_deleted", attachment_type=allure.attachment_type.PNG)


def test_download_invoice_after_purchase_order(test_before_each, page, main_page, register_user, fake, product_page, url_for_pages, messages):
    with allure.step("Add product to cart and proceed to checkout"):
        product_page.click_add_to_cart_1()
        product_page.click_button_view_cart()
        expect(page).to_have_url(url_for_pages["cart"])
        product_page.click_button_proceed_to_checkout()
        product_page.click_button_login_register()
        register_user.register(fake.email(), fake.name())
        expect(register_user.form_account_info).to_be_visible()
        register_user.add_data_about_account()
        expect(register_user.form_congrats).to_be_visible()
        register_user.click_continue_button()
        expect(main_page.form_with_entry_message).to_contain_text("Logged in as")
        product_page.click_button_cart()
        product_page.click_button_proceed_to_checkout()
        expect(product_page.form_address_delivery).to_be_enabled()
        expect(product_page.form_address_invoice).to_be_enabled()
        expect(product_page.form_review_order).to_be_visible()
        allure.attach(page.screenshot(), name="checkout_page", attachment_type=allure.attachment_type.PNG)

    with allure.step("Place order and verify order confirmation"):
        product_page.fill_textarea_description()
        product_page.click_button_place_order()
        product_page.fill_payment_data(fake.name(), fake.credit_card_number(), fake.credit_card_security_code(), fake.month(), fake.year())
        expect(product_page.form_order_congrats).to_contain_text(messages["card_congrats"])
        allure.attach(page.screenshot(), name="order_confirmation", attachment_type=allure.attachment_type.PNG)

    with allure.step("Download invoice and verify file existence"):
        with page.expect_download() as download_info:
            product_page.click_button_download_invoice()
        download = download_info.value
        download_path = download.path()
        assert download_path is not None and os.path.exists(download_path)
        allure.attach(page.screenshot(), name="invoice_download", attachment_type=allure.attachment_type.PNG)

    with allure.step("Continue after order and delete account"):
        product_page.click_button_continue_after_order()
        main_page.click_delete_button()
        expect(main_page.form_account_deleted).to_be_visible()
        allure.attach(page.screenshot(), name="account_deleted", attachment_type=allure.attachment_type.PNG)
