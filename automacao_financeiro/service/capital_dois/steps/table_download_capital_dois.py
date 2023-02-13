from playwright.sync_api import Page
from .util.elements_identifiers_capital_dois import GERAR_EXCEL

def table_download_capital_dois(page: Page):
    page.click(GERAR_EXCEL)