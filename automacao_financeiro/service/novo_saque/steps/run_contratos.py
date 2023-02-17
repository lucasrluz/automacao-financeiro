from playwright.sync_api import Page
from .util.elements_identifiers import (
    FILTER_INIT_DATE,
    FILTER_END_DATE,
    FILTER_BUTTON,
    REPORT_EMAIL_INPUT,
    REPORT_ENVIAR_BUTTON,
    REPORT_SOLICITAR_POR_EMAIL_BUTTON
)

def run_contratos(page: Page, date):
    # Seta os filtros com data inicial e data final
    page.type(FILTER_INIT_DATE, date['init_date']) # dd-mm-yyyy
    page.type(FILTER_END_DATE, date['end_date']) # dd-mm-yyyy

    # Clica para pesquisar
    page.click(FILTER_BUTTON)

    # Clica para enviar relatório pelo e-mail
    page.wait_for_timeout(3000)

    page.click(REPORT_SOLICITAR_POR_EMAIL_BUTTON)
    page.type(REPORT_EMAIL_INPUT, 'lucasr.luzbr@gmail.com')
    page.click(REPORT_ENVIAR_BUTTON)
