from playwright.sync_api import Page
from .util.elements_identifiers_relatorios_movimentos_fatura import (
    RELATORIOS_MOVIMENTOS_FATURA_BUTTON,
    PERIODO_INICIO,
    PERIODO_FIM,
    PESQUISAR_BUTTON,
)
from time import sleep

def set_filters_relatorios_movimentos_fatura(page: Page):
    page.evaluate('(RELATORIOS_MOVIMENTOS_FATURA_BUTTON) => document.querySelector(RELATORIOS_MOVIMENTOS_FATURA_BUTTON).click()', RELATORIOS_MOVIMENTOS_FATURA_BUTTON)

    sleep(5)

    page.evaluate('(PERIODO_INICIO) => document.querySelector(PERIODO_INICIO).value = "15/01/2023"', PERIODO_INICIO)
    page.evaluate('(PERIODO_FIM) => document.querySelector(PERIODO_FIM).value = "24/01/2023"', PERIODO_FIM)
    page.evaluate('(PESQUISAR_BUTTON) => document.querySelector(PESQUISAR_BUTTON).click()', PESQUISAR_BUTTON)