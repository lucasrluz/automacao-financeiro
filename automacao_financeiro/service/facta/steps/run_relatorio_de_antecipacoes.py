from playwright.sync_api import Page
from typing import TypedDict
from automacao_financeiro.service.facta.util.elements_identifiers import (
    MENU,
    FACTA_FINANCEIRA,
    FINANCEIRO,
    RELATORIO_DE_ANTECIPACOES,
    MONTH,
    YEAR,
    PESQUISAR_BUTTON_ANTECIPACAO
)

class Date(TypedDict):
    init_date: str
    end_date: str

def run_relatorio_de_antecipacoes(page: Page, date: Date):
    # Formatação de data para os filtros
    month = date['end_date'][3:5]
    year = date['end_date'][6:10]

    # Vai para a página de relatorio de antecipações
    page.wait_for_timeout(3000)

    page.wait_for_selector(MENU)
    page.click(MENU)
    page.wait_for_selector(FACTA_FINANCEIRA)
    page.click(FACTA_FINANCEIRA)
    page.wait_for_selector(FINANCEIRO)
    page.click(FINANCEIRO)
    page.wait_for_selector(RELATORIO_DE_ANTECIPACOES)
    page.click(RELATORIO_DE_ANTECIPACOES)

    # Seta o filtro de mês
    page.wait_for_selector(MONTH)
    page.evaluate(
        f'(MONTH) => document.querySelector(MONTH).value = "{month}"',
        MONTH
    )

    # Seta o filtro de ano
    page.wait_for_selector(YEAR)
    page.evaluate(
        f'(YEAR) => document.querySelector(YEAR).value = "{year}"',
        YEAR
    )

    # Clica no botão para realizar pesquisa
    page.click(PESQUISAR_BUTTON_ANTECIPACAO)

    # Clica nos botões para gerar excel
    page.wait_for_timeout(5000)
    i = 1
    while True:
        ID_GERAR_EXCEL = f'#tabelaRelatorio > tbody > tr:nth-child({i}) > td:nth-child(6) > a > span' 

        element = page.evaluate(
            '(ID_GERAR_EXCEL) => document.querySelector(ID_GERAR_EXCEL)',
            ID_GERAR_EXCEL
        )

        if element == None:
            break

        page.click(ID_GERAR_EXCEL)

        i += 1