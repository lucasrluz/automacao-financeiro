from playwright.sync_api import Page
from .util.elements_identifiers_clientes_efetivados import (
    GERAR_CONSULTA_BUTTON
)

def table_download_clientes_efetivados(page: Page):
    page.locator(GERAR_CONSULTA_BUTTON).click()