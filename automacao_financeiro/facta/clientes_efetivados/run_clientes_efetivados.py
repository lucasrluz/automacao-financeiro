from playwright.sync_api import Page
from facta.clientes_efetivados.steps.set_filters_clientes_efetivados import set_filters_clientes_efetivados
from facta.clientes_efetivados.steps.table_download_clientes_efetivados import table_download_clientes_efetivados
from time import sleep

def run_clientes_efetivados(page: Page):    
    sleep(5)
    set_filters_clientes_efetivados(page)
    
    table_download_clientes_efetivados(page)