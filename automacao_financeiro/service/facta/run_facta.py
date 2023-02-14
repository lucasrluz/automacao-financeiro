from playwright.sync_api import Page
from .clientes_efetivados.run_clientes_efetivados import run_clientes_efetivados
from .relatorios_movimentos_fatura.run_relatorios_movimentos_fatura import run_relatorios_movimentos_fatura
from .relatorio_de_antencipacoes.run_relatorio_de_antecipacoes import run_relatorio_de_antecipacoes
from .login.login import login
from time import sleep
from .clientes_efetivados.steps.util.date import Date

def run_facta(page: Page, data: Date):
    page.goto('http://desenv.facta.com.br/sistemaNovo/login.php')
    
    login(page)

    # run_clientes_efetivados(page, data)

    # run_relatorios_movimentos_fatura(page, data)

    run_relatorio_de_antecipacoes(page, data)
