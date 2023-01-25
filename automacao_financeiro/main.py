from playwright.sync_api import Playwright, sync_playwright
from clientes_efetivados.steps.login import login
from clientes_efetivados.steps.set_filters import set_filters
from relatorios_movimentos_fatura.set_filters_relatorios_movimentos_fatura import set_filters_relatorios_movimentos_fatura
from time import sleep

def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium')
    page = browser.new_page()
    page.goto('http://desenv.facta.com.br/sistemaNovo/login.php')

    login(page)

    sleep(5)
    set_filters(page)

    sleep(5)
    set_filters_relatorios_movimentos_fatura(page)

    sleep(10000)

with sync_playwright() as playwright:
    main(playwright)
