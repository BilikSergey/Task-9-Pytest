from playwright.sync_api import Page 
from pages.main_page import Main_page

class Product_page:
    def __init__(self, page: Page):
        self.page = page
        self.main_page = Main_page(page)
        self.button_products = page.locator('(//a[@href="/products"])')
        self.list_of_wares = page.locator('(//*[@class="features_items"])')
        self.button_view_ware = page.locator('(//a[@href="/product_details/1"])[1]')
        self.product_information = page.locator('(//*[@class="product-information"])')
        self.input_search = page.locator('(//*[@id="search_product"])')
        self.button_submit_search = page.locator('(//*[@id="submit_search"])')
        self.form_of_product_information = page.locator('(//*[@class="productinfo text-center"])')
        self.add_to_cart_1 = page.locator('(//*[@data-product-id="1"])[1]')
        self.add_to_cart_2 = page.locator('(//*[@data-product-id="2"])[1]')
        self.button_continue_shopping = page.locator('(//*[@class="btn btn-success close-modal btn-block"])')
        self.form_of_product_at_cart_1 = page.locator('(//*[@id="product-1"])')
        self.form_of_product_at_cart_2 = page.locator('(//*[@id="product-2"])')
        self.cart_quantity_1 = page.locator('//*[@id="product-1"]//td[@class="cart_quantity"]//button')
        self.cart_quantity_2 = page.locator('//*[@id="product-2"]//td[@class="cart_quantity"]//button')
        self.input_quantity = page.locator('//*[@id="quantity"]')
        self.button_add_to_cart = page.locator('//*[@class="btn btn-default cart"]')
        self.button_proceed_to_checkout = page.locator('//*[@class="btn btn-default check_out"]')
        self.form_address_delivery = page.locator('//*[@id="address_delivery"]')
        self.form_address_invoice = page.locator('//*[@id="address_invoice"]')
        self.form_review_order = page.locator('//*[@class="step-one"][2]')
        self.textarea_description = page.locator('//*[@class="form-control"]')
        self.button_cart = page.locator('(//a[@href="/view_cart"])[1]')
        self.button_view_cart = page.locator('(//a[@href="/view_cart"])[2]')
        self.button_place_order = page.locator('(//a[@href="/payment"])')
        self.input_name_on_card = page.locator('(//*[@name="name_on_card"])')
        self.input_card_number = page.locator('(//*[@name="card_number"])')
        self.input_cvc = page.locator('(//*[@name="cvc"])')
        self.input_expiry_month = page.locator('(//*[@name="expiry_month"])')
        self.input_expiry_year = page.locator('(//*[@name="expiry_year"])')
        self.button_pay_confirm_order = page.locator('(//*[@id="submit"])')
        self.form_order_congrats = page.locator('(//*[@class="col-sm-9 col-sm-offset-1"])')
        self.button_delete_from_cart = page.locator('(//*[@class="cart_quantity_delete"])')
        self.button_login_register = page.locator('(//a[@href="/login"])[2]')
        self.button_login_register_at_view_cart = page.locator('(//a[@href="/login"])[1]')
        self.form_empty_cart = page.locator('(//*[@id="empty_cart"])')
        self.form_category = page.locator('(//*[@id="accordian"])')
        self.button_women_category = page.locator('(//*[@href="#Women"])')
        self.button_dress = page.locator('//a[@href="/category_products/1"]')
        self.title_of_category = page.locator('//*[@class="title text-center"]')
        self.button_men_category = page.locator('(//*[@href="#Men"])')
        self.button_tshirts = page.locator('//a[@href="/category_products/3"]')
        self.form_brand = page.locator('//*[@class="brands_products"]')
        self.button_brand_polo = page.locator('//a[@href="/brand_products/Polo"]')
        self.form_product_of_polo = page.locator('//*[@class="features_items"]')
        self.button_brand_h_and_m = page.locator('//a[@href="/brand_products/H&M"]')
        self.form_write_review = page.locator('//*[@class="category-tab shop-details-tab"]')
        self.input_email_review = page.locator('//*[@id="email"]')
        self.input_name_review = page.locator('//*[@id="name"]')
        self.input_review = page.locator('//*[@id="review"]')
        self.button_review = page.locator('//*[@id="button-review"]')
        self.message_successful_review = page.locator('(//*[@class="alert-success alert"])[1]')
        self.form_recomended_items = page.locator('(//*[@class="recommended_items"])')
        self.button_download_invoice = page.locator('(//*[@class="btn btn-default check_out"])')
        self.button_continue_after_order = page.locator('(//*[@class="btn btn-primary"])')

    def fill_payment_data(self, name_on_card: str, card_number: str, cvc: str, expiry_month: str, expiry_year: str) -> None:
        self.input_name_on_card.type(name_on_card)
        self.input_card_number.type(card_number)
        self.input_cvc.type(cvc)
        self.input_expiry_month.type(expiry_month)
        self.input_expiry_year.type(expiry_year)
        self.button_pay_confirm_order.click()

    def click_button_products(self) -> None:
        self.button_products.click()

    def click_button_continue_after_order(self) -> None:
        self.button_continue_after_order.click()

    def click_button_download_invoice(self) -> None:
        self.button_download_invoice.click()

    def fill_review_from(self, name: str, email:str, description: str) -> None:
        self.input_name_review.type(name)
        self.input_email_review.type(email)
        self.input_review.type(description)
        self.button_review.click()

    def click_button_brand_h_and_m(self) -> None:
        self.button_brand_h_and_m.click()

    def click_button_brand_polo(self) -> None:
        self.button_brand_polo.click()

    def click_button_login_register_at_view_cart(self) -> None:
        self.button_login_register_at_view_cart.click()

    def click_button_login_register(self) -> None:
        self.button_login_register.click()

    def click_button_view_ware(self) -> None:
        self.button_view_ware.click()

    def search_for_ware(self, ware_name: str) -> None:
        self.input_search.type(ware_name)
        self.button_submit_search.click()

    def click_button_cart(self) -> None:
        self.button_cart.click()

    def click_button_delete_from_cart(self) -> None:
        self.button_delete_from_cart.click()

    def click_add_to_cart_1(self) -> None:
        self.add_to_cart_1.click()

    def click_button_women_category(self) -> None:
        self.button_women_category.click()
        self.button_dress.click()

    def click_button_men_category(self) -> None:
        self.button_men_category.click()
        self.button_tshirts.click()

    def click_add_to_cart_2(self) -> None:
        self.add_to_cart_2.click()

    def click_button_continue_shopping(self) -> None:
        self.button_continue_shopping.click()

    def click_button_view_cart(self) -> None:
        self.button_view_cart.click()

    def click_button_add_to_cart(self) -> None:
        self.button_add_to_cart.click()

    def click_button_proceed_to_checkout(self) -> None:
        self.button_proceed_to_checkout.click()

    def click_button_place_order(self) -> None:
        self.button_place_order.click()

    def fill_textarea_description(self) -> None:
        self.textarea_description.type("some description for wares")

    def increase_quantity_of_ware(self) -> None:
        self.input_quantity.type("4")  