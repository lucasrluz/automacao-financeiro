from playwright.sync_api import Page
from .steps.login import login
from .steps.set_filter import set_filter
from .steps.table_download_novo_saque import table_download_novo_saque
from time import sleep

def run_novo_saque(page: Page, date):
    page.goto('https://nsaque.ultragate.com.br/login')
    
    login(page)

    set_filter(page, date)

    table_download_novo_saque(page)