from playwright.sync_api import Page
from .util.elements_identifiers_relatorios_movimentos_fatura import GERAR_EXEL_BUTTON
from time import sleep
import shutil

def table_download_relatorios_movimentos_fatura(page: Page):
    page.wait_for_selector(GERAR_EXEL_BUTTON)
    page.click(GERAR_EXEL_BUTTON)

    sleep(5)
    shutil.rmtree('/home/lucas/Documents/relatorios')

    shutil.move(
        '/home/lucas/Projects/automacao-financeiro/relatorios',
        '/home/lucas/Documents'
    )