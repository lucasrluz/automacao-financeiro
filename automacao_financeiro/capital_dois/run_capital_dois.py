from playwright.sync_api import Page
from capital_dois.steps.login import login
from capital_dois.steps.contrato_geral import contrato_geral

def run_capital_dois(page: Page):
    page.goto('https://capital2.multsistema.com.br/index.php')

    login(page)

    contrato_geral(page)


