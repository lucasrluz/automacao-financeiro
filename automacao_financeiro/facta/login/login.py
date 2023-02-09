from playwright.sync_api import Page
from dotenv import dotenv_values
from .util.element_identifiers_login import (
    LOGIN_USERNAME,
    LOGIN_PASSWORD,
    LOGIN_BUTTON_SUBMIT
)

env = dotenv_values('.env')

def login(page: Page):
    page.wait_for_selector(LOGIN_USERNAME)
    page.type(LOGIN_USERNAME, env['USERNAME'])

    page.wait_for_selector(LOGIN_PASSWORD)
    page.type(LOGIN_PASSWORD, env['PASSWORD'])

    page.wait_for_selector(LOGIN_BUTTON_SUBMIT)
    page.click(LOGIN_BUTTON_SUBMIT)