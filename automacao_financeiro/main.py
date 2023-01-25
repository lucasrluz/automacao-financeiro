from playwright.sync_api import Playwright, sync_playwright
from clientes_efetivados.run_clientes_efetivados import run_clientes_efetivados
from relatorios_movimentos_fatura.run_relatorios_movimentos_fatura import run_relatorios_movimentos_fatura
from login.login import login
from time import sleep

def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium', downloads_path='.')
    page = browser.new_page()
    page.goto('http://desenv.facta.com.br/sistemaNovo/login.php')

    login(page)

    run_clientes_efetivados(page)

    run_relatorios_movimentos_fatura(page)

    sleep(1000000)

with sync_playwright() as playwright:
    main(playwright)
