from playwright.sync_api import Page, sync_playwright
from .facta.run_facta import run_facta
from .novo_saque.run_novo_saque import run_novo_saque
from .capital_dois.run_capital_dois import run_capital_dois
import shutil
from time import sleep

playwright = sync_playwright().start()

def run_service(data, banks: list):
    browser = playwright.chromium.launch(headless=False, channel='chromium', downloads_path='/home/lucas/Projects/automacao-financeiro/relatorios')
    page = browser.new_page()

    date = {
        'init_date': data['init_date'],
        'end_date': data['end_date']
    }

    if banks[0] == 2:
        run_facta(page, date)
    
    if banks[1] == 2:
        run_novo_saque(page, date)
    
    if banks[2] == 2:
        run_capital_dois(page, date)

    sleep(8)
    shutil.rmtree('/home/lucas/Documents/relatorios')

    sleep(1)
    shutil.move(
        '/home/lucas/Projects/automacao-financeiro/relatorios',
        '/home/lucas/Documents'
    )
    sleep(1)
    page.close()