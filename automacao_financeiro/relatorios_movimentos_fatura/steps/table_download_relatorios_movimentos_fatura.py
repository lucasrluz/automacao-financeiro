from playwright.sync_api import Page
from .util.elements_identifiers_relatorios_movimentos_fatura import GERAR_EXEL_BUTTON
from time import sleep

def table_download_relatorios_movimentos_fatura(page: Page):
    sleep(3)
    page.evaluate('(GERAR_EXEL_BUTTON) => document.querySelector(GERAR_EXEL_BUTTON).click()', GERAR_EXEL_BUTTON)