from playwright.sync_api import Page
from typing import TypedDict 
from automacao_financeiro.service.facta.util.elements_identifiers import (
    RELATORIOS_MOVIMENTOS_FATURA_BUTTON,
    PERIODO_INICIO,
    PERIODO_FIM,
    PESQUISAR_BUTTON,
    MENU,
    FACTA_FINANCEIRA,
    FINANCEIRO,
    GERAR_EXEL_BUTTON
)

class Date(TypedDict):
    init_date: str
    end_date: str

def run_relatorios_movimentos_fatura(page: Page, data: Date):
    # Vai para a página de movimentos fatura 
    page.wait_for_timeout(3000)
    
    page.wait_for_selector(MENU)
    page.click(MENU)
    page.wait_for_selector(FACTA_FINANCEIRA)
    page.click(FACTA_FINANCEIRA)
    page.wait_for_selector(FINANCEIRO)
    page.click(FINANCEIRO)
    page.wait_for_selector(RELATORIOS_MOVIMENTOS_FATURA_BUTTON)
    page.click(RELATORIOS_MOVIMENTOS_FATURA_BUTTON)

    # Adiciona o filtro de data inicial
    page.wait_for_selector(PERIODO_INICIO)
    page.evaluate(
        f'(PERIODO_INICIO) => document.querySelector(PERIODO_INICIO).value = "{data["init_date"]}"',
        PERIODO_INICIO
    )

    # Adiciona o filtro de data final
    page.wait_for_selector(PERIODO_FIM)
    page.evaluate(
        f'(PERIODO_FIM) => document.querySelector(PERIODO_FIM).value = "{data["end_date"]}"',
        PERIODO_FIM
    )

    # Clica no botão para fazer a pesquisa
    page.wait_for_selector(PESQUISAR_BUTTON)
    page.click(PESQUISAR_BUTTON)

    # Clica no botão para gerar excel
    page.wait_for_selector(GERAR_EXEL_BUTTON)
    page.click(GERAR_EXEL_BUTTON)