from playwright.sync_api import Page
from .steps.run_relatorios_movimentos_fatura import run_relatorios_movimentos_fatura
from .steps.run_relatorio_de_antecipacoes import run_relatorio_de_antecipacoes
from .steps.login import login
from time import sleep
from .util.elements_identifiers import BUTTON_ID

def run_facta(page: Page, data: dict):
    # Vai para a página de login do banco facta
    page.goto('http://desenv.facta.com.br/sistemaNovo/login.php')
    
    # Faz o login no banco facta
    login(page)

    # Fecha notificação
    page.wait_for_timeout(5000)
    page.click(BUTTON_ID)

    # Roda parte de movimentos fatura
    run_relatorios_movimentos_fatura(page, data)

    # Roda pate de relatórios de antecipação
    run_relatorio_de_antecipacoes(page, data)
