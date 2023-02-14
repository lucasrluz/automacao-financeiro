from playwright.sync_api import Page
from .util.elements_identifiers_relatorio_de_antecipacoes import (
    MENU,
    FACTA_FINANCEIRA,
    FINANCEIRO,
    RELATORIO_DE_ANTECIPACOES,
    MONTH,
    YEAR,
    PESQUISAR_BUTTON
)

def set_filters_ralatorio_movimento_fatura(page: Page):
    page.wait_for_timeout(10000)
    page.click(MENU)
    page.click(FACTA_FINANCEIRA)
    page.click(FINANCEIRO)
    page.click(RELATORIO_DE_ANTECIPACOES)

    page.wait_for_selector(MONTH)
    page.evaluate(
        '(MONTH) => document.querySelector(MONTH).value = "02"',
        MONTH
    )

    page.wait_for_selector(YEAR)
    page.evaluate(
        '(YEAR) => document.querySelector(YEAR).value = "2023"',
        YEAR
    )

    page.click(PESQUISAR_BUTTON)
