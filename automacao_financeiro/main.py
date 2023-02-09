from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
from facta.run_facta import run_facta
from novo_saque.run_novo_saque import run_novo_saque
from capital_dois.run_capital_dois import run_capital_dois
from time import sleep

load_dotenv()

facta_data = {
    'clientes_efetivados': {
        'init_date': '05/02/2023',
        'end_date': '09/02/2023'
    },
    'relatorios_movimentos_fatura': {
        'init_date': '05/02/2023',
        'end_date': '09/02/2023'
    }
}

def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium', downloads_path='.')
    page = browser.new_page()

    run_facta(page, facta_data)
    
    run_novo_saque(page)

    run_capital_dois(page)
    sleep(1000000)

with sync_playwright() as playwright:
    main(playwright)
