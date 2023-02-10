from playwright.sync_api import Page, sync_playwright
from automacao_financeiro.facta.run_facta import run_facta

playwright = sync_playwright().start()

def run_service(data):
    browser = playwright.chromium.launch(headless=False, channel='chromium', downloads_path='/home/lucas/Projects/automacao-financeiro/relatorios')
    page = browser.new_page()

    date = {
        'init_date': data['init_date'],
        'end_date': data['end_date']
    }

    run_facta(page, date)
    
    # run_novo_saque(page)

    # run_capital_dois(page)