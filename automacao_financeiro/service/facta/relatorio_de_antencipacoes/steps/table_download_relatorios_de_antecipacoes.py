from playwright.sync_api import Page

def table_download_relatorio_de_antecipacoes(page: Page):
    page.wait_for_timeout(10000)
    i = 1
    while True:
        ID_GERAR_EXCEL = f'#tabelaRelatorio > tbody > tr:nth-child({i}) > td:nth-child(6) > a > span' 

        element = page.evaluate(
            '(ID_GERAR_EXCEL) => document.querySelector(ID_GERAR_EXCEL)',
            ID_GERAR_EXCEL
        )

        if element == None:
            print('Elemento não encontrado')
            break

        page.click(ID_GERAR_EXCEL)

        i += 1