from playwright.sync_api import Page
from .util.elements_identifiers import (
    CLIENTES_EFETIVADOS,
    FILTER_DATA_INICIAL,
    FILTER_DATA_FINAL,
    FILTER_PESQUISAR_BUTTON,
    GERAR_CONSULTA_BUTTON
)
from time import sleep

def set_filters(page: Page):
    page.evaluate('(CLIENTES_EFETIVADOS) => document.querySelector(CLIENTES_EFETIVADOS).click()', CLIENTES_EFETIVADOS)

    sleep(5)
    page.evaluate('(FILTER_DATA_INICIAL) => document.querySelector(FILTER_DATA_INICIAL).value = "22/01/2023"', FILTER_DATA_INICIAL)
    page.evaluate('(FILTER_DATA_FINAL) => document.querySelector(FILTER_DATA_FINAL).value = "24/01/2023"', FILTER_DATA_FINAL)

    page.locator(FILTER_PESQUISAR_BUTTON).click()

    page.locator(GERAR_CONSULTA_BUTTON).click()