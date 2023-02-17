from playwright.sync_api import Page
from .steps.login import login
from .steps.contrato_geral import contrato_geral

def run_capital_dois(page: Page, date):
    page.goto('https://capital2.multsistema.com.br/index.php')

    login(page)

    contrato_geral(page, date)