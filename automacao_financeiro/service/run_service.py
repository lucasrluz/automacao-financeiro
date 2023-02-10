from playwright.sync_api import Page, sync_playwright
from automacao_financeiro.facta.run_facta import run_facta
from automacao_financeiro.novo_saque.run_novo_saque import run_novo_saque
from automacao_financeiro.capital_dois.run_capital_dois import run_capital_dois
import shutil
from time import sleep

playwright = sync_playwright().start()

def run_service(data):
    browser = playwright.chromium.launch(headless=False, channel='chromium', downloads_path='/home/lucas/Projects/automacao-financeiro/relatorios')
    page = browser.new_page()

    date = {
        'init_date': data['init_date'],
        'end_date': data['end_date']
    }

    run_facta(page, date)
    
    run_novo_saque(page, date)

    run_capital_dois(page, date)

    sleep(5)
    shutil.rmtree('/home/lucas/Documents/relatorios')

    shutil.move(
        '/home/lucas/Projects/automacao-financeiro/relatorios',
        '/home/lucas/Documents'
    )