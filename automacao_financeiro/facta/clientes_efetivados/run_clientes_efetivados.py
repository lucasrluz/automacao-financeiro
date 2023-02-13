from playwright.sync_api import Page
from .steps.set_filters_clientes_efetivados import set_filters_clientes_efetivados
from .steps.table_download_clientes_efetivados import table_download_clientes_efetivados
from .steps.util.date import Date

def run_clientes_efetivados(page: Page, date: Date):    
    set_filters_clientes_efetivados(page, date)
    
    table_download_clientes_efetivados(page)