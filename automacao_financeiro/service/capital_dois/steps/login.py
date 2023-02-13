from playwright.sync_api import Page
from dotenv import dotenv_values
from .util.elements_identifiers_capital_dois import (
    LOGIN_USERNAME_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON,
    ACEITAR_COOKIES
)

env = dotenv_values()

def login(page: Page):
    page.click(ACEITAR_COOKIES)
    page.type(LOGIN_USERNAME_INPUT, env['USERNAME_CAPITAL_DOIS'])
    page.type(LOGIN_PASSWORD_INPUT, env['PASSWORD_CAPITAL_DOIS'])
    page.click(LOGIN_BUTTON)