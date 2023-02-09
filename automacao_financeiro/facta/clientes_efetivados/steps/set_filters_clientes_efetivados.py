from playwright.sync_api import Page
from .util.elements_identifiers_clientes_efetivados import (
    CLIENTES_EFETIVADOS,
    FILTER_DATA_INICIAL,
    FILTER_DATA_FINAL,
    FILTER_PESQUISAR_BUTTON,
    MENU,
    OPERACIONAL,
    CONSULTAS
)
from .util.date import Date

def set_filters_clientes_efetivados(page: Page, date: Date):
    page.wait_for_timeout(10000)

    page.click(MENU)
    page.click(OPERACIONAL)
    page.click(CONSULTAS)
    page.click(CLIENTES_EFETIVADOS)

    page.wait_for_selector(FILTER_DATA_INICIAL)
    page.evaluate(
        f'(FILTER_DATA_INICIAL) => document.querySelector(FILTER_DATA_INICIAL).value = "{date["init_date"]}"',
        FILTER_DATA_INICIAL
    )

    page.wait_for_selector(FILTER_DATA_FINAL)
    page.evaluate(
        f'(FILTER_DATA_FINAL) => document.querySelector(FILTER_DATA_FINAL).value = "{date["end_date"]}"',
        FILTER_DATA_FINAL
    )

    page.wait_for_selector(FILTER_PESQUISAR_BUTTON)
    page.click(FILTER_PESQUISAR_BUTTON)