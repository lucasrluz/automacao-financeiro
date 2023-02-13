from playwright.sync_api import Page
from .util.elements_identifiers_relatorios_movimentos_fatura import (
    RELATORIOS_MOVIMENTOS_FATURA_BUTTON,
    PERIODO_INICIO,
    PERIODO_FIM,
    PESQUISAR_BUTTON,
    MENU,
    FACTA_FINANCEIRA,
    FINANCEIRO
)
from .util.date import Date

def set_filters_relatorios_movimentos_fatura(page: Page, date: Date):
    page.wait_for_timeout(10000)
    
    page.click(MENU)
    page.click(FACTA_FINANCEIRA)
    page.click(FINANCEIRO)

    page.wait_for_selector(RELATORIOS_MOVIMENTOS_FATURA_BUTTON)
    page.click(RELATORIOS_MOVIMENTOS_FATURA_BUTTON)

    page.wait_for_selector(PERIODO_INICIO)
    page.evaluate(
        f'(PERIODO_INICIO) => document.querySelector(PERIODO_INICIO).value = "{date["init_date"]}"',
        PERIODO_INICIO
    )

    page.wait_for_selector(PERIODO_FIM)
    page.evaluate(
        f'(PERIODO_FIM) => document.querySelector(PERIODO_FIM).value = "{date["end_date"]}"',
        PERIODO_FIM
    )

    page.wait_for_selector(PESQUISAR_BUTTON)
    page.click(PESQUISAR_BUTTON)