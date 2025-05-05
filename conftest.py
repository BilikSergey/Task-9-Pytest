import pytest
from playwright.sync_api import sync_playwright
import json
from pathlib import Path
from pages.login_page import Login_user
from pages.register_page import Register_user
from pages.basic_pages_page import Basic_pages
from pages.product_page import Product_page
from pages.main_page import Main_page
from faker import Faker

import pytest

@pytest.fixture(scope="function")
def browser_context_args():
    return {"viewport": {"width": 1280, "height": 720}} 

@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": True} 

@pytest.fixture(scope="function")
def page(browser_type, browser_type_launch_args):
    browser = browser_type.launch(**browser_type_launch_args)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture
def user_data():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["valid_user"]

@pytest.fixture
def url_for_pages():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["url"]

@pytest.fixture
def details_of_wares():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["details_of_wares"]

@pytest.fixture
def details_of_wares_2():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["details_of_wares_2"]

@pytest.fixture
def messages():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["messages"]

@pytest.fixture
def wares_of_polo():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["wares_of_polo"]

@pytest.fixture
def wares_of_h_and_m():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["wares_of_h&m"]

@pytest.fixture
def names_of_categories():
    with open(Path(__file__).parent / "data/test_data.json") as f:
        return json.load(f)["names_of_categories"]

@pytest.fixture
def fake():
    return Faker()

@pytest.fixture
def login_user(page):
    return Login_user(page)

@pytest.fixture
def register_user(page):
    return Register_user(page)

@pytest.fixture
def basic_pages(page):
    return Basic_pages(page)

@pytest.fixture
def product_page(page):
    return Product_page(page)

@pytest.fixture
def main_page(page):
    return Main_page(page)
