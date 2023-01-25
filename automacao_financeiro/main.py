from playwright.sync_api import Playwright, sync_playwright
from dotenv import load_dotenv
from facta.run_facta import run_facta
from novo_saque.run_novo_saque import run_novo_saque
from time import sleep

load_dotenv()

def main(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel='chromium', downloads_path='.')
    page = browser.new_page()
    # page.goto('http://desenv.facta.com.br/sistemaNovo/login.php')
    page.goto('https://nsaque.ultragate.com.br/login')

    # run_facta(page)
    run_novo_saque(page)

    sleep(1000000)

with sync_playwright() as playwright:
    main(playwright)
