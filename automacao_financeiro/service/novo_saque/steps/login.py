from playwright.sync_api import Page
from dotenv import dotenv_values
from .util.elements_identifiers import (
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_SUBMIT_BUTTON
)

env = dotenv_values()

def login(page: Page):
    page.type(LOGIN_EMAIL_INPUT, env['USERNAME_NOVO_SAQUE'])
    page.type(LOGIN_PASSWORD_INPUT, env['PASSWORD_NOVO_SAQUE'])
    page.click(LOGIN_SUBMIT_BUTTON)