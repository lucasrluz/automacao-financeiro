from playwright.sync_api import Page
from dotenv import dotenv_values
from .util.elements_identifiers_capital_dois import (
    PRODUCAO,
    CONTRATOS_GERAL,
    PASSWORD_RELATORIO,
    RELATORIO_BUTTON,
    INIT_DATE,
    GERAR_EXCEL
)

env = dotenv_values()

def contrato_geral(page: Page, date):
    # Vai para o menu de contratos gerais
    page.wait_for_selector(PRODUCAO)
    page.evaluate(
        '(CONTRATOS_GERAL) => document.querySelector(CONTRATOS_GERAL).click()',
        CONTRATOS_GERAL
    )

    # Seta a senha para entrar na página de relatórios
    page.type(PASSWORD_RELATORIO, env['PASSWORD_RELATORIO'])
    page.click(RELATORIO_BUTTON)

    # Seta os filtro de data inicial
    page.wait_for_selector(INIT_DATE)

    page.evaluate(f'() => document.querySelector("#datai").value = "{date["init_date"]}"')

    # Clica para gerar excel
    page.click(GERAR_EXCEL)
