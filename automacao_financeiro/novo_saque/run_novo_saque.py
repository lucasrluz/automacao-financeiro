from playwright.sync_api import Page
from novo_saque.steps.login import login
from novo_saque.steps.set_filter import set_filter
from novo_saque.steps.table_download_novo_saque import table_download_novo_saque
from time import sleep

def run_novo_saque(page: Page):
    page.goto('https://nsaque.ultragate.com.br/login')
    
    login(page)

    set_filter(page)

    table_download_novo_saque(page)