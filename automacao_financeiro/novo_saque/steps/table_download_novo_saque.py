from playwright.sync_api import Page
from time import sleep
from .util.elements_identifiers import (
    REPORT_EMAIL_INPUT,
    REPORT_ENVIAR_BUTTON,
    REPORT_SOLICITAR_POR_EMAIL_BUTTON
)

def table_download_novo_saque(page: Page):
    sleep(3)

    page.click(REPORT_SOLICITAR_POR_EMAIL_BUTTON)
    page.type(REPORT_EMAIL_INPUT, 'lucasr.luzbr@gmail.com')
    page.click(REPORT_ENVIAR_BUTTON)
