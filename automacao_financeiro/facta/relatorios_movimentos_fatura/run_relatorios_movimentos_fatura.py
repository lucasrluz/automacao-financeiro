from playwright.sync_api import Page
from facta.relatorios_movimentos_fatura.steps.set_filters_relatorios_movimentos_fatura import set_filters_relatorios_movimentos_fatura
from facta.relatorios_movimentos_fatura.steps.table_download_relatorios_movimentos_fatura import table_download_relatorios_movimentos_fatura
from time import sleep

def run_relatorios_movimentos_fatura(page: Page):
    sleep(5)
    set_filters_relatorios_movimentos_fatura(page)

    table_download_relatorios_movimentos_fatura(page)