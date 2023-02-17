from playwright.sync_api import Page, sync_playwright
from .facta.run_facta import run_facta
from .novo_saque.run_novo_saque import run_novo_saque
from .capital_dois.run_capital_dois import run_capital_dois
import shutil
from time import sleep
import os

playwright = sync_playwright().start()

def run_service(data, view_browser: str, banks: list):
    value = True

    if view_browser == '2':
        value = False
    
    browser = playwright.chromium.launch(headless=value, channel='chromium', downloads_path='/home/lucas/Projects/automacao-financeiro/relatorios')
    page = browser.new_page()

    date = {
        'init_date': data['init_date'],
        'end_date': data['end_date']
    }

    if banks[0] == 0 and banks[1] == 0 and banks[2] == 0:
        page.close()
        return

    if banks[0] == 2:
        run_facta(page, date)
    
    if banks[1] == 2:
        run_novo_saque(page, date)
    
    if banks[2] == 2:
        run_capital_dois(page, date)

    # Renomeia arquivos baixados e move eles para outro diretório
    page.wait_for_timeout(5000)
    
    files = os.listdir('./relatorios')

    for file in files:
        new_name = file + '.xls'
        os.rename('./relatorios/' + file, './relatorios/' + new_name)

    files_for_move = os.listdir('./relatorios')

    for file in files_for_move:
        shutil.move('./relatorios/' + file, '/home/lucas/Documentos/relatorios')

    page.close()