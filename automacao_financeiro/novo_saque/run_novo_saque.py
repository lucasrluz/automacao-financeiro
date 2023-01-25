from playwright.sync_api import Page
from novo_saque.steps.login import login
from novo_saque.steps.set_filter import set_filter

def run_novo_saque(page: Page):
    login(page)

    set_filter(page)