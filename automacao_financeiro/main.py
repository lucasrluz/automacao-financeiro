from playwright.sync_api import Playwright, sync_playwright
from clientes_efetivados.run_clientes_efetivados import run_clientes_efetivados
from login.login import login
from relatorios_movimentos_fatura.set_filters_relatorios_movimentos_fatura import set_filters_relatorios_movimentos_fatura
from time import sleep

def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium')
    page = browser.new_page()
    page.goto('http://desenv.facta.com.br/sistemaNovo/login.php')

    login(page)

    run_clientes_efetivados(page)

    sleep(5)
    set_filters_relatorios_movimentos_fatura(page)

    sleep(10000)

with sync_playwright() as playwright:
    main(playwright)
