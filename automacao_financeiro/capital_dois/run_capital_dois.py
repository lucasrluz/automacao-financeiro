from playwright.sync_api import Page
from .steps.login import login
from .steps.contrato_geral import contrato_geral
from .steps.table_download_capital_dois import table_download_capital_dois

def run_capital_dois(page: Page, date):
    page.goto('https://capital2.multsistema.com.br/index.php')

    login(page)

    contrato_geral(page, date)

    table_download_capital_dois(page)
