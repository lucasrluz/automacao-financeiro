from playwright.sync_api import Page
from .steps.login import login
from .steps.run_contratos import run_contratos

def run_novo_saque(page: Page, date):
    page.goto('https://nsaque.ultragate.com.br/login')
    
    login(page)

    run_contratos(page, date)