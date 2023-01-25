from playwright.sync_api import Page
from .clientes_efetivados.run_clientes_efetivados import run_clientes_efetivados
from .relatorios_movimentos_fatura.run_relatorios_movimentos_fatura import run_relatorios_movimentos_fatura
from .login.login import login

def run_facta(page: Page):
    login(page)

    run_clientes_efetivados(page)

    run_relatorios_movimentos_fatura(page)