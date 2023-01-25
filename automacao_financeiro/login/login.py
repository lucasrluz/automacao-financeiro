from playwright.sync_api import Page
from .util.element_identifiers_login import (
    LOGIN_USERNAME,
    LOGIN_PASSWORD,
    LOGIN_BUTTON_SUBMIT
)

def login(page: Page):
    page.locator(LOGIN_USERNAME).type('92254_anafernande')
    page.locator(LOGIN_PASSWORD).type('Agilizza23*')
    page.evaluate('(LOGIN_BUTTON_SUBMIT) => document.querySelector(LOGIN_BUTTON_SUBMIT).click()', LOGIN_BUTTON_SUBMIT)