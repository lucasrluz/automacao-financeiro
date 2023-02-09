from playwright.sync_api import Page
from .clientes_efetivados.run_clientes_efetivados import run_clientes_efetivados
from .relatorios_movimentos_fatura.run_relatorios_movimentos_fatura import run_relatorios_movimentos_fatura
from .login.login import login
from time import sleep
from .clientes_efetivados.steps.util.clientes_fetivados_and_relatorios_movimento_fatura import ClientesEfetivadosAndRelatoriosMovimentoFatura

def run_facta(page: Page, data: ClientesEfetivadosAndRelatoriosMovimentoFatura):
    page.goto('http://desenv.facta.com.br/sistemaNovo/login.php')
    
    login(page)

    run_clientes_efetivados(page, data['clientes_efetivados'])

    run_relatorios_movimentos_fatura(page, data['relatorios_movimentos_fatura'])