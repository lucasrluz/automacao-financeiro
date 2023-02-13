from playwright.sync_api import Page
from .steps.set_filters_relatorios_movimentos_fatura import set_filters_relatorios_movimentos_fatura
from .steps.table_download_relatorios_movimentos_fatura import table_download_relatorios_movimentos_fatura
from .steps.util.date import Date

def run_relatorios_movimentos_fatura(page: Page, data: Date):
    set_filters_relatorios_movimentos_fatura(page, data)

    table_download_relatorios_movimentos_fatura(page)