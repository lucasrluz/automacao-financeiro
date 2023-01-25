from playwright.sync_api import Page
from dotenv import dotenv_values
from .util.element_identifiers_login import (
    LOGIN_USERNAME,
    LOGIN_PASSWORD,
    LOGIN_BUTTON_SUBMIT
)

env = dotenv_values('.env')

def login(page: Page):
    page.locator(LOGIN_USERNAME).type(env['USERNAME'])
    page.locator(LOGIN_PASSWORD).type(env['PASSWORD'])
    page.evaluate('(LOGIN_BUTTON_SUBMIT) => document.querySelector(LOGIN_BUTTON_SUBMIT).click()', LOGIN_BUTTON_SUBMIT)