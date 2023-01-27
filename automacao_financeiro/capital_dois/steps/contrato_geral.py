from playwright.sync_api import Page
from capital_dois.steps.util.elements_identifiers_capital_dois import (
    PRODUCAO,
    CONTRATOS_GERAL
)

def contrato_geral(page: Page):
    page.click(PRODUCAO)
    page.click(CONTRATOS_GERAL)