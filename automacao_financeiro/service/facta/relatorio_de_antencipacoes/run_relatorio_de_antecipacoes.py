from .steps.set_filters_relatorios_de_antecipacoes import set_filters_ralatorio_movimento_fatura
from .steps.table_download_relatorios_de_antecipacoes import table_download_relatorio_de_antecipacoes
from playwright.sync_api import Page

def run_relatorio_de_antecipacoes(page: Page, data):
    set_filters_ralatorio_movimento_fatura(page)

    table_download_relatorio_de_antecipacoes(page)